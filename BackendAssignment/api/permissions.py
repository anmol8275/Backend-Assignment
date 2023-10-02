from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission

User = get_user_model()


class IsPostOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        user = User.objects.filter(email=request.user.email).first()
        return obj.user == user
