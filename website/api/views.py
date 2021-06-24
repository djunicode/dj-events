from django.shortcuts import render, HttpResponse
from rest_framework import generics, status, mixins, permissions
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (
    TokenAuthentication,
    BasicAuthentication,
)
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from .serializers import (
    EventsSerializer,
    CommitteeSerializer,
    CommitteeDetailSerializer,
    StudentsSerializer,
    EventLikeSerializer,
    CoCommitteeTasksSerializer,
    ChangePasswordSerializer,
    CoCommitteeSerializer,
    CoreCommitteeSerializer,
    ListStudentSerializer,
)
from .models import (
    Events,
    Committee,
    Students,
    CoCommitteeReferals,
    CoCommittee,
    EventLikes,
    CoCommitteeTasks,
    CoreCommittee,
    CommitteeToSubscribers,
)
from .permissions import (
    ForEventsCreate,
    ForReferralTable,
    ForEventLikeDislike,
    ForCoreTaskListAndCreate,
    ForCoTaskList,
    IsStudent,
    IsCommittee,
    IsParticularCommittee,
    IsItTheSameCommittee,
    ForEventLikeCheck,
)
from django.db.models import Q

"""
Committees
"""


class CommitteeList(generics.GenericAPIView):
    def get(self, request):
        committee = Committee.objects.all()
        committees_list = CommitteeSerializer(committee, many=True).data
        return JsonResponse(
            committees_list, status=status.HTTP_200_OK, safe=False
        )


# Detail of a particular committee based on id("GET" request)
class CommitteeDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Committee.objects.all()
    serializer_class = CommitteeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# Update/Delete of a particular committee based on id("DELETE" or "PUT" request)
# check if committee is updated/deleted by that committee only
class CommitteeCrud(
    mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView
):
    queryset = Committee.objects.all()
    serializer_class = CommitteeSerializer
    permission_classes = (IsAuthenticated, IsCommittee, IsItTheSameCommittee)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return JsonResponse(
            {"message": "Committee Deleted Successfully"},
            status=status.HTTP_200_OK,
            safe=False,
        )


"""
Events
"""

# List of all Events("GET" request)


class EventsList(generics.GenericAPIView):
    def get(self, request):
        events = Events.objects.all()
        event_list = EventsSerializer(events, many=True).data
        return JsonResponse(event_list, status=status.HTTP_200_OK, safe=False)


# Detail of a particular event based on id("GET" request)
class EventDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# Creating a new event("POST")
class EventsCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    permission_classes = (
        IsAuthenticated,
        IsCommittee,
        ForEventsCreate,
    )

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Update/Delete of a particular event based on id("DELETE" or "PUT" request)
# check if event is edited/deleted for a particular committee by that committee only
class EventCrud(
    mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView
):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    permission_classes = (IsAuthenticated, IsCommittee, IsParticularCommittee)

    def put(self, request, *args, **kwargs):

        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return JsonResponse(
            {"message": "Event Deleted Successfully"},
            status=status.HTTP_200_OK,
            safe=False,
        )


