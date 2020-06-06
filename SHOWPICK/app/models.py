from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    si = models.TextField()
    gu = models.TextField()
    dong = models.TextField()

class Store(models.Model):
    big_category = models.TextField()
    small_category = models.TextField()
    title = models.TextField()

class Custom_user(models.Model):
    real_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'custom_user')
    gender = models.TextField()
    age = models.TextField()
    location_gu = models.TextField()
    location_dong = models.TextField()
    email = models.TextField()

class Vote(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "vote")
    image = models.TextField(null = True)
    big_category = models.TextField(null = True)
    small_category= models.TextField(null = True)
    location_dong = models.TextField(null = True)
    title = models.TextField(null = True)

class ConventionVote(models.Model):
    big_category = models.TextField(null = True)
    small_category = models.TextField(null = True)
    location_dong = models.TextField(null = True)
    title = models.TextField(null = True)
    vote_count = models.IntegerField()

class Temporary_Big_Category(models.Model):
    category = models.TextField()

class Temporary_Small_Category(models.Model):
    category = models.TextField()

