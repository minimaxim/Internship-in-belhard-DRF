from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import GroupViewSet, CourseViewSet, CategoryViewSet, AudienceViewSet, AddressViewSet, UserViewSet, \
    RoleViewSet, ScheduleViewSet, FeedbackTrueViewSet, FeedbackForUserViewSet, FeedbackAllViewSet, FeedbackFalseViewSet, \
    TaskViewSet, TaskUserViewSet

api_router = SimpleRouter()

api_router.register(r'group', GroupViewSet)
api_router.register(r'course', CourseViewSet)
api_router.register(r'category', CategoryViewSet)
api_router.register(r'audience', AudienceViewSet)
api_router.register(r'address', AddressViewSet)
api_router.register(r'user', UserViewSet)
api_router.register(r'role', RoleViewSet)
api_router.register(r'schedule', ScheduleViewSet)
api_router.register(r'feedback', FeedbackForUserViewSet)
api_router.register(r'feedback-true', FeedbackTrueViewSet)
api_router.register(r'feedback-all', FeedbackAllViewSet)
api_router.register(r'feedback-false', FeedbackFalseViewSet)
api_router.register(r'tasks', TaskViewSet)
api_router.register(r'mytasks', TaskUserViewSet)

urlpatterns = [
    path('', include(api_router.urls))
]
