from datetime import datetime

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
    http_method_names = ['post',]


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    http_method_names = ['get',]


class ScheduleViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def perform_create(self, serializer):
        days = serializer.data.get('day')
        # При заполнении формы ругается на неверный исо-формат скрин http://joxi.ru/krDdDagCdBDeyr, for начинает перебирать саму дату с первой цифры
        # Для решения этого полученные данные в days сделал списком [] - тогда ошибка не появляется. Но по итогу тогда данные не сохраняются и получаю пустой список на GET
        for day in days:
            day = datetime.fromisoformat(day)
            schedule = Schedule(day=day)
            # Из schedule group=... убрал, т.к. ругалось что должно получать инстанс модели групп. Не прописывая он всё равно передаётся с верным id группы
            try:
                schedule.save()
            except:
                pass
    # Ниже функция с которой данные сохраняются, но сохраняются в таком виде http://joxi.ru/Dr8bEzacDy7742 . Данные сохранялись т.к. явно вызвал self.perform_create(serializer), без него не сохранялось
    # Список дат передать не смог чтобы несколько дат передать в одном id

    # def create(self, request, *args, **kwargs):
    #     day = [request.data.get('day')]
    #     day в формате списка чтобы исключить ошибку в цикле for. Я так понимаю ругалось на длину строки, получаемую в атрибуте day (в fromisoformat есть if на длину получаемых данных)
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         for day in day:
    #             day = datetime.fromisoformat(day)
    #             schedule = Schedule(day=day)
    #             try:
    #                 schedule.save()
    #             except:
    #                 pass
    #         self.perform_create(serializer)
    #         header = self.get_success_headers(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=header)

