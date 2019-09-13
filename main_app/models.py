from django.db import models
from django.contrib.auth.models import AbstractUser
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

  def __str__(self):
    return self.name

class Event(models.Model):
  genre = models.CharField(max_length=100)
  artists = models.CharField(max_length=100)
  description = models.TextField(max_length=800)
  date = models.DateField('date of show')

  def __str__(self):
    return self.artists

class CustomUser(AbstractUser):
  is_customer = models.BooleanField('customer status', default=False)
  is_manager = models.BooleanField('manager status', default=False)

class Manager(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

class Customer(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

  