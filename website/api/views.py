from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(["GET"])
def test1(request):
    test = ["This", "is", "a", "test", 1, 2]
    return Response(status=status.HTTP_200_OK, data={"data": test})


@api_view(["GET"])
def test2(request):
    test = ["This", "is", "a", "test", 1, 2]
    return Response(status=status.HTTP_200_OK, data={"data": test})


@api_view(["GET"])
def test3(request):
    test = ["This", "is", "a", "test", 1, 2]
    return Response(status=status.HTTP_200_OK, data={"data": test})
