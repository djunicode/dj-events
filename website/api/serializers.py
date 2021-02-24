from rest_framework import serializers
from .models import Events, CoreCommittee, CoCommitteeReferals,CoCommitteeTasks ,CoCommittee, Faculty ,Committee, Students
from django.contrib.auth.password_validation import validate_password

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
            "is_referral",
            "organisingCommittee",
            "contactName1",
            "contactName2",
            "contactNumber1",
            "contactNumber2",
        ]


class CoreCommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model= CoreCommittee
        fields = [
            "id",
            "student",
            "committee",
            "positionAssigned",
        ]

class CoCommitteeReferalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoCommitteeReferals
        fields = [
            "id",
            "student",
            "coCommittee",
            "event",
        ]

class CoCommitteeTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoCommitteeTasks
        fields = [
            "id",
            "coCommittee",
            "task",
        ]

class CoCommitteeSerializer(serializers.ModelSerializer):
    referrals = CoCommitteeReferalsSerializer(many=True)
    tasks = CoCommitteeTasksSerializer(many=True)

    class Meta:
        model= CoCommittee
        fields = [
            "id",
            "student",
            "committee",
            "positionAssigned",
            "referrals",
            "tasks",
        ]

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = [
            "id",
            "name",
            "positionAssigned",
            "committee",
            "department",
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

class CommitteeDetailSerializer(serializers.ModelSerializer):
    events = EventsSerializer(many=True)
    coreCommitteeMembers = CoreCommitteeSerializer(many=True)
    facultyMembers = FacultySerializer(many=True)

    class Meta:
        model = Committee
        fields = [
            "id",
            "committeeName",
            "committeeDescription",
            "committeeDept",
            "committeeChairperson",
            "events",
            "coreCommitteeMembers",
            "facultyMembers",
        ]
        depth=2

class StudentsSerializer(serializers.ModelSerializer):
    coCommittees = CoCommitteeSerializer(many=True)
    coreCommittees = CoreCommitteeSerializer(many=True)

    class Meta:
        model = Students
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "sap",
            "department",
            "coCommittees",
            "coreCommittees"
        ]