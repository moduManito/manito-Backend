from rest_framework import permissions


class IsManitoOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return obj.manito.author == request.user
        if request.method in permissions.SAFE_METHODS:
            return True
