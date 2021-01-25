from django.db import models
from django.contrib.auth.models import AbstractUser

class Committee(models.Model):
    # These are the attributes for the committee account...
    committeeName            = models.CharField(max_length = 100)
    # committeePhoto           = models.ImageField(upload_to = "")
    committeeDescription     = models.TextField()
    committeeDept            = models.CharField(max_length = 100)
    committeeChairperson     = models.CharField(max_length = 200)

#----------------------------------------------------------------------------------------
# User Models 
class Students(AbstractUser):
    # profilePic               = models.ImageField(upload_to = "", blank=True)
    sap                      = models.CharField(max_length=11, unique=True)
    department               = models.CharField(max_length=100)

class CoCommittee(models.Model):
    student                  = models.ForeignKey(Students, on_delete=models.CASCADE)
    committee                = models.ForeignKey(Committee, on_delete=models.CASCADE)
    positionAssigned         = models.CharField(max_length=200)
    referralCount            = models.IntegerField(default=0)

class CoreCommittee(models.Model):
    student                  = models.ForeignKey(Students, on_delete=models.CASCADE)
    committee                = models.ForeignKey(Committee, on_delete=models.CASCADE)
    positionAssigned         = models.CharField(max_length=200)
        
class CommitteeToSubscribers(models.Model):
    committee                = models.ForeignKey(Committee, on_delete=models.CASCADE)
    subscribers              = models.ForeignKey(Students, on_delete=models.CASCADE)

#----------------------------------------------------------------------------------------

class Events(models.Model):
    # These are the attributes for the events...
    eventDescription          = models.TextField()
    eventSummary              = models.CharField(max_length=500)
    eventName                 = models.CharField(max_length = 100)
    eventDate                 = models.DateField()
    eventTime                 = models.CharField(max_length=15)
    eventSeatingCapacity      = models.IntegerField()
    eventVenue                = models.TextField()
    #eventBanner               = models.ImageField(upload_to = "")
    registrationLink          = models.URLField()
    is_payable                = models.BooleanField(default = False)

    # FK to link the organising committee...
    organisingCommittee       = models.ForeignKey(Committee, on_delete = models.CASCADE)

class EventLikes(models.Model):
    event                     = models.ForeignKey(Events, on_delete=models.CASCADE)
    student                   = models.ForeignKey(Students, on_delete=models.CASCADE)

class EventImages(models.Model):
    event                    = models.ForeignKey(Events, on_delete=models.CASCADE)
    #pic                      = models.ImageField(upload_to = "")
