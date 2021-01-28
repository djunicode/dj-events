import json
from .models import Events, Committee
from .serializers import *

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from django.utils import timezone
import pytz


class CreateCommitteeTestCase(APITestCase):
    def test_create_committee(self):
        data = {
            "committeeName": "TestCommittee3",
            "committeeDescription": "A Student Chapter Helping Students to Make Web Apps and Mobile Apps",
            "committeeDept": "Computer Engineering",
            "committeeChairperson": "Test Person",
        }
        response = self.client.post("/api/committees/new/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CreateEventTestCase(APITestCase):
    def setUp(self):
        Committee.objects.create(
            committeeName="TestCommittee4",
            committeeDescription="A Student Chapter Helping Students to Make Web Apps and Mobile Apps",
            committeeDept="Computer Engineering",
            committeeChairperson="TestPerson",
        )

    def test_create_event(self):
        testcommittee = Committee.objects.get(committeeName="TestCommittee4")
        data = {
            "eventDescription": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's",
            "eventSummary": "Lorem Ipsum is simply dummy text of the ",
            "eventName": "TestEvent101",
            "eventDate": "2020-12-12",
            "eventTime": "6pm",
            "eventSeatingCapacity": 31,
            "eventVenue": "6Th Fllor",
            "registrationLink": "https://www.lifewire.com/",
            "organisingCommittee": testcommittee.id,
        }
        response = self.client.post("/api/events/new/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class GetTestCase(APITestCase):
    def setUp(self):
        Committee.objects.create(
            committeeName="TestCommittee4",
            committeeDescription="A Student Chapter Helping Students to Make Web Apps and Mobile Apps",
            committeeDept="Computer Engineering",
            committeeChairperson="TestPerson",
        )

    def test_create_event(self):
        testcommittee = Committee.objects.get(committeeName="TestCommittee4")
        data = {
            "eventDescription": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's",
            "eventSummary": "Lorem Ipsum is simply dummy text of the ",
            "eventName": "TestEvent101",
            "eventDate": "2020-12-12",
            "eventTime": "6pm",
            "eventSeatingCapacity": 31,
            "eventVenue": "6Th Fllor",
            "registrationLink": "https://www.lifewire.com/",
            "organisingCommittee": testcommittee.id,
        }
        response = self.client.post("/api/events/new/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class EventCommitteeList(APITestCase):
    def test_list_event(self):
        response = self.client.get("/api/events/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_committee(self):
        response = self.client.get("/api/committees/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
