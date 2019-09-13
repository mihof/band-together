from django.urls import include, path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup', views.signup.as_views(), name='signup'),
  path('accounts/signup/customer/', views.CustomerSignUp.as_views(), name='customer_signup'),
  path('accounts/signup/manager/', views.ManagerSignUp.as_views(), name='manager_signup'),
]