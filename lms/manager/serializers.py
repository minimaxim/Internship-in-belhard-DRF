from rest_framework.serializers import ModelSerializer

from .models import Group, Course, Category, Audience, Address, User, Role, Schedule


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'price', 'category', 'duration']


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'number', 'date_start', 'audience', 'course', 'mentor']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class AudienceSerializer(ModelSerializer):
    class Meta:
        model = Audience
        fields = ['id', 'number', 'is_online', 'address']


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'address_name']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'role']


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']


class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'day', 'group']
