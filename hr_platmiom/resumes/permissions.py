from rest_framework import permissions

class IsCandidate(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'CANDIDATE'

class IsHR(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'HR'

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'ADMIN'

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.user.role == 'ADMIN'