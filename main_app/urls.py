from django.urls import include, path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup', views.signup, name='signup'),
  path('events/', views.event_index, name='index'),
  path('events/<int:event_id>/', views.event_detail, name='detail'),
  path('events/create/', views.EventCreate.as_view(), name='create'),
]