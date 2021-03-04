from registrations.models import *


def get_user_data(user):
  ##################################
  #             TURE               #
  ##################################
  # calculate total user km
  ture = Ture.objects.all()
  km = [tur.km_count for tur in ture]       # km counter registrations
  users = [tur.user.id for tur in ture[1:]] # by user (omit first entry)
  # calculate difference between km registrations = km's travelled
  delta_km = [km[n]-km[n-1] for n in range(1,len(km))]
  
  # Calculate total user km
  user_km = 0
  for i in range(len(users)):
    if users[i] == user.id:
      user_km = user_km + delta_km[i]

  # Calculate total km cost
  user_km_cost = 0
  for i in range(len(users)):
    if users[i] == user.id:
      user_km_cost = user_km_cost + delta_km[i]*ture[i+1].km_rate # count from index 1

  ##################################
  #            TANKNING            #
  ##################################
  tankninger = Tankning.objects.filter(user=user)
  user_tankning_cost = 0
  for tankning in tankninger:
    user_tankning_cost = user_tankning_cost + tankning.amount

  ##################################
  #             UDGIFT             #
  ##################################
  udgifter = Udgift.objects.filter(user=user)
  user_udgift_cost = 0
  for udgift in udgifter:
    user_udgift_cost = user_udgift_cost + udgift.amount

  ##################################
  #           INDBETALING          #
  ##################################
  indbetalinger = Indbetaling.objects.filter(user=user)
  user_indbetaling = 0
  for indbetaling in indbetalinger:
    user_indbetaling = user_indbetaling + indbetaling.amount

  ##################################
  #             BALANCE            #
  ##################################
  user_balance = user_indbetaling + user_udgift_cost + user_tankning_cost - user_km_cost

  # print(km)
  # print(delta_km)
  # print(users)
  # print(user_km)
  # print(user_km_cost)
  # print(user_tankning_cost)
  # print(user_udgift_cost)
  # print(user_indbetaling)
  # print(user_balance)

  return {'user': user, 'user_km': user_km, 'balance': user_balance}