from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsOwnerOrAdminOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Если пользователь является админом то будет доступ

        if request.user.is_staff:
            return True

        # Если пользователь является хозяином какой-либо сущности, то будет доступ
        return obj.owner == request.user

# class IsOwnerFeedback(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.permissions in SAFE_METHODS:


