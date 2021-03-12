from django.contrib import admin
from django import forms
from .models import (
    Students,
    Committee,
    CoCommittee,
    CoreCommittee,
    CommitteeToSubscribers,
    Events,
    EventLikes,
    Faculty,
    CoCommitteeReferals,
    CoCommitteeTasks,
)
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ("sap",)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(StudentCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomStudentAdmin(UserAdmin):
    add_form = StudentCreationForm
    list_display = (
        "username",
        "email",
        "sap",
        "department",
        "first_name",
        "last_name",
    )
    ordering = ("sap",)

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                    "sap",
                    "department",
                    "is_active",
                ),
            },
        ),
    )

    filter_horizontal = ()


# For Committee Admin
class CommitteeCreationForm(forms.ModelForm):
    class Meta:
        model = Committee
        fields = ("email",)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(StudentCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomCommitteeAdmin(UserAdmin):
    add_form = StudentCreationForm
    list_display = ("committeeName", "email", "committeeDept", "username")
    ordering = ("committeeName",)

    fieldsets = ((None, {"fields": ("username", "email", "password")}),)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password",
                    "committeeName",
                    "committeeDescription",
                    "committeeDept",
                    "committeeChairperson",
                    "is_active",
                ),
            },
        ),
    )

    filter_horizontal = ()


class CoCommitteeAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Student", {"fields": ["student"]}),
        ("Committee", {"fields": ["committee"]}),
        ("Position", {"fields": ["positionAssigned"]}),
    ]
    list_display = (
        "student",
        "committee",
        "positionAssigned",
    )


class CoreCommitteeAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Student", {"fields": ["student"]}),
        ("Committee", {"fields": ["committee"]}),
        ("Position", {"fields": ["positionAssigned"]}),
    ]
    list_display = (
        "student",
        "committee",
        "positionAssigned",
    )


class CommitteeToSubscribersAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Committee", {"fields": ["committee"]}),
        ("Subscribers", {"fields": ["subscribers"]}),
    ]
    list_display = (
        "committee",
        "subscribers",
    )


class EventsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Name", {"fields": ["eventName"]}),
        ("Date", {"fields": ["eventDate"]}),
        ("Time", {"fields": ["eventTime"]}),
        ("Summary", {"fields": ["eventSummary"]}),
        ("Description", {"fields": ["eventDescription"]}),
        ("Organising Committee", {"fields": ["organisingCommittee"]}),
        ("Seating Capacity", {"fields": ["eventSeatingCapacity"]}),
        ("Venue", {"fields": ["eventVenue"]}),
        ("Registration Link", {"fields": ["registrationLink"]}),
        ("Referral", {"fields": ["is_referral"]}),
        ("Contact 1", {"fields": ["contactName1", "contactNumber1"]}),
        ("Contact 2", {"fields": ["contactName2", "contactNumber2"]}),
    ]
    list_display = (
        "id",
        "eventName",
        "eventDate",
        "eventTime",
        "eventVenue",
        "eventSeatingCapacity",
        "organisingCommittee",
        "is_referral",
        "contactName1",
        "contactName2",
        "contactNumber1",
        "contactNumber2",
    )


class EventLikesAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Event", {"fields": ["event"]}),
        ("Student", {"fields": ["student"]}),
    ]
    list_display = (
        "event",
        "student",
    )


class FacultyAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Name", {"fields": ["name"]}),
        ("Position", {"fields": ["positionAssigned"]}),
        ("Committee", {"fields": ["committee"]}),
        ("Department", {"fields": ["department"]}),
    ]
    list_display = (
        "name",
        "positionAssigned",
        "committee",
        "department",
    )


class CoCommitteeReferalsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Student", {"fields": ["participant"]}),
        ("Co Committee", {"fields": ["coCommittee"]}),
        ("Event", {"fields": ["event"]}),
    ]
    list_display = (
        "participant",
        "coCommittee",
        "event",
    )


class CoCommitteeTasksAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Co Committee", {"fields": ["coCommittee"]}),
        ("Task", {"fields": ["task"]}),
        ("Assigned By", {"fields": ["assigned_by"]}),
    ]
    list_display = (
        "id",
        "coCommittee",
        "task",
        "assigned_by",
    )


admin.site.register(Students, CustomStudentAdmin)
admin.site.register(Committee, CustomCommitteeAdmin)
admin.site.register(CoCommittee, CoCommitteeAdmin)
admin.site.register(CoreCommittee, CoreCommitteeAdmin)
admin.site.register(CommitteeToSubscribers, CommitteeToSubscribersAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(EventLikes, EventLikesAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(CoCommitteeReferals, CoCommitteeReferalsAdmin)
admin.site.register(CoCommitteeTasks, CoCommitteeTasksAdmin)
