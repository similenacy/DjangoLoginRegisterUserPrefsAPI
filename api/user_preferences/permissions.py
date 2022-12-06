from rest_framework import permissions


class OnlyOwnerCanView(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return bool(obj.user == request.user)


class OnlyOwnerAndAdminCanView(permissions.BasePermission):

    def has_permission(self, request, view):
            return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
            return bool((obj.user == request.user) or (request.user.is_staff))





