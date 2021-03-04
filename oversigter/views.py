from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .data import *
from django.contrib.auth import get_user_model


@login_required(login_url='login')
def oversigt(request):
  if request.user.is_staff:
    User = get_user_model()
    users = User.objects.all()
    users_data = [get_user_data(user) for user in users]
    context = {'users': users_data[1:]} # remove admin user
    return render(request, 'oversigter/admin_oversigt.html', context)
  else:
    user_data = get_user_data(request.user)
    context = {'user': request.user, 'user_data': user_data}
    return render(request, 'oversigter/user_oversigt.html', context)