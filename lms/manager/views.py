from datetime import datetime

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Group, Course, Category, Audience, Address, User, Role, Schedule, Feedback, Task, GroupUsers
from .serializers import GroupSerializer, CourseSerializer, CategorySerializer, AudienceSerializer, AddressSerializer, \
    UserSerializer, RoleSerializer, ScheduleSerializer, FeedbackSerializer, FeedbackAllSerializer, TaskSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class AudienceViewSet(ModelViewSet):
    queryset = Audience.objects.all()
    serializer_class = AudienceSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post', ]


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    http_method_names = ['get', ]


class ScheduleViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def create(self, request, *args, **kwargs):
        days = request.data.get('days')
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            group = get_object_or_404(Group, pk=request.data.get('group'))
            for day in days:
                day = datetime.fromtimestamp(day)
                schedule = Schedule(day=day, group=group)
                try:
                    schedule.save()
                except:
                    pass
        header = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=header)


class FeedbackForUserViewSet(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    http_method_names = ['post', ]
    permission_classes = ['IsStudent', ]


class FeedbackTrueViewSet(ModelViewSet):
    queryset = Feedback.objects.filter(is_published=True)
    serializer_class = FeedbackSerializer
    http_method_names = ['get', ]


class FeedbackAllViewSet(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackAllSerializer
    http_method_names = ['get', ]
    permission_classes = ['IsAdminOrManager', ]


class FeedbackFalseViewSet(ModelViewSet):
    queryset = Feedback.objects.filter(is_published=False)
    serializer_class = FeedbackAllSerializer
    http_method_names = ['get', 'put', 'delete']
    permission_classes = ['IsAdminOrManager', ]


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = ['IsAdminOrManagerOrMentor', ]


class TaskUserViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = ['get', ]
    permission_classes = ['IsStudent', ]

    def list(self, request, *args, **kwargs):

        my_schedule = Schedule.objects.all()
        user_id = request.user.id
        user = GroupUsers.objects.filter(user=user_id)

        usergroups = []

        for group in user:
            usergroups.append(group.group)

        pastdays = []

        for day in my_schedule:
            if datetime.now() > day.day and day.group in usergroups:
                pastdays.append(day.id)

        queryset = Task.objects.filter(day__in=pastdays)
        serializer = TaskSerializer(queryset, many=True)
        header = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=header)
