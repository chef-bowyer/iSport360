from django.db import models

# Create your models here.

class BetaTester(models.Model):
    first_name  = models.CharField(max_length=32)
    last_name   = models.CharField(max_length=32)
    email       = models.EmailField(max_length=254)
    city        = models.CharField(max_length=32)
    state       = models.CharField(max_length=2)
    coach       = models.BooleanField()
    parent      = models.BooleanField()
    soccer      = models.BooleanField()
    baseball    = models.BooleanField()
    softball    = models.BooleanField()
    lacrosse    = models.BooleanField()
    basketball  = models.BooleanField()
    volleyball  = models.BooleanField()
    football    = models.BooleanField()
    golf        = models.BooleanField()
    tennis      = models.BooleanField()
    ice_skating = models.BooleanField()
    swimming    = models.BooleanField()
    gymnastics  = models.BooleanField()
    other       = models.CharField(max_length=32,default="None")

    def __unicode__(self):
        return self.email
