from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('login')
    else:
        return render(request, 'partials/_login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def dashboard(request):
  return render(request, 'users/dashboard.html')


