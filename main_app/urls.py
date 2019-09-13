from django.urls import include, path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup', views.signup, name='signup'),
  path('events/', views.EventList.as_view(), name='events'),
]