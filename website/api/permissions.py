from rest_framework import permissions
from .models import *
from rest_framework import status
from rest_framework.exceptions import APIException

class StatusException(APIException):

    status_code = status.HTTP_400_BAD_REQUEST


    def __init__(self, detail, status_code=None):
        self.detail = detail
        if status_code is not None:
            self.status_code = status_code


class IsCommitteeExtraDetail(permissions.BasePermission):
 
    def has_permission(self, request, view):
        committee = Committee.objects.filter(user=request.user).first()
        if committee: 
            if committee.id==view.kwargs['pk']:
                return True
        raise StatusException(detail="You are not allowed to access", status_code=400)