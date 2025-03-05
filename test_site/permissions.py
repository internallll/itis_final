from rest_framework import permissions

from test_site.models import Feedback


# Класс разрешения для feedback и questions
class IsOwnerOrAdminOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Если пользователь является админом, то будет доступ

        if request.user.is_staff:
            return True

        # Если пользователь является хозяином какой-либо сущности, то будет доступ
        return obj.user == request.user


# Пока что на данный момент этот класс доступа для User
class IsSelfOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        #
        return obj.pk == request.user.pk


class IsFeedbackOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        user_pk = view.kwargs.get('pk')
        feedbacks = Feedback.objects.filter(user_id=user_pk)
        return all(feedback.user == request.user for feedback in feedbacks)
