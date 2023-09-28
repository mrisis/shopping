from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):

    def has_object_permission(self,request,view,obj):
        user = request.user
        if user.is_anonymous:
            return False
        return  obj.id == user.id













