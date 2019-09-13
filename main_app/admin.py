from django.contrib import admin
from django.contrib.auth import get_user_model
from  .models import Venue, Event

admin.site.register(Venue)
admin.site.register(Event)

# Register your models here.
