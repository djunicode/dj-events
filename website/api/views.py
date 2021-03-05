from django.shortcuts import render, HttpResponse
from rest_framework import generics, status, mixins, permissions
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import (
    TokenAuthentication,
    BasicAuthentication,
)
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
)

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


class CommitteeDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Committee.objects.all()
    serializer_class = CommitteeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CommitteeCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Committee.objects.all()
    serializer_class = CommitteeSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommitteeCrud(
    mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView
):
    queryset = Committee.objects.all()
    serializer_class = CommitteeSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


"""
Events
"""


class EventsList(generics.GenericAPIView):
    def get(self, request):
        events = Events.objects.all()
        event_list = EventsSerializer(events, many=True).data
        return JsonResponse(event_list, status=status.HTTP_200_OK, safe=False)


class EventDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class EventsCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EventCrud(
    mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView
):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Committee Page feed is provided by the following view.
def EventFinder(request, pk):
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


def CommitteeExtraDetail(request, pk):
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


def StudentProfile(request, pk):
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


def ReferralTable(request, pk):
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
                "Referral Count": referrals.filter(coCommittee=cocom).count(),
            }
            data.append(d)
        return JsonResponse(data, status=status.HTTP_200_OK, safe=False)
    except Events.DoesNotExist:
        return JsonResponse(
            {"message": "The event does not exist"},
            status=status.HTTP_204_NO_CONTENT,
        )


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

                # login(request, user)
                data = {
                    "id": user.pk,
                    "Name": user.first_name + " " + user.last_name,
                    "Username": user.username,
                    "SapID": student.sap,
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

                # login(request, user)
                data = {
                    "id": user.pk,
                    "Committee Name": committee.committeeName,
                    "Committee Department": committee.committeeDept,
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


@api_view(["POST"])
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


@api_view(["DELETE"])
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


@api_view(["GET"])
def core_task_list(request, pk):
    if request.method == "GET":
        try:
            tasks = CoCommitteeTasks.objects.filter(
                assigned_by__student__user__id=pk
            ).order_by("coCommittee__committee")
            serializer = CoCommitteeTasksSerializer(tasks, many=True)
            for i in range(len(serializer.data)):
                x1 = serializer.data[i]["coCommittee"]["student"]
                x2 = serializer.data[i]["coCommittee"]["committee"]
                y1 = serializer.data[i]["assigned_by"]["student"]
                y2 = serializer.data[i]["assigned_by"]["committee"]
                x1.pop("password")
                x1.pop("last_login")
                x1.pop("is_staff")
                x1.pop("is_superuser")
                x1.pop("is_active")
                x1.pop("date_joined")
                x1.pop("groups")
                x1.pop("user_permissions")
                y1.pop("password")
                y1.pop("last_login")
                y1.pop("is_staff")
                y1.pop("is_superuser")
                y1.pop("is_active")
                y1.pop("date_joined")
                y1.pop("groups")
                y1.pop("user_permissions")
                x2.pop("password")
                x2.pop("last_login")
                x2.pop("is_staff")
                x2.pop("is_superuser")
                x2.pop("is_active")
                x2.pop("date_joined")
                x2.pop("groups")
                x2.pop("user_permissions")
                y2.pop("password")
                y2.pop("last_login")
                y2.pop("is_staff")
                y2.pop("is_superuser")
                y2.pop("is_active")
                y2.pop("date_joined")
                y2.pop("groups")
                y2.pop("user_permissions")
            return Response(serializer.data, status=status.HTTP_200_OK)
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


@api_view(["POST"])
def core_task_create(request, pk):
    if request.method == "POST":
        try:
            coCommittee = request.data.get("coCommittee")
            task = request.data.get("task")
            co = CoCommittee.objects.filter(
                student__username=coCommittee
            ).values("committee")
            core_val = CoreCommittee.objects.filter(
                student__user__id=pk
            ).values("committee")
            core_pk = CoreCommittee.objects.get(student__user__id=pk)
            co_pk = CoCommittee.objects.get(student__username=coCommittee)
            for x in co:
                co_committee = x["committee"]
            for y in core_val:
                core_committee = y["committee"]
            if co_committee == core_committee:
                tasks = CoCommitteeTasks(
                    coCommittee=co_pk, task=task, assigned_by=core_pk
                )
                tasks.save()
                return Response(
                    {"success": "Task Created"}, status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {
                        "message": "Cannot Create Task For Other Committee Member"
                    },
                    status=status.HTTP_201_CREATED,
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


@api_view(["DELETE"])
def core_task_crud(request, pk1, pk2):
    try:
        tasks = CoCommitteeTasks.objects.get(pk=pk1)
        assigned_by = CoreCommittee.objects.get(student__user__id=pk2)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)
    """
    if request.method == "PUT":
        serializer = CoCommitteeTasksSerializer(tasks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """
    if request.method == "DELETE":
        if assigned_by:
            if tasks.assigned_by == assigned_by:
                tasks.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(
                    {"message": "You do have the required permission"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                {"message": "You do have the required permission"},
                status=status.HTTP_400_BAD_REQUEST,
            )


@api_view(["GET"])
def co_task_list(request, pk1, pk2):
    if request.method == "GET":
        try:
            tasks = CoCommitteeTasks.objects.filter(
                coCommittee__student__user__id=pk1
            )
            serializer = CoCommitteeTasksSerializer(tasks, many=True)
            for i in range(len(serializer.data)):
                x1 = serializer.data[i]["coCommittee"]["student"]
                x2 = serializer.data[i]["coCommittee"]["committee"]
                y1 = serializer.data[i]["assigned_by"]["student"]
                y2 = serializer.data[i]["assigned_by"]["committee"]
                x1.pop("password")
                x1.pop("last_login")
                x1.pop("is_staff")
                x1.pop("is_superuser")
                x1.pop("is_active")
                x1.pop("date_joined")
                x1.pop("groups")
                x1.pop("user_permissions")
                y1.pop("password")
                y1.pop("last_login")
                y1.pop("is_staff")
                y1.pop("is_superuser")
                y1.pop("is_active")
                y1.pop("date_joined")
                y1.pop("groups")
                y1.pop("user_permissions")
                x2.pop("password")
                x2.pop("last_login")
                x2.pop("is_staff")
                x2.pop("is_superuser")
                x2.pop("is_active")
                x2.pop("date_joined")
                x2.pop("groups")
                x2.pop("user_permissions")
                y2.pop("password")
                y2.pop("last_login")
                y2.pop("is_staff")
                y2.pop("is_superuser")
                y2.pop("is_active")
                y2.pop("date_joined")
                y2.pop("groups")
                y2.pop("user_permissions")
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

@api_view(["POST"])
def student_registration(request):
    if request.method == 'POST':
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        confirm = request.data.get('confirm')
        sap = request.data.get('sap')
        department = request.data.get('department')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')        

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
                user = Students.objects.create_user(username=username, password=password, email=email, sap=sap, department=department, first_name=first_name, last_name=last_name)
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