# Committee Page feed is provided by the following view.
@api_view(["GET"])
def EventFinder(request, pk):
    if request.method == "GET":
        try:
            return JsonResponse(
                EventsSerializer(
                    Events.objects.filter(
                        organisingCommittee=Committee.objects.get(id=pk)
                    ),
                    many=True,
                ).data,
                status=status.HTTP_200_OK,
                safe=False,
            )
        except Exception:
            return JsonResponse(
                data={"Message": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    else:
        return JsonResponse(
            data={"Message": "Only GET request allowed"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
def CommitteeExtraDetail(request, pk):
    if request.method == "GET":
        try:
            committee = Committee.objects.get(id=pk)
            return JsonResponse(
                CommitteeDetailSerializer(committee).data,
                status=status.HTTP_200_OK,
                safe=False,
            )
        except Committee.DoesNotExist:
            return JsonResponse(
                {"message": "The committee does not exist"},
                status=status.HTTP_204_NO_CONTENT,
            )
    else:
        return JsonResponse(
            data={"Message": "Only GET request allowed"},
            status=status.HTTP_400_BAD_REQUEST,
        )


# Student Profile and Detail View
@api_view(["GET"])
@permission_classes([IsAuthenticated, IsStudent])
def StudentProfile(request, pk):
    if request.method == "GET":
        if request.user.id != pk:
            return JsonResponse(
                {"message": "You cannot access details of other students"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        try:
            student = Students.objects.get(id=pk)
            return JsonResponse(
                StudentsSerializer(student).data,
                status=status.HTTP_200_OK,
                safe=False,
            )
        except Students.DoesNotExist:
            return JsonResponse(
                {"message": "The student does not exist"},
                status=status.HTTP_204_NO_CONTENT,
            )
    else:
        return JsonResponse(
            data={"Message": "Only GET request allowed"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated, IsCommittee, ForReferralTable])
def ReferralTable(request, pk):
    if request.method == "GET":
        try:
            event = Events.objects.get(id=pk)
            referrals = CoCommitteeReferals.objects.filter(event=event)
            coCommittee = CoCommittee.objects.filter(
                committee=event.organisingCommittee
            )
            data = []
            for cocom in coCommittee:
                d = {
                    "SAP ID": cocom.student.sap,
                    "Name": cocom.student.first_name
                    + " "
                    + cocom.student.last_name,
                    "Referral Count": referrals.filter(
                        coCommittee=cocom
                    ).count(),
                }
                data.append(d)
            return JsonResponse(data, status=status.HTTP_200_OK, safe=False)
        except Events.DoesNotExist:
            return JsonResponse(
                {"message": "The event does not exist"},
                status=status.HTTP_204_NO_CONTENT,
            )
    else:
        return JsonResponse(
            data={"Message": "Only GET request allowed"},
            status=status.HTTP_400_BAD_REQUEST,
        )


# Login of a student
@api_view(["POST"])
def student_login(request):
    if request.method == "POST":
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            user = authenticate(request, username=username, password=password)
            student = Students.objects.get(user=user)

            if user is not None:
                token, _ = Token.objects.get_or_create(user=user)

                login(request, user)
                data = {
                    "id": user.pk,
                    "Name": user.first_name + " " + user.last_name,
                    "Username": user.username,
                    "Email": user.email,
                    "Department": student.department,
                    "SapID": student.sap,
                    "Token": token.key,
                }

                return JsonResponse(data=data, status=status.HTTP_200_OK)
            else:
                data = {"Message": "There was error authenticating"}
                return JsonResponse(
                    data=data, status=status.HTTP_400_BAD_REQUEST
                )
        except Exception:
            return JsonResponse(
                data={"Message": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    else:
        return JsonResponse(
            data={"Message": "Only POST request allowed"},
            status=status.HTTP_400_BAD_REQUEST,
        )


# Login of a Committee
@api_view(["POST"])
def committee_login(request):
    if request.method == "POST":
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            user = authenticate(request, username=username, password=password)
            committee = Committee.objects.get(user=user)
            if user is not None:
                token, _ = Token.objects.get_or_create(user=user)

                login(request, user)
                data = {
                    "id": user.pk,
                    "CommitteeName": committee.committeeName,
                    "CommitteeDepartment": committee.committeeDept,
                    "Token": token.key,
                }
                return JsonResponse(data, status=status.HTTP_200_OK)
            else:
                data = {"Message": "There was error authenticating"}
                return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return JsonResponse(
                data={"Message": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    else:
        return JsonResponse(
            data={"Message": "Only POST request allowed"},
            status=status.HTTP_400_BAD_REQUEST,
        )


# Liking of an Event
@api_view(["POST"])
@permission_classes([IsAuthenticated, IsStudent, ForEventLikeDislike])
def event_like(request, pk1, pk2):
    if request.method == "POST":
        try:
            student = Students.objects.get(user__id=pk2)
            event = Events.objects.get(id=pk1)
            liked = EventLikes.objects.filter(student=student, event=event)
            if liked:
                return Response({"message": "Event Already Liked"})
            else:
                eventliked = EventLikes(student=student, event=event)
                eventliked.save()
                return Response(
                    {"success": "Event Liked"}, status=status.HTTP_201_CREATED
                )
        except Exception:
            return JsonResponse(
                data={"Message": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    else:
        return JsonResponse(
            data={"Message": "Only POST request allowed"},
            status=status.HTTP_400_BAD_REQUEST,
        )


# Dis-Liking of an Event
@api_view(["DELETE"])
@permission_classes([IsAuthenticated, IsStudent, ForEventLikeDislike])
def event_dislike(request, pk1, pk2):
    if request.method == "DELETE":
        try:
            eventlike = EventLikes.objects.filter(
                event__id=pk1, student__user__id=pk2
            )
            if eventlike:
                eventlike.delete()
                return Response(
                    {"success": "Event DisLiked"}, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"message": "Event Not Liked Previously"},
                    status=status.HTTP_200_OK,
                )
        except Exception:
            return JsonResponse(
                data={"Message": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    else:
        return JsonResponse(
            data={"Message": "Only DELETE request allowed"},
            status=status.HTTP_400_BAD_REQUEST,
        )


# List Of Tasks Assigned by Core
# List depends upon the committee the core selects
@api_view(["GET"])
@permission_classes([IsAuthenticated, IsStudent, ForCoreTaskListAndCreate])
def core_task_list(request, pk1, pk2):
    if request.method == "GET":
        try:
            tasks = CoCommitteeTasks.objects.filter(
                assigned_by__student__user__id=pk1,
                assigned_by__committee__user__id=pk2,
            )
            if tasks:
                serializer = CoCommitteeTasksSerializer(tasks, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return JsonResponse(
                    data={"Message": "Core Member not part of committee"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception:
            return JsonResponse(
                data={"Message": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    else:
        return JsonResponse(
            data={"Message": "Only GET request allowed"},
            status=status.HTTP_400_BAD_REQUEST,
        )


# Creating Of Tasks by Core
@api_view(["POST"])
@permission_classes([IsAuthenticated, IsStudent, ForCoreTaskListAndCreate])
def core_task_create(request, pk1, pk2):
    if request.method == "POST":
        try:
            coCommittee = request.data.get("coCommittee")
            task = request.data.get("task")

            co = CoCommittee.objects.filter(
                student__username=coCommittee
            ).values("committee")
            core_val = CoreCommittee.objects.filter(
                student__user__id=pk1
            ).values("committee")
            for x in Committee.objects.filter(id=pk2).values("id"):
                committee_associated = x["id"]
            co_com_list = []
            core_com_list = []
            for x in co:
                co_com_list.append(x["committee"])
            for y in core_val:
                core_com_list.append(y["committee"])
            if co_com_list and core_com_list:
                if (
                    committee_associated in core_com_list
                    and committee_associated in co_com_list
                ):
                    core_pk = CoreCommittee.objects.get(
                        student__user__id=pk1,
                        committee__user__id=committee_associated,
                    )
                    co_pk = CoCommittee.objects.get(
                        student__username=coCommittee,
                        committee__user__id=committee_associated,
                    )
                    tasks = CoCommitteeTasks(
                        coCommittee=co_pk, task=task, assigned_by=core_pk
                    )
                    tasks.save()
                    return Response(
                        {"success": "Task Created"},
                        status=status.HTTP_201_CREATED,
                    )
                else:
                    return Response(
                        {"message": "Not authorised"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(
                    {
                        "message": "Requested Core Committee/ Co Committee member not found"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception:
            return JsonResponse(
                data={"Message": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    else:
        return JsonResponse(
            data={"Message": "Only POST request allowed"},
            status=status.HTTP_400_BAD_REQUEST,
        )


# Delete Task by Core
@api_view(["DELETE"])
@permission_classes([IsAuthenticated, IsStudent])
def core_task_crud(request, pk1, pk2):
    try:
        tasks = CoCommitteeTasks.objects.get(id=pk2)
        commid = tasks.assigned_by.committee.user.id
    except Exception:
        return Response(
            data={"Message": "Task not found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    try:
        assigned_by = CoreCommittee.objects.get(
            student__user__id=pk1, committee__user__id=commid
        )
        print(assigned_by)
    except Exception:
        return Response(
            data={"Message": "Core Committee Member not found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    if request.method == "DELETE":
        if assigned_by.student.user == request.user:
            if tasks.assigned_by == assigned_by:
                tasks.delete()
                return Response(
                    data={"Message": "Deleted Successfully"},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"message": "You do have the required permission1"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                {"message": "You do have the required permission2"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    else:
        return JsonResponse(
            data={"Message": "Only DELETE request allowed"},
            status=status.HTTP_400_BAD_REQUEST,
        )


# List Of Tasks Assigned to Co
# List depends upon the committee the co selects
@api_view(["GET"])
@permission_classes([IsAuthenticated, IsStudent, ForCoTaskList])
def co_task_list(request, pk1, pk2):
    if request.method == "GET":
        try:
            tasks = CoCommitteeTasks.objects.filter(
                coCommittee__student__user__id=pk1,
                coCommittee__committee__user__id=pk2,
            )
            serializer = CoCommitteeTasksSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return JsonResponse(
                data={"Message": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    else:
        return JsonResponse(
            data={"Message": "Only POST request allowed"},
            status=status.HTTP_400_BAD_REQUEST,
        )


# Student Registration
@api_view(["POST"])
def student_registration(request):
    if request.method == "POST":
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        confirm = request.data.get("confirm")
        sap = request.data.get("sap")
        department = request.data.get("department")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")

        if password == confirm:
            if Students.objects.filter(sap=sap).exists():
                return JsonResponse(
                    data={"Message": "SAP Already registered"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if Students.objects.filter(username=username).exists():
                return JsonResponse(
                    data={"Message": "Username Taken"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            elif Students.objects.filter(email=email).exists():
                return JsonResponse(
                    data={"Message": "Email Taken"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                user = Students.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    sap=sap,
                    department=department,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.save()
                return JsonResponse(
                    data={"Message": "User Created"},
                )
        else:
            return JsonResponse(
                data={"Message": "Passwords Do Not Match"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    else:
        return JsonResponse(
            data={"Message": "Only POST request allowed"},
            status=status.HTTP_400_BAD_REQUEST,
        )


# Change Of password
class ChangePasswordView(generics.UpdateAPIView):

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(
                serializer.data.get("old_password")
            ):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Password updated successfully",
                "data": [],
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Creation of core committee by committee
@csrf_exempt
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upgradeToCoreCom(request, pk, position):
    try:
        committee = Committee.objects.get(user=request.user)
        to_be_upgraded = Students.objects.get(id=pk)

        if CoreCommittee.objects.filter(
            student=to_be_upgraded, committee=committee
        ).exists():
            return JsonResponse(
                data={
                    "detail": f"{to_be_upgraded.username} is already a core member for {committee}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        CoreCommittee.objects.create(
            student=to_be_upgraded,
            committee=committee,
            positionAssigned=position,
        )
        _ = CoCommittee.objects.filter(
            student=to_be_upgraded, committee=committee
        )
        if _.exists():
            _.delete()

        return JsonResponse(
            data={
                "detail": f"{to_be_upgraded.username} upgraded successfully",
            },
            status=status.HTTP_200_OK,
        )

    except Committee.DoesNotExist:
        return JsonResponse(
            data={
                "detail": f" {request.user} is not a committee",
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )


# Creation of co committee by committee
@csrf_exempt
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upgradeToCoCom(request, pk, position):
    try:
        committee = Committee.objects.get(user=request.user)
        to_be_upgraded = Students.objects.get(id=pk)

        if CoCommittee.objects.filter(
            student=to_be_upgraded, committee=committee
        ).exists():
            return JsonResponse(
                data={
                    "detail": f"{to_be_upgraded.username} is already a co-committee member for {committee}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        CoCommittee.objects.create(
            student=to_be_upgraded,
            committee=committee,
            positionAssigned=position,
        )
        _ = CoreCommittee.objects.filter(
            student=to_be_upgraded, committee=committee
        )
        if _.exists():
            _.delete()

        return JsonResponse(
            data={
                "detail": f"{to_be_upgraded.username} upgraded successfully",
            },
            status=status.HTTP_200_OK,
        )

    except Committee.DoesNotExist:
        return JsonResponse(
            data={
                "detail": f" {request.user} is not a committee",
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )


# Lists core committee members
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def listCoreCommittee(request, pk):
    try:
        committee = Committee.objects.get(id=pk)
        return JsonResponse(
            CoreCommitteeSerializer(
                CoreCommittee.objects.filter(committee=committee), many=True
            ).data,
            safe=False,
        )

    except Committee.DoesNotExist:
        return JsonResponse(
            data={
                "detail": f" {request.user} is not a committee",
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )


# Lists co committee members
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def listCoCommittee(request, pk):
    try:
        committee = Committee.objects.get(id=pk)
        return JsonResponse(
            CoCommitteeSerializer(
                CoCommittee.objects.filter(committee=committee), many=True
            ).data,
            safe=False,
        )

    except Committee.DoesNotExist:
        return JsonResponse(
            data={
                "detail": f" {request.user} is not a committee",
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )


# List of members not in the co committee
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def listNonCoCommittee(request, pk):
    try:
        committee = Committee.objects.get(id=pk)
        cocommittee = CoCommittee.objects.filter(committee=committee)
        cocomstudents = set()
        for i in cocommittee:
            cocomstudents.add(i.student)
        students = Students.objects.all()
        students = set(students)
        students = students.difference(cocomstudents)
        return JsonResponse(
            ListStudentSerializer(students, many=True).data,
            safe=False,
        )

    except Committee.DoesNotExist:
        return JsonResponse(
            data={
                "detail": f" {request.user} is not a committee",
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )


# List of members not in the core committee
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def listNonCoreCommittee(request, pk):
    try:
        committee = Committee.objects.get(id=pk)
        corecommittee = CoreCommittee.objects.filter(committee=committee)
        corecomstudents = set()
        for i in corecommittee:
            corecomstudents.add(i.student)
        students = Students.objects.all()
        students = set(students)
        students = students.difference(corecomstudents)
        return JsonResponse(
            ListStudentSerializer(students, many=True).data,
            safe=False,
        )

    except Committee.DoesNotExist:
        return JsonResponse(
            data={
                "detail": f" {request.user} is not a committee",
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )


# Deletes core committee members
@csrf_exempt
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def deleteCoreCommittee(request, pk):
    try:
        committee = Committee.objects.get(user=request.user)
        x = CoreCommittee.objects.get(id=pk)
        if x.committee == committee:
            CoreCommittee.objects.get(id=pk).delete()
        else:
            return JsonResponse(
                data={
                    "detail": f" {request.user} is not authorized to alter {x.committee}'s core-committee.",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return JsonResponse(
            data={
                "detail": f"{x} has been deleted from the core committee of {committee}",
            },
            status=status.HTTP_200_OK,
        )

    except Committee.DoesNotExist:
        return JsonResponse(
            data={
                "detail": f" {request.user} is not a committee",
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )


# Deletes co committee members
@csrf_exempt
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def deleteCoCommittee(request, pk):
    try:
        committee = Committee.objects.get(user=request.user)
        x = CoCommittee.objects.get(id=pk)
        if x.committee == committee:
            x.delete()
        else:
            return JsonResponse(
                data={
                    "detail": f" {request.user} is not authorized to alter {x.committee}'s co-committee ",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        return JsonResponse(
            data={
                "detail": f"{x} has been deleted from the co-committee of {committee}",
            },
            status=status.HTTP_200_OK,
        )

    except Committee.DoesNotExist:
        return JsonResponse(
            data={
                "detail": f" {request.user} is not a committee",
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )


@api_view(["POST"])
@permission_classes([IsAuthenticated, IsCommittee])
def changeCoCommitteePosition(request, updationId):
    try:
        committee = Committee.objects.get(committeeName=request.user)
        to_be_updated = CoCommittee.objects.get(id=updationId)
        if (
            to_be_updated.committee == committee
            and to_be_updated.positionAssigned
            != request.data.get("updatedPosition")
        ):
            to_be_updated.positionAssigned = request.data.get(
                "updatedPosition"
            )
            to_be_updated.save()

            return JsonResponse(
                data={
                    "detail": f" {request.user}'s position updated ",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        elif (
            to_be_updated.committee == committee
            and to_be_updated.positionAssigned
            == request.data.get("updatedPosition")
        ):
            return JsonResponse(
                data={
                    "detail": f" {to_be_updated.student}'s new position is same as before. Hence, not updated",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        else:
            return JsonResponse(
                data={
                    "detail": f" {request.user} is not authorized to alter {to_be_updated.committee}'s co-committee ",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

    except Committee.DoesNotExist:
        return JsonResponse(
            data={
                "detail": f" {request.user} is not a committee",
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )


@api_view(["POST"])
@permission_classes([IsAuthenticated, IsCommittee])
def changeCoreCommitteePosition(request, updationId):
    try:
        committee = Committee.objects.get(committeeName=request.user)
        to_be_updated = CoreCommittee.objects.get(id=updationId)
        if (
            to_be_updated.committee == committee
            and to_be_updated.positionAssigned
            != request.data.get("updatedPosition")
        ):
            to_be_updated.positionAssigned = request.data.get(
                "updatedPosition"
            )
            to_be_updated.save()

            return JsonResponse(
                data={
                    "detail": f" {request.user}'s position updated ",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        elif (
            to_be_updated.committee == committee
            and to_be_updated.positionAssigned
            == request.data.get("updatedPosition")
        ):
            return JsonResponse(
                data={
                    "detail": f" {to_be_updated.student}'s new position is same as before. Hence, not updated",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        else:
            return JsonResponse(
                data={
                    "detail": f" {request.user} is not authorized to alter {to_be_updated.committee}'s core-committee ",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

    except Committee.DoesNotExist:
        return JsonResponse(
            data={
                "detail": f" {request.user} is not a committee",
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )


def studentList(request):
    return JsonResponse(
        StudentsSerializer(Students.objects.all(), many=True).data, safe=False
    )


# To implement Forgot Password API
def sendmail(receiver, subject, body):
    msg = MIMEMultipart()
    msg["From"] = "unicodeevents12@gmail.com"  # enter YOUR EMAIL ADDRESS
    password = "Unicode@123"  # enter YOUR PASSWORD
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.attach(MIMEText(body))

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(msg["From"], password)
    s.sendmail(msg["From"], msg["To"], msg.as_string())
    s.quit()


class StudentForgotPassword(APIView):
    def post(self, request):
        sap = request.data.get("sap")
        if Students.objects.filter(sap=sap).exists():
            student = Students.objects.get(sap=sap)
            student.otp_generator()
            email_body = (
                "Hello, please use the OTP (One Time Password) "
                + str(student.otp)
                + " to reset your password"
            )
            sendmail(student.email, "Password Reset Mail", str(email_body))
            return Response(
                {
                    "message": "Email sent successfully",
                    "user_id": student.user.id,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "Student does not exists"},
                status=status.HTTP_404_NOT_FOUND,
            )


class CommitteeForgotPassword(APIView):
    def post(self, request):
        email = request.data.get("email")
        if Committee.objects.filter(email=email).exists():
            committee = Committee.objects.get(email=email)
            committee.otp_generator()
            email_body = (
                "Hello, please use the OTP (One Time Password) "
                + str(committee.otp)
                + " to reset your password"
            )
            sendmail(committee.email, "Password Reset Mail", str(email_body))
            return Response(
                {
                    "message": "Email sent successfully",
                    "user_id": committee.user.id,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "Committee does not exists"},
                status=status.HTTP_404_NOT_FOUND,
            )


@api_view(["POST"])
def OTPChecker(request, id):
    otp = request.data.get("otp")
    if User.objects.get(id=id):
        user = User.objects.get(id=id)
        if Students.objects.get(user=user):
            studentorcommittee = Students.objects.get(user=user)
        else:
            studentorcommittee = Committee.objects.get(user=user)
        if studentorcommittee.otp == int(otp):
            studentorcommittee.otp = 0
            studentorcommittee.save()
            return Response(
                {"message": "OTP matched!, user is validated"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "OTP did not match"},
                status=status.HTTP_400_BAD_REQUEST,
            )
    else:
        return Response(
            {"message": "User does not exists"},
            status=status.HTTP_404_NOT_FOUND,
        )


@api_view(["POST"])
def ChangePassword(request, id):
    user = User.objects.get(id=id)
    new_password = request.data.get("new_password")
    confirm_password = request.data.get("confirm_password")
    if new_password == confirm_password:
        user.set_password(new_password)
        user.otp = 0
        user.save()
        return Response(
            {"message": "Password changed successfully"},
            status=status.HTTP_200_OK,
        )
    else:
        return Response(
            {"message": "Passwords do not match"},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated, ForEventLikeCheck])
def EventLikeCheck(request, event_id, student_id):
    try:
        event = Events.objects.get(id=event_id)
    except Exception:
        return Response(
            {"message": "Event does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )
    try:
        student = Students.objects.get(id=student_id)
    except Exception:
        return Response(
            {"message": "Student does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    try:
        EventLikes.objects.get(student=student, event=event)
        return Response({"event_liked": True}, status=status.HTTP_200_OK)
    except Exception:
        return Response({"event_liked": False}, status=status.HTTP_200_OK)


@api_view(["POST"])
def event_search(request):
    if request.method == "POST":
        search = request.data.get("q")
        events = Events.objects.filter(Q(eventName__icontains=search))
        if events:
            event_list = EventsSerializer(events, many=True).data
            return JsonResponse(
                event_list, status=status.HTTP_200_OK, safe=False
            )
        else:
            return JsonResponse(
                {"message": "No Events Found"}, status=status.HTTP_200_OK
            )


@api_view(["POST"])
def committee_search(request):
    if request.method == "POST":
        search = request.data.get("q")
        committees = Committee.objects.filter(
            Q(committeeName__icontains=search)
        )
        if committees:
            committee_list = CommitteeSerializer(committees, many=True).data
            return JsonResponse(
                committee_list, status=status.HTTP_200_OK, safe=False
            )
        else:
            return JsonResponse(
                {"message": "No Committees Found"}, status=status.HTTP_200_OK
            )
@api_view(["GET"])
def get_liked_events_for_a_user(request, student_id):
    x = EventLikes.objects.filter(student=student_id)
    array_of_event_ids = []
    for each in x:
        array_of_event_ids.append(each.event.id)
    events = [Events.objects.get(id = id) for id in array_of_event_ids]
    array_of_event_ids.clear()
    return JsonResponse(EventsSerializer(events, many=True).data, status=status.HTTP_200_OK, safe=False)

@api_view(["GET"])
def get_followers_for_committee(request, committee_id):
    followers = CommitteeToSubscribers.objects.filter(committee=Committee.objects.get(id=committee_id))
    return JsonResponse(
        {"follower_count" : len(followers)}, status=status.HTTP_200_OK
    )

#Committee Logout
@permission_classes([IsAuthenticated, IsCommittee])
def committee_logout(request):
    x = f"{request.user} was logged out"
    committee = Committee.objects.get(username=request.user)
    committee.auth_token.delete()
    return JsonResponse(
        {"Message" : x, "id": -1}, status=status.HTTP_200_OK
    )

#Student Logout
@permission_classes([IsAuthenticated, IsStudent])
def student_logout(request):
    x = f"{request.user} was logged out"
    student = Students.objects.get(username=request.user)
    student.auth_token.delete()
    return JsonResponse(
        {"Message" : x, "id": -1}, status=status.HTTP_200_OK
    )

@api_view(["GET"])
#sorts events by date and if two events fall on the same date then the are sorted according to their time.
def event_sorter(request):
    all_events = Events.objects.order_by('-eventDate', 'eventTime')
    return JsonResponse(EventsSerializer(all_events, many=True).data, status=status.HTTP_200_OK, safe=False)


@api_view(["POST"])
@permission_classes([IsAuthenticated, IsStudent])
def follow_committee(request, student_id, committee_id):
    if request.user.id == student_id:
        committee = Committee.objects.get(id=committee_id)
        student = Students.objects.get(id=student_id)
        if CommitteeToSubscribers.objects.filter(subscribers=student, committee=committee).exists():
            return JsonResponse(
            {"Message" : f"{student.username} is already a follower"}, safe=True, status=status.HTTP_200_OK
        )
        CommitteeToSubscribers.objects.create(subscribers=student, committee=committee)
        return JsonResponse(
            {"Message" : f"followed {committee.username}"}, safe=True, status=status.HTTP_200_OK
        )
    else:
        return JsonResponse(
        {"Message" : f"unauthorized"}, safe=True, status=status.HTTP_401_UNAUTHORIZED
    )

@api_view(["POST"])
@permission_classes([IsAuthenticated, IsStudent])
def unfollow_committee(request, student_id, committee_id):
    if request.user.id == student_id:
        committee = Committee.objects.get(id=committee_id)
        student = Students.objects.get(id=student_id)
        if not CommitteeToSubscribers.objects.filter(subscribers=student, committee=committee):
            return JsonResponse(
            {"Message" : f"{student.username} is not a follwer"}, safe=True, status=status.HTTP_200_OK
        )
        CommitteeToSubscribers.objects.get(subscribers=student, committee=committee).delete()
        return JsonResponse(
            {"Message" : f"unfollowed {committee.username}"}, safe=True, status=status.HTTP_200_OK
        )
    else:
        return JsonResponse(
        {"Message" : f"unauthorized"}, safe=True, status=status.HTTP_401_UNAUTHORIZED
    )

@api_view(['GET'])
def creation_time_sorter(request):
    events = Events.objects.order_by("-id")
    event_list = EventsSerializer(events, many=True).data
    return JsonResponse(event_list, status=status.HTTP_200_OK, safe=False)

@api_view(['GET'])
def committees_followed(request, student_id):
    student = Students.objects.get(id=student_id)
    committees_followed = CommitteeToSubscribers.objects.filter(subscribers=student)
    array_of_followed_committees_ids = []
    for each in committees_followed:
        array_of_followed_committees_ids.append(each.committee.id)
    committees  = [Committee.objects.get(id = id) for id in array_of_followed_committees_ids]
    array_of_followed_committees_ids.clear()
    return JsonResponse(CommitteeSerializer(committees, many=True).data, status=status.HTTP_200_OK, safe=False)

@api_view(['GET'])
def get_events_for_followed_committees(request, student_id):
    student = Students.objects.get(id=student_id)
    committees_followed = CommitteeToSubscribers.objects.filter(subscribers=student)
    array_of_followed_committees_ids = []
    for each in committees_followed:
        array_of_followed_committees_ids.append(each.committee.id)
    committees  = [Committee.objects.get(id = id) for id in array_of_followed_committees_ids]
    array_of_followed_committees_ids.clear()
    events = []
    for each in committees:
        events.append(EventsSerializer(Events.objects.filter(organisingCommittee=each), many=True).data)
    print(events)
    return JsonResponse({"data":events}, status=status.HTTP_200_OK, safe=False)

