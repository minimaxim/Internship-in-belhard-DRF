from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role.name == 'administrator')


class IsAdminOrManager(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role.name in ('administrator', 'manager'))


class IsAdminOrManagerOrMentor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role.name in ('administrator', 'manager', 'mentor'))
