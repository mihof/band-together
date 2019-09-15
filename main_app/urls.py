from django.urls import include, path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup', views.signup, name='signup'),
  path('events/', views.event_index, name='index'),
  path('events/<int:event_id>/', views.event_detail, name='detail'),
  path('events/create/', views.EventCreate.as_view(), name='create'),
  path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='update'),
  path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='delete'),
  path('venues/', views.VenueList.as_view(), name='venue_index'),
  path('venues/create/', views.VenueCreate.as_view(), name='venue_create'),
  path('venues/<int:pk>/update/', views.VenueUpdate.as_view(), name='venue_update'),
  path('venues/<int:pk>/delete/', views.VenueDelete.as_view(), name='venue_delete'),
  
]