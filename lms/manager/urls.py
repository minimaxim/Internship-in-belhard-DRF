from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import GroupViewSet, CourseViewSet, CategoryViewSet, AudienceViewSet, AddressViewSet, UserViewSet, \
    RoleViewSet

api_router = SimpleRouter()
api_router.register(r'group', GroupViewSet)
api_router.register(r'course', CourseViewSet)
api_router.register(r'category', CategoryViewSet)
api_router.register(r'audience', AudienceViewSet)
api_router.register(r'address', AddressViewSet)
api_router.register(r'user', UserViewSet)
api_router.register(r'role', RoleViewSet)



urlpatterns = [
    path('', include(api_router.urls)),
]
