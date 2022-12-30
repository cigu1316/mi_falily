from django.db import models

# Create your models here.

class Integrant(models.Model):
    name = models.CharField(max_length=20)
    edge = models.IntegerField()
    major = models.BooleanField()
    