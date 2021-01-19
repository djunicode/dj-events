from django.urls import path
from .views import test1, test2, test3


urlpatterns = [
    path("test1/", test1, name="test1"),
    path("test2/", test2, name="test2"),
    path("test3/", test3, name="test3"),
]
