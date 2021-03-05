from django.urls import path
from . import views

urlpatterns = [
    path('user', views.oversigt, name='oversigt'),
    path('all_transactions', views.all_transactions, name='all_transactions'),
    path('transactions/<int:id>', views.user_transactions, name='user_transactions'),
    path('bank_account', views.bank_account_oversigt, name='bank_account_oversigt'),
    path('faq', views.faq, name='faq'),
  ]