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


class FeedbackViewSet(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN, data={'detail': 'You must be authenticated for '
                                                                          'create a feedback'})

    def update(self, request, *args, **kwargs):
        if request.user.role.name == 'administrator' or request.user.role.name == 'manager':
            return super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN, data={'detail': 'permission'})

    def list(self, request, *args, **kwargs):
        if request.user.is_anonymous or request.user.role.name == 'student' or request.user.role.name == 'mentor':
            queryset = Feedback.objects.filter(is_published=True)
            serializer = FeedbackSerializer(queryset, many=True)
            header = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK, headers=header)
        else:
            queryset = Feedback.objects.all()
            serializer = FeedbackSerializer(queryset, many=True)
            header = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK, headers=header)

    def destroy(self, request, *args, **kwargs):
        if request.user.role.name == 'administrator' or request.user.role.name == 'manager':
            return super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN, data={'detail': 'permission'})


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    # permission_classes = ['IsAdminOrManagerOrMentor', 'IsStudent']

    def create(self, request, *args, **kwargs):
        if request.user.role.name != 'student':
            return super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN, data={'detail': 'permission'})


    def list(self, request, *args, **kwargs):
        if request.user.role.name == 'student':
            my_schedule = Schedule.objects.all()
            user_id = request.user.id
            user = GroupUsers.objects.filter(user=user_id)

            usergroups = []

            for group in user:
                usergroups.append(group.group)

            usergroups1 = list(map(lambda group: group.group, user))

            pastdays = []

            for day in my_schedule:
                if datetime.now() > day.day and day.group in usergroups:
                    pastdays.append(day.id)

            queryset = Task.objects.filter(day__in=pastdays)
            serializer = TaskSerializer(queryset, many=True)
            header = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK, headers=header)

        elif request.user.role.name == 'mentor':
            mentor_id = request.user.id
            groups = Group.objects.filter(mentor=mentor_id)

            mentor_groups = []

            for group in groups:
                mentor_groups.append(group.id)

            mentor_schedule = Schedule.objects.filter(group__in=mentor_groups)

            mentor_days = []

            for day in mentor_schedule:
                mentor_days.append(day.id)

            queryset = Task.objects.filter(day__in=mentor_days)
            serializer = TaskSerializer(queryset, many=True)
            header = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK, headers=header)

        else:
            queryset = Task.objects.all()
            serializer = TaskSerializer(queryset, many=True)
            header = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK, headers=header)

    def update(self, request, *args, **kwargs):
        if request.user.role.name == 'administrator' or request.user.role.name == 'manager':
            return super().update(request, *args, **kwargs)

        elif request.user.role.name == 'mentor':
            mentor_id = request.user.id
            groups = Group.objects.filter(mentor=mentor_id)

            mentor_groups = []

            for group in groups:
                mentor_groups.append(group.id)

            mentor_schedule = Schedule.objects.filter(group__in=mentor_groups)

            mentor_days = []

            for day in mentor_schedule:
                mentor_days.append(day.id)

            queryset = Task.objects.filter(day__in=mentor_days)
            serializer = TaskSerializer(queryset, many=True)
            header = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK, headers=header)
        return Response(status=status.HTTP_403_FORBIDDEN, data={'detail': 'permission'})

    def destroy(self, request, *args, **kwargs):
        if request.user.role.name == 'administrator' or request.user.role.name == 'manager':
            return super().destroy(request, *args, **kwargs)

        elif request.user.role.name == 'mentor':
            mentor_id = request.user.id
            groups = Group.objects.filter(mentor=mentor_id)

            mentor_groups = []

            for group in groups:
                mentor_groups.append(group.id)

            mentor_schedule = Schedule.objects.filter(group__in=mentor_groups)

            mentor_days = []

            for day in mentor_schedule:
                mentor_days.append(day.id)

            queryset = Task.objects.filter(day__in=mentor_days)
            serializer = TaskSerializer(queryset, many=True)
            header = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK, headers=header)
        return Response(status=status.HTTP_403_FORBIDDEN, data={'detail': 'permission'})

