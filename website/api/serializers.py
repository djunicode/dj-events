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
            "registrationLink",
            "organisingCommittee",
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
