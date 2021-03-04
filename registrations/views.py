from django.shortcuts import render, redirect
from .models import *
from .forms import *

def get_current_km():
  Ture_obj = Ture.objects.latest('id')
  current_km = Ture_obj.km_count
  return current_km


def create_tur(request):
  if request.method == "POST":
    form = TurForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
  form = TurForm(initial={'km_count': get_current_km(), 'user': request.user.id})
  context = {'form': form}
  return render(request, 'registrations/create_tur.html', context)


def create_tankning(request):
  if request.method == "POST":
    form = TankningForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
  form = TankningForm(initial={'user': request.user.id})
  context = {'form': form}
  return render(request, 'registrations/create_tankning.html', context)


def create_udgift(request):
  if request.method == "POST":
    form = UdgiftForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
  form = UdgiftForm(initial={'user': request.user.id})
  context = {'form': form}
  return render(request, 'registrations/create_tankning.html', context)


def create_indbetaling(request):
  if request.method == "POST":
    form = IndbetalingForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
  form = IndbetalingForm(initial={'user': request.user.id})
  context = {'form': form}
  return render(request, 'registrations/create_indbetaling.html', context)
