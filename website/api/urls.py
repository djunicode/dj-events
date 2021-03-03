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
    path("eventfinder/<int:pk>/", views.EventFinder, name="event_finder"),
    path(
        "committee_detail/<int:pk>/",
        views.CommitteeExtraDetail,
        name="committee_detail",
    ),
    path(
        "student_profile/<int:pk>/",
        views.StudentProfile,
        name="student_profile",
    ),
    path(
        "referral_table/<int:pk>/", views.ReferralTable, name="referral_table"
    ),
    path(
        "event_like/<eventName>/<username>/",
        views.event_like,
        name="event_like",
    ),
    path(
        "event_delete/<eventName>/<username>/",
        views.event_delete,
        name="event_delete",
    ),
    # tasks
    path("coretasklist/<core>/", views.core_task_list, name="core_task_list"),
    path(
        "coretaskcreate/<core>/",
        views.core_task_create,
        name="core_task_create",
    ),
    path(
        "core_task_crud/<int:pk>/", views.core_task_crud, name="core_task_crud"
    ),
    path("cotasklist/<co>/", views.co_task_list, name="co_task_list"),
    # login
    path("student_login/", views.student_login, name="student_login"),
]
