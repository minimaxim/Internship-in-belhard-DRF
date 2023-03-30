from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role.name == 'administrator')


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role.name == 'manager')


class IsMentor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role.name == 'mentor')


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role.name == 'student')


class IsAdminOrManager(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role.name in ('administrator', 'manager'))


class IsAdminOrManagerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method == 'GET' or
            request.user and request.user.role.name in ('administrator', 'manager')
        )


class IsAdminOrManagerOrMentor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role.name in ('administrator', 'manager', 'mentor'))



class IsAdminOrManagerOrMentorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method == 'GET' or
            request.user and request.user.role.name in ('administrator', 'manager', 'mentor'))