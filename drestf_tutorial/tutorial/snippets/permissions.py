from rest_framework import permissions

# customed permission to only allow owners of an object to edit it.
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # read permissions are allowed to any request, so [GET, HEAD, OPTIONS] are allowed here
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions are allowed to the owner of the object, so [PUT, DELETE] are allowed here
        return obj.owner == request.user