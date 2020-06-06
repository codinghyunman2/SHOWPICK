from django.db import models

# Create your models here.
class Question(models.Model):
  name = models.CharField(max_length=200)
  date = models.DateTimeField()

  def __str__(self):
    return self.name 

class Choice(models.Model):
  name = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  q = models.ForeignKey(Question, on_delete=models.CASCADE)

  def __str__(self):
    return self.name 