# from django.contrib import admin
# from .models import (
#     Students,
#     Committee,
#     CoCommittee,
#     CoreCommittee,
#     CommitteeToSubscribers,
#     Events,
#     EventLikes,
# )
# from django.contrib.auth.admin import UserAdmin


# class StudentAdmin(UserAdmin):
#     model = Students
#     list_display = ["username", "sap", "department", "email"]
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {"fields": ("sap", "department")}),
#     )


# class CommitteeAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ("Name", {"fields": ["committeeName"]}),
#         ("Description", {"fields": ["committeeDescription"]}),
#         ("Department", {"fields": ["committeeDept"]}),
#         ("Chairperson", {"fields": ["committeeChairperson"]}),
#     ]
#     list_display = (
#         "id",
#         "committeeName",
#         "committeeDept",
#         "committeeChairperson",
#     )


# class CoCommitteeAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ("Student", {"fields": ["student"]}),
#         ("Committee", {"fields": ["committee"]}),
#         ("Position", {"fields": ["positionAssigned"]}),
#         ("Referrals", {"fields": ["referralCount"]}),
#     ]
#     list_display = (
#         "student",
#         "committee",
#         "positionAssigned",
#         "referralCount",
#     )


# class CoreCommitteeAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ("Student", {"fields": ["student"]}),
#         ("Committee", {"fields": ["committee"]}),
#         ("Position", {"fields": ["positionAssigned"]}),
#     ]
#     list_display = (
#         "student",
#         "committee",
#         "positionAssigned",
#     )


# class CommitteeToSubscribersAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ("Committee", {"fields": ["committee"]}),
#         ("Subscribers", {"fields": ["subscribers"]}),
#     ]
#     list_display = (
#         "committee",
#         "subscribers",
#     )


# class EventsAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ("Name", {"fields": ["eventName"]}),
#         ("Date", {"fields": ["eventDate"]}),
#         ("Time", {"fields": ["eventTime"]}),
#         ("Summary", {"fields": ["eventSummary"]}),
#         ("Description", {"fields": ["eventDescription"]}),
#         ("OrganisingCommittee", {"fields": ["organisingCommittee"]}),
#         ("SeatingCapacity", {"fields": ["eventSeatingCapacity"]}),
#         ("Venue", {"fields": ["eventVenue"]}),
#         ("RegistrationLink", {"fields": ["registrationLink"]}),
#         ("Payable", {"fields": ["is_payable"]}),
#     ]
#     list_display = (
#         "id",
#         "eventName",
#         "eventDate",
#         "eventTime",
#         "eventVenue",
#         "eventSeatingCapacity",
#         "organisingCommittee",
#         "is_payable",
#     )


# class EventLikesAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ("Event", {"fields": ["event"]}),
#         ("Student", {"fields": ["student"]}),
#     ]
#     list_display = (
#         "event",
#         "student",
#     )


# admin.site.register(Students, StudentAdmin)
# admin.site.register(Committee, CommitteeAdmin)
# admin.site.register(CoCommittee, CoCommitteeAdmin)
# admin.site.register(CoreCommittee, CoreCommitteeAdmin)
# admin.site.register(CommitteeToSubscribers, CommitteeToSubscribersAdmin)
# admin.site.register(Events, EventsAdmin)
# admin.site.register(EventLikes, EventLikesAdmin)
