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

class Question(models.Model):
  name = models.CharField(max_length=200)
  date = models.DateTimeField()

  def __str__(self):
    return self.name 

class Question_brand(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name 

class Choice(models.Model):
  name = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  q = models.ForeignKey(Question, on_delete=models.CASCADE)

  def __str__(self):
    return self.name 

class Custom_user(models.Model):
    real_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'custom_user')
    gender = models.TextField()
    age = models.TextField()
    location_gu = models.TextField()
    location_dong = models.TextField()
    email = models.TextField()

    def __str__(self):
        return self.name 
