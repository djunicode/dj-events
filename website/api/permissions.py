from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import APIException
from .models import (
    Students,
    Committee,
    Events,
    CoreCommittee,
    CoCommittee,
)


class StatusException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, detail, status_code=None):
        self.detail = detail
        if status_code is not None:
            self.status_code = status_code


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            Students.objects.get(user__id=request.user.id)
            return True
        except Students.DoesNotExist:
            raise StatusException(detail="Not a Student", status_code=400)


class IsCommittee(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            Committee.objects.get(user__id=request.user.id)
            return True
        except Committee.DoesNotExist:
            raise StatusException(detail="Not a Committee", status_code=400)

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


class ForCoreTaskListAndCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            Committee.objects.get(user__id=view.kwargs["pk2"])
        except Committee.DoesNotExist:
            raise StatusException(
                detail="Committee ID not valid", status_code=400
            )
        try:
            corecom = CoreCommittee.objects.get(
                student__user__id=view.kwargs["pk1"],
                committee__user__id=view.kwargs["pk2"],
            )
        except CoreCommittee.DoesNotExist:
            raise StatusException(
                detail="Core Committee ID not valid", status_code=400
            )
        if corecom.student.user == request.user:
            return True
        else:
            raise StatusException(
                detail="You are not allowed to access", status_code=400
            )


class ForCoTaskList(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            Committee.objects.get(user__id=view.kwargs["pk2"])
        except Committee.DoesNotExist:
            raise StatusException(
                detail="Committee ID not valid", status_code=400
            )
        try:
            cocom = CoCommittee.objects.get(
                student__user__id=view.kwargs["pk1"],
                committee__user__id=view.kwargs["pk2"],
            )
        except CoCommittee.DoesNotExist:
            raise StatusException(
                detail="Co Committee ID not valid", status_code=400
            )
        if cocom.student.user == request.user:
            return True
        else:
            raise StatusException(
                detail="You are not allowed to access", status_code=400
            )
