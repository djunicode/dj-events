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

            if user is not None:
                token, _ = Token.objects.get_or_create(user=user)

                # login(request, user)
                data = {
                    "id": user.pk,
                    "Name": user.first_name + " " + user.last_name,
                    "Username": user.username,
                    "SapID": user.sap,
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
def event_like(request, eventName, username):
    if request.method == "POST":
        try:
            student = Students.objects.get(username=username)
            event = Events.objects.get(eventName=eventName)
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
def event_delete(request, eventName, username):
    if request.method == "DELETE":
        try:
            eventlike = EventLikes.objects.filter(
                event__eventName=eventName, student__username=username
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
def core_task_list(request, core):
    if request.method == "GET":
        try:
            tasks = CoCommitteeTasks.objects.filter(
                assigned_by__student__username=core
            )
            serializer = CoCommitteeTasksSerializer(tasks, many=True)
            x = serializer.data[0]["coCommittee"]["student"]
            y = serializer.data[0]["assigned_by"]["student"]
            x.pop("password")
            x.pop("last_login")
            x.pop("is_staff")
            x.pop("is_superuser")
            x.pop("is_active")
            x.pop("date_joined")
            x.pop("groups")
            x.pop("user_permissions")
            y.pop("password")
            y.pop("last_login")
            y.pop("is_staff")
            y.pop("is_superuser")
            y.pop("is_active")
            y.pop("date_joined")
            y.pop("groups")
            y.pop("user_permissions")
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
def core_task_create(request, core):
    if request.method == "POST":
        try:
            coCommittee = request.data.get("coCommittee")
            task = request.data.get("task")
            co = CoCommittee.objects.filter(
                student__username=coCommittee
            ).values("committee")
            core_val = CoreCommittee.objects.filter(
                student__username=core
            ).values("committee")
            core_pk = CoreCommittee.objects.get(student__username=core)
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


@api_view(["PUT", "DELETE"])
def core_task_crud(request, pk):
    try:
        tasks = CoCommitteeTasks.objects.get(pk=pk)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = CoCommitteeTasksSerializer(tasks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        tasks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def co_task_list(request, co):
    if request.method == "GET":
        try:
            tasks = CoCommitteeTasks.objects.filter(
                coCommittee__student__username=co
            )
            serializer = CoCommitteeTasksSerializer(tasks, many=True)
            x = serializer.data[0]["coCommittee"]["student"]
            y = serializer.data[0]["assigned_by"]["student"]
            x.pop("password")
            x.pop("last_login")
            x.pop("is_staff")
            x.pop("is_superuser")
            x.pop("is_active")
            x.pop("date_joined")
            x.pop("groups")
            x.pop("user_permissions")
            y.pop("password")
            y.pop("last_login")
            y.pop("is_staff")
            y.pop("is_superuser")
            y.pop("is_active")
            y.pop("date_joined")
            y.pop("groups")
            y.pop("user_permissions")
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
