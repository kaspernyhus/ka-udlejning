from django.urls import path
from . import views

urlpatterns = [
  path('tur', views.create_tur, name='create_tur'),
  path('tankning', views.create_tankning, name='create_tankning'),
  path('udgift', views.create_udgift, name='create_udgift'),
  path('indbetaling', views.create_indbetaling, name='create_indbetaling'),
  ]