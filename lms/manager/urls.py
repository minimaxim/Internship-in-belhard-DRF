from django.urls import path, include
from rest_framework import routers

from .views import GroupViewSet, CourseViewSet

api_router = routers.DefaultRouter()
api_router.register(r'groups', GroupViewSet)
api_router.register(r'courses', CourseViewSet)


urlpatterns = [
    path('', include(api_router.urls)),
]