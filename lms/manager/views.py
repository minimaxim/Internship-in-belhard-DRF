from datetime import datetime

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Group, Course, Category, Audience, Address, User, Role, Schedule
from .serializers import GroupSerializer, CourseSerializer, CategorySerializer, AudienceSerializer, AddressSerializer, \
    UserSerializer, RoleSerializer, ScheduleSerializer


class IsManagerOrReadOnly(IsAuthenticatedOrReadOnly):

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.is_staff
        )


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AudienceViewSet(ModelViewSet):
    queryset = Audience.objects.all()
    serializer_class = AudienceSerializer


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


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

    def create(self, request, *args, **kwargs):
        lesson_day = request.data.get('lesson_day')
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            group = get_object_or_404(Group, pk=request.data.get('group'))
            for day in lesson_day:
                day = datetime.fromtimestamp(day)
                schedule = Schedule(lesson_day=day, group=group)
                try:
                    schedule.save()
                except:
                    pass
        header = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=header)


