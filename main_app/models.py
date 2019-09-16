from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

OPTIONS = (
  ('Y', 'Yes'),
  ('N', 'No')
)

ROLES = (
  ('C', 'Customer'),
  ('M', 'Manager')
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

  def get_absolute_url(self):
    return reverse('detail', kwargs={'event_id': self.id})

  venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  user_role = models.CharField(
    max_length=1,
    choices=ROLES,
    default=ROLES[0][0]
  )
  favorite_color = models.CharField(max_length=50)

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
      Profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

