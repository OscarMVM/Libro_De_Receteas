from django.db import models

# Create your models here.
class Client(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def __unicode__(self):
        return self.email
