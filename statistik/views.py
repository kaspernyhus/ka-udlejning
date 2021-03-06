from registrations.models import Tankning, Tur, Udgift
from django.shortcuts import render
from django.contrib.auth.models import User


def show_stats(request):
  # Total km
  first_entry = Tur.objects.first()
  latest_entry = Tur.objects.latest('id')
  total_km = latest_entry.odometer - first_entry.odometer
  # Benzin price pr. km
  tankninger = Tankning.objects.all()
  tankning_total = 0
  for tankning in tankninger:
    tankning_total += tankning.amount
  gas_price_pr_km = tankning_total / total_km
  # Udgifter
  udgifter = Udgift.objects.all()
  udgifter_total = 0
  for udgift in udgifter:
    udgifter_total += udgift.amount
  # Total price pr km
  total_expenses = tankning_total + udgifter_total
  price_pr_km = total_expenses / total_km
  # User usage
  users = User.objects.all()
  user_usages = []
  for user in users:
    user_ture = Tur.objects.filter(user=user)
    user_km_total = 0
    for tur in user_ture:
      try:
        user_km_total += tur.delta_km
      except:
        pass
    user_usage = (user_km_total / total_km) * 100 
    user_usages.append({'user': user, 'user_km': user_km_total, 'usage': round(user_usage,2)})
  
  context = {'total_km': total_km, 'benzinpris_pr_km': gas_price_pr_km, 'total_expenses': udgifter_total, 'pris_pr_km': price_pr_km, 'user_usage': user_usages[1:]}
  return render(request, 'statistik/stats.html', context)