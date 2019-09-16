from django.contrib import admin
from django.contrib.auth import get_user_model
from  .models import Venue, Event, Profile

admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Profile)
# Register your models here.
