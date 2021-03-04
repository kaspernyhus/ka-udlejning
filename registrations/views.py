from django.shortcuts import render, redirect
from .models import *
from .forms import *
from users.user_data import get_user_km_price


def get_current_km():
  Ture_obj = Ture.objects.latest('id')
  current_km = Ture_obj.km_count
  return current_km


def create_tur(request):
  if request.method == "POST":
    form = TurForm(request.POST)
    if form.is_valid():
      form_data = form.cleaned_data
      print(form_data['user'])
      previous_km_count = get_current_km()
      if form_data['km_count'] > previous_km_count:
        form.save()
        delta_km = form_data['km_count'] - previous_km_count
        price = delta_km * get_user_km_price(request.user)
        return render(request, 'registrations/confirm_tur.html', context={'user': form_data['user'], 'km': delta_km, 'tur_pris': price})
      else:
        return render(request, 'registrations/form_error.html', {'error': 'Nuværende kilometertælleraflæsning skal være højere end den seneste!'})
  form = TurForm(initial={'km_count': get_current_km(), 'user': request.user.id})
  context = {'form': form}
  return render(request, 'registrations/create_tur.html', context)


def create_tankning(request):
  if request.method == "POST":
    form = TankningForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'registrations/confirm_tankning.html', {'user': form.cleaned_data['user'], 'pris': form.cleaned_data['amount']})
  form = TankningForm(initial={'user': request.user.id})
  context = {'form': form}
  return render(request, 'registrations/create_tankning.html', context)


def create_udgift(request):
  if request.method == "POST":
    form = UdgiftForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'registrations/confirm_udgift.html', 
        {
          'user': form.cleaned_data['user'], 
          'description': form.cleaned_data['description'], 
          'pris': form.cleaned_data['amount']
        })
  form = UdgiftForm(initial={'user': request.user.id})
  context = {'form': form}
  return render(request, 'registrations/create_tankning.html', context)


def create_indbetaling(request):
  if request.method == "POST":
    form = IndbetalingForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'registrations/confirm_indbetaling.html', 
        {
          'date': form.cleaned_data['date'],
          'user': form.cleaned_data['user'],  
          'amount': form.cleaned_data['amount']
        })
  form = IndbetalingForm(initial={'user': request.user.id})
  context = {'form': form}
  return render(request, 'registrations/create_indbetaling.html', context)
