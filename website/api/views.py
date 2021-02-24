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
from .serializers import EventsSerializer, CommitteeSerializer, CommitteeDetailSerializer, StudentsSerializer, ChangePasswordSerializer
from .models import Events, Committee, Students, CoCommitteeReferals, CoCommittee

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
        EventsSerializer(Events.objects.filter(organisingCommittee=Committee.objects.get(id=pk)), many=True).data, 
        status=status.HTTP_200_OK, 
        safe=False
        )

def CommitteeExtraDetail(request,pk):
    return JsonResponse(
        CommitteeDetailSerializer(Committee.objects.get(id=pk)).data, 
        status=status.HTTP_200_OK, 
        safe=False
        )

def StudentProfile(request,pk):
    return JsonResponse(
        StudentsSerializer(Students.objects.get(id=pk)).data, 
        status=status.HTTP_200_OK, 
        safe=False
        )

def ReferralTable(request,pk):
    event = Events.objects.get(id=pk)
    referrals = CoCommitteeReferals.objects.filter(event=event)
    coCommittee = CoCommittee.objects.filter(committee=event.organisingCommittee)
    data = []
    for cocom in coCommittee:
        d={
            'SAP ID':cocom.student.sap,
            'Name':cocom.student.first_name+" "+cocom.student.last_name,
            'Referral Count':referrals.filter(coCommittee=cocom).count()
        }
        data.append(d)
    return JsonResponse(
        data, 
        status=status.HTTP_200_OK, 
        safe=False
        )