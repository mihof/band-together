from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

OPTIONS = (
  ('Y', 'Yes'),
  ('N', 'No')
)

class Venue(models.Model):
  name = models.CharField(max_length=100)
  capacity = models.IntegerField()
  accessibility = models.CharField(
    max_length=1,
    choices=OPTIONS,
    default=OPTIONS[0][0]
  )
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class Event(models.Model):
  genre = models.CharField(max_length=100)
  artists = models.CharField(max_length=100)
  description = models.TextField(max_length=800)
  date = models.DateField('date of show')

  def __str__(self):
    return self.artists