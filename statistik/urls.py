from django.urls import path
from . import views

urlpatterns = [
  path('', views.show_stats, name='show_stats'),
  ]