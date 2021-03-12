from django.urls import path
from api import views
from django.conf.urls import include


urlpatterns = [
    # committees
    path("committees/", views.CommitteeList.as_view(), name="committees_list"),
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
    # event like dislike
    path(
        "event_like/<int:pk1>/<int:pk2>/",
        views.event_like,
        name="event_like",
    ),
    path(
        "event_dislike/<int:pk1>/<int:pk2>/",
        views.event_dislike,
        name="event_dislike",
    ),
    # tasks
    path(
        "coretasklist/<int:pk1>/<int:pk2>/",
        views.core_task_list,
        name="core_task_list",
    ),
    path(
        "coretaskcreate/<int:pk1>/<int:pk2>/",
        views.core_task_create,
        name="core_task_create",
    ),
    path(
        "core_task_crud/<int:pk1>/<int:pk2>/",
        views.core_task_crud,
        name="core_task_crud",
    ),
    path(
        "cotasklist/<int:pk1>/<int:pk2>/",
        views.co_task_list,
        name="co_task_list",
    ),
    # login
    path("student_login/", views.student_login, name="student_login"),
    path("committee_login/", views.committee_login, name="committee_login"),
    # Registration
    path(
        "student_registration/",
        views.student_registration,
        name="student_registration",
    ),
    # password change
    path(
        "change_password/",
        views.ChangePasswordView.as_view(),
        name="change_password",
    ),

    #Core Committee and Co Committee crud operations
    #------------------------------------------------------------------------------------
    path(
        "upgrade_to_core/<int:pk>/<str:position>/",
        views.upgradeToCoreCom,
        name="uprgade-to-core",
    ),

    path(
    "upgrade_to_co/<int:pk>/<str:position>/",
    views.upgradeToCoCom,
    name="uprgade-to-co",
    ),

    path(
    "get_core_committee_members/",
    views.listCoreCommittee,
    name="list-of-core-committee-members",
    ),

    path(
    "get_co_committee_members/",
    views.listCoCommittee,
    name="list-of-co-committee-members",
    ),

    path(
    "delete_core_committee_member/<int:pk>/",
    views.deleteCoreCommittee,
    name="delete-core-committee-members",
    ),

    path(
    "delete_co_committee_member/<int:pk>/",
    views.deleteCoCommittee,
    name="delete-co-committee-members",
    ),
    #------------------------------------------------------------------------------------
        
    path("students/", views.studentList, name="student_list"),

]
