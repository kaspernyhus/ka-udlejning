from registrations.models import Indbetaling, Tankning, Tur, Udgift
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def show_stats(request):
  # Total km
  first_entry = Tur.objects.first()
  latest_entry = Tur.objects.latest('id')
  total_km = latest_entry.odometer - first_entry.odometer
  # GoMore stats
  gomore_ture = Tur.objects.filter(user=6) # GoMore user id = 6
  gomore_km = 0
  for tur in gomore_ture:
    gomore_km += tur.delta_km
  total_km_minus_gomore = total_km - gomore_km
  gomore_indbetalinger = Indbetaling.objects.all().filter(user=6)
  gomore_income = 0
  for indbetaling in gomore_indbetalinger:
     gomore_income += indbetaling.amount
  try:
    gomore_income_pr_km = gomore_income / gomore_km
  except:
    gomore_income_pr_km = 0
  # Benzin price pr. km
  tankninger = Tankning.objects.all()
  tankning_total = 0
  for tankning in tankninger:
    tankning_total += tankning.amount
  try:
    gas_price_pr_km = tankning_total / total_km_minus_gomore
  except:
    gas_price_pr_km = 0
  # Udgifter
  udgifter = Udgift.objects.all()
  udgifter_total = 0
  for udgift in udgifter:
    udgifter_total += udgift.amount
  # Total price pr km
  total_expenses = tankning_total + udgifter_total - gomore_income
  try:
    price_pr_km = total_expenses / total_km
  except:
    price_pr_km = 0
  # User usage
  users = User.objects.all()
  user_usages = []
  for user in users:
    user_ture = Tur.objects.filter(user=user)
    user_km_total = 0
    for tur in user_ture:
      user_km_total += tur.delta_km
    user_usage = (user_km_total / total_km) * 100 
    user_usages.append({'user': user, 'user_km': user_km_total, 'usage': round(user_usage,2)})
  context = {
    'total_km': total_km,
    'benzinpris_pr_km': gas_price_pr_km, 
    'total_expenses': udgifter_total, 
    'pris_pr_km': price_pr_km, 
    'user_usage': user_usages[1:],
    'gomore_km': gomore_km,
    'gomore_income': gomore_income,
    'gomore_income_pr_km': gomore_income_pr_km
    }
  return render(request, 'statistik/stats.html', context)