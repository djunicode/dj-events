from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import APIException
from .models import (
    Students,
    Committee,
    Events,
)


class StatusException(APIException):

    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, detail, status_code=None):
        self.detail = detail
        if status_code is not None:
            self.status_code = status_code


class ForEventsCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        event_creator = request.data.get("organisingCommittee")
        committee = Committee.objects.get(user__id=request.user.id)
        if committee:
            if event_creator == committee.id:
                return True
        raise StatusException(
            detail="You are not allowed to access", status_code=400
        )


class ForReferralTable(permissions.BasePermission):
    def has_permission(self, request, view):
        committee = Committee.objects.get(user__id=request.user.id)
        referraltable_committee = Events.objects.get(
            id=view.kwargs["pk"]
        ).organisingCommittee
        if committee == referraltable_committee:
            return True
        else:
            raise StatusException(
                detail="You are not allowed to access", status_code=400
            )


class ForEventLikeDislike(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            request_student = Students.objects.get(user__id=request.user.id)
        except Students.DoesNotExist:
            request_student = None
        try:
            actual_student = Students.objects.get(user__id=view.kwargs["pk2"])
        except Students.DoesNotExist:
            raise StatusException(detail="Invalid Student ID", status_code=400)

        if request_student == actual_student:
            return True
        else:
            raise StatusException(
                detail="You are not allowed to access", status_code=400
            )
