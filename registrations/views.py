from django.shortcuts import render, redirect
from .models import *
from .forms import *
from users.user_data import get_user_km_price


def get_current_km():
  Ture_obj = Tur.objects.latest('id')
  current_km = Ture_obj.odometer
  return current_km


def create_tur(request):
  if request.method == "POST":
    form = TurForm(request.user, request.POST)
    if form.is_valid():
      form_data = form.cleaned_data
      previous_odometer = get_current_km()
      if form_data['odometer'] > previous_odometer: # a valid entry
        data_to_save = form.save(commit=False)
        # if entry from non staff member
        if 'user' not in form_data:
          data_to_save.user = request.user
          user = request.user
        # else user is selectable in form
        else:
          user = form_data['user']
        # calculate distance and price to show
        delta_km = form_data['odometer'] - previous_odometer
        price = delta_km * get_user_km_price(request.user)
        data_to_save.delta_km = delta_km
        data_to_save.tur_price = price
        data_to_save.save()
        if user.id == 6:  # GoMore
          return redirect('/registrer/gomore')
        else:
          return render(request, 'registrations/confirm_tur.html', context={'user': user, 'km': delta_km, 'tur_pris': price})
      else: # not a valid entry -> error
        return render(request, 'registrations/form_error.html', {'error': 'Nuværende kilometertælleraflæsning skal være højere end den seneste!'})
  form = TurForm(request.user, initial={'odometer': get_current_km(), 'user': request.user.id})
  context = {'form': form, 'km_rate': get_user_km_price(request.user)}
  return render(request, 'registrations/create_tur.html', context)


def create_tankning(request):
  if request.method == "POST":
    form = TankningForm(request.user, request.POST)
    if form.is_valid():
      form_data = form.cleaned_data
      data_to_save = form.save(commit=False)
      if 'user' not in form_data:
        data_to_save.user = request.user
        user = request.user
      # else user is selectable in form
      else:
        user = form_data['user']
      data_to_save.save()
      return render(request, 'registrations/confirm_tankning.html', {'user': user, 'pris': form.cleaned_data['amount']})
  form = TankningForm(request.user, initial={'user': request.user.id})
  context = {'form': form}
  return render(request, 'registrations/create_tankning.html', context)


def create_udgift(request):
  if request.method == "POST":
    form = UdgiftForm(request.user, request.POST)
    if form.is_valid():
      form_data = form.cleaned_data
      data_to_save = form.save(commit=False)
      if 'user' not in form_data:
        data_to_save.user = request.user
        user = request.user
      # else user is selectable in form
      else:
        user = form_data['user']
      data_to_save.save()
      return render(request, 'registrations/confirm_udgift.html', 
      {
        'user': user, 
        'description': form.cleaned_data['description'], 
        'pris': form.cleaned_data['amount']
      })
  form = UdgiftForm(request.user, initial={'user': request.user.id})
  context = {'form': form}
  return render(request, 'registrations/create_udgift.html', context)


def create_indbetaling(request):
  if request.method == "POST":
    form = IndbetalingForm(request.user, request.POST)
    if form.is_valid():
      form_data = form.cleaned_data
      data_to_save = form.save(commit=False)
      if 'user' not in form_data:
        data_to_save.user = request.user
        user = request.user
      # else user is selectable in form
      else:
        user = form_data['user']
      data_to_save.save()
      return render(request, 'registrations/confirm_indbetaling.html', 
        {
          'date': form.cleaned_data['date'],
          'user': user,  
          'amount': form.cleaned_data['amount']
        })
  form = IndbetalingForm(request.user, initial={'user': request.user.id})
  context = {'form': form}
  return render(request, 'registrations/create_indbetaling.html', context)


def register_gomore_use(request):
  if request.method == "POST":
    form = GomoreForm(request.POST)
    if form.is_valid():
      form_data = form.cleaned_data
      data_to_save = form.save(commit=False)
      data_to_save.user = User.objects.get(id=6) # GoMore user
      data_to_save.save()
      tur_obj = Tur.objects.latest('id')
      context = {'km': tur_obj.delta_km, 'amount': form_data['amount']}
      return render(request, 'registrations/confirm_gomore.html', context)
  gomore_form = GomoreForm()
  context = {'form': gomore_form}
  return render(request, 'registrations/gomore.html', context)
