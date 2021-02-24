from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

DEPARTMENT_CHOICES = [
    ("CSE", "Computer Science"),
    ("COMPS", "Computer"),
    ("IT", "Information Technology"),
    ("EXTC", "Electronics & Telecommunication"),
    ("MECH", "Mechanical"),
    ("BIO", "Biomedical"),
    ("ELEX", "Electronics"),
    ("CHEM", "Chemical"),
]


class Committee(models.Model):
    # These are the attributes for the committee account...
    committeeName = models.CharField(max_length=100)
    # committeePhoto           = models.ImageField(upload_to = "")
    committeeDescription = models.TextField()
    committeeDept = models.CharField(max_length=100)
    committeeChairperson = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Committee"
        verbose_name_plural = "Committees"

    def __str__(self):
        return self.committeeName
    
    @property
    def events(self):
        return self.events_set.all()

    @property
    def coreCommitteeMembers(self):
        return self.corecommittee_set.all()

    @property
    def facultyMembers(self):
        return self.faculty_set.all()


# ----------------------------------------------------------------------------------------
# User Models
class Students(AbstractUser):
    sap_regex = RegexValidator(
        regex=r"^\+?6?\d{10,12}$", message="SAP ID must be valid"
    )

    # profilePic               = models.ImageField(upload_to = "", blank=True)
    sap = models.CharField(
        validators=[sap_regex],
        max_length=12,
        blank=False,
        null=False,
        default=None,
        unique=True,
    )
    department = models.CharField(
        max_length=5, blank=False, choices=DEPARTMENT_CHOICES
    )

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.username

    @property
    def coCommittees(self):
        return self.cocommittee_set.all()
    
    @property
    def coreCommittees(self):
        return self.corecommittee_set.all()


class CoCommittee(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE)
    positionAssigned = models.CharField(max_length=200)

    class Meta:
        verbose_name = "CoCommittee"
        verbose_name_plural = "CoCommittees"

    def __str__(self):
        return str(self.id)
    
    @property
    def referrals(self):
        return self.cocommitteereferals_set.all()

    @property
    def tasks(self):
        return self.cocommitteetasks_set.all()


class CoreCommittee(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE)
    positionAssigned = models.CharField(max_length=200)

    class Meta:
        verbose_name = "CoreCommittee"
        verbose_name_plural = "CoreCommittees"

    def __str__(self):
        return str(self.id)


class CommitteeToSubscribers(models.Model):
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE)
    subscribers = models.ForeignKey(Students, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "CommitteeToSubscriber"
        verbose_name_plural = "CommitteeToSubscribers"

    def __str__(self):
        return self.committee

class CoCommitteeTasks(models.Model):
    coCommittee = models.ForeignKey(CoCommittee, on_delete=models.CASCADE)
    task = models.TextField()

    class Meta:
        verbose_name = "CoCommitteeTask"
        verbose_name_plural = "CoCommitteeTasks"

    def __str__(self):
        return str(self.coCommittee)+" "+str(self.id)

class Faculty(models.Model):
    name= models.CharField(max_length=200)
    # pic= models.ImageField(upload_to="")
    positionAssigned = models.CharField(max_length=200)
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE)
    department = models.CharField(
        max_length=5, blank=False, choices=DEPARTMENT_CHOICES
    )

    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"

    def __str__(self):
        return self.name

# ----------------------------------------------------------------------------------------


class Events(models.Model):
    # These are the attributes for the events...
    eventDescription = models.TextField()
    eventSummary = models.CharField(max_length=500)
    eventName = models.CharField(max_length=100)
    eventDate = models.DateField()
    eventTime = models.CharField(max_length=15)
    eventSeatingCapacity = models.IntegerField()
    eventVenue = models.TextField()
    # eventBanner               = models.ImageField(upload_to = "")
    # eventPoster               = models.ImageField(upload_to = "")
    registrationLink = models.URLField()
    is_referral = models.BooleanField(default=False)

    # FK to link the organising committee...
    organisingCommittee = models.ForeignKey(
        Committee, on_delete=models.CASCADE
    )

    contactName1=models.CharField(max_length=100,default='dummy user')
    contactName2=models.CharField(max_length=100,blank=True,null=True)
    contactNumber1=models.CharField(max_length=10,default='0000000000')
    contactNumber2=models.CharField(max_length=10,blank=True,null=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.eventName


class EventLikes(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "EventLikes"
        verbose_name_plural = "EventLikes"

    def __str__(self):
        return self.event


class EventImages(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    # pic                      = models.ImageField(upload_to = "")

    class Meta:
        verbose_name = "EventImages"
        verbose_name_plural = "EventImages"

# ----------------------------------------------------------------------------------------

class CoCommitteeReferals(models.Model):
    student = models.CharField(max_length=100,blank=True,null=True)
    coCommittee = models.ForeignKey(CoCommittee, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "CoCommitteeReferal"
        verbose_name_plural = "CoCommitteeReferals"

    def __str__(self):
        return str(self.id)
    

