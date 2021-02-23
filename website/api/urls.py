from django.urls import path
from api import views
from django.conf.urls import include


urlpatterns = [
    # committees
    path("committees/", views.CommitteeList.as_view(), name="committees_list"),
    path(
        "committees/new/",
        views.CommitteeCreate.as_view(),
        name="committee_create",
    ),
    path(
        "committees/<int:pk>/",
        views.CommitteeDetail.as_view(),
        name="committee_detail",
    ),
    path(
        "committeescrud/<int:pk>/",
        views.CommitteeCrud.as_view(),
        name="committee_crud",
    ),
    # events
    path("events/", views.EventsList.as_view(), name="events_list"),
    path("events/new/", views.EventsCreate.as_view(), name="event_create"),
    path("events/<int:pk>/", views.EventDetail.as_view(), name="event_detail"),
    path("eventscrud/<int:pk>/", views.EventCrud.as_view(), name="event_crud"),
    path("eventfinder/<int:pk>/", views.EventFinder, name="event_finder")
]
