from django.db import models

# Create your models here.

class Location(models.Model):
    si = models.TextField()
    gu = models.TextField()
    dong = models.TextField()

class Store(models.Model):
    big_category = models.TextField()
    small_category = models.TextField()