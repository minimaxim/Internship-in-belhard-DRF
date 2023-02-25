from rest_framework.serializers import ModelSerializer

from .models import Group, Course


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields =['id', 'name', 'price', 'category']


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'number', 'date_start', 'audience', 'course']