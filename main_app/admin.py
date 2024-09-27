from django.contrib import admin
from django.contrib.auth import get_user_model
from  .models import Venue, Event, Profile, Ticket

admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Profile)
admin.site.register(Ticket)
