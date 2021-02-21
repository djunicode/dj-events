from rest_framework import serializers
from .models import Events, Committee


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = [
            "id",
            "eventDescription",
            "eventSummary",
            "eventName",
            "eventDate",
            "eventTime",
            "eventSeatingCapacity",
            "eventVenue",
            "registrationLink",
            "is_referal",
            "organisingCommittee",
            "contactName1",
            "contactName2",
            "contactNumber1",
            "contactNumber2",
        ]


class CommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Committee
        fields = [
            "id",
            "committeeName",
            "committeeDescription",
            "committeeDept",
            "committeeChairperson",
        ]
