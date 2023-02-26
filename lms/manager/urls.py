from django.urls import path, include
from rest_framework import routers

from .views import GroupViewSet, CourseViewSet

api_router = routers.DefaultRouter()
api_router.register(r'group', GroupViewSet)
api_router.register(r'course', CourseViewSet)


urlpatterns = [
    path('', include(api_router.urls)),
]