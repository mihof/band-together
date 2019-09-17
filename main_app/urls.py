from django.urls import include, path
from django.contrib.admin.views.decorators import staff_member_required
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup', views.signup, name='signup'),
  path('events/', views.event_index, name='index'),
  path('events/<int:event_id>/', views.event_detail, name='detail'),
  path('events/create/', views.EventCreate.as_view(), name='create'),
  path('events/<int:pk>/update/', staff_member_required(views.EventUpdate.as_view()), name='update'),
  path('events/<int:pk>/delete/', staff_member_required(views.EventDelete.as_view()), name='delete'),
  path('venues/', views.venue_index, name='venue_index'),
  path('venues/create/', staff_member_required(views.VenueCreate.as_view()), name='venue_create'),
  path('venues/<int:pk>/update/', staff_member_required(views.VenueUpdate.as_view()), name='venue_update'),
  path('venues/<int:pk>/delete/', staff_member_required(views.VenueDelete.as_view()), name='venue_delete'),
  
]