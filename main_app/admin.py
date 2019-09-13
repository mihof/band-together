from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from  .models import Venue, Event, Manager, Customer
from .forms import CustomerSignUpForm, ManagerSignUpForm

class ManagerSignUpFormAdmin(UserAdmin):
    add_form = ManagerSignUpForm
    model = Manager
    list_display = ['email', 'username',]

class CustomerSignUpFormAdmin(UserAdmin):
    add_form = CustomerSignUpForm
    model = Customer
    list_display = ['email', 'username',]

admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Manager, ManagerSignUpFormAdmin)
admin.site.register(Customer, CustomerSignUpFormAdmin)
# Register your models here.
