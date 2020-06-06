from django.db import models

# Create your models here.

class Location(models.Model):
    si = models.TextField()
    gu = models.TextField()
    dong = models.TextField()
    