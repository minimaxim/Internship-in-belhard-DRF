from datetime import datetime

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Group, Course, Category, Audience, Address, Schedule
from .serializers import GroupSerializer, CourseSerializer, CategorySerializer, AudienceSerializer, AddressSerializer, \
    RoleSerializer, ScheduleSerializer
from authentication.models import CustomUser, Role


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

