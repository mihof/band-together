from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Customer, Manager

class CustomerSignUpForm(UserCreationForm):
  class Meta(UserCreationForm.Meta):
    model = CustomUser

  def save(self, commit=True):
    user = super().save(commit=False)
    user.is_customer = True
    if commit:
      user.save()
    return user

class ManagerSignUpForm(UserCreationForm):
  class Meta(UserCreationForm.Meta):
    model = CustomUser

  def save(self, commit=True):
    user = super().save(commit=False)
    user.is_manager = True
    if commit:
      user.save()
    return user
