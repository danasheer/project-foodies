from rest_framework.permissions import BasePermission
from reciepes.models import Reciepe


class IsAuthor(BasePermission):
    message = "You must be the user of this reciepe."

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
