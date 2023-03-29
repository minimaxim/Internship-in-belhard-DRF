from datetime import datetime

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Group, Course, Category, Audience, Address, Schedule
from .serializers import GroupSerializer, CourseSerializer, CategorySerializer, AudienceSerializer, AddressSerializer, \
    RoleSerializer, ScheduleSerializer
from authentication.models import CustomUser, Role
from authentication.permissions import IsAdminOrManager, IsAdminOrManagerOrMentor, IsAdminOrManagerOrReadOnly, IsAdmin


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminOrManagerOrMentor]
    http_method_names = ['get', 'post', 'put', 'delete']

    def create(self, request, *args, **kwargs):
        if request.user.role.name != 'mentor':
            return super(GroupViewSet, self).create(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN, data={'detail': 'permission'})


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrManagerOrReadOnly]
    http_method_names = ['get', 'post', 'put', 'delete']


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrManagerOrReadOnly]
    http_method_names = ['get', 'post', 'put', 'delete']


class AudienceViewSet(ModelViewSet):
    queryset = Audience.objects.all()
    serializer_class = AudienceSerializer
    permission_classes = [IsAdminOrManagerOrMentor]
    http_method_names = ['get', 'post', 'put', 'delete']

    def create(self, request, *args, **kwargs):
        if request.user.role.name != 'mentor':
            return super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN, data={'detail': 'permission'})


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAdminOrManagerOrMentor]
    http_method_names = ['get', 'post', 'put', 'delete']

    def create(self, request, *args, **kwargs):
        if request.user.role.name != 'mentor':
            return super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN, data={'detail': 'permission'})


class ScheduleViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAdminOrManagerOrReadOnly]
    http_method_names = ['get', 'post', 'put', 'delete']

    def create(self, request, *args, **kwargs):
        days = request.data.get('days')
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            group = get_object_or_404(Group, pk=request.data.get('group'))
            course = get_object_or_404(Course, group=group)
            if course.duration == len(set(days)):
                for day in sorted(days):
                    day = datetime.fromtimestamp(day)
                    schedule = Schedule(day=day, group=group)
                    try:
                        schedule.save()
                    except:
                        pass
                header = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=header)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={'detail': f'duration must be equal {course.duration} or dates is not unique'})
