from registrations.models import *


def get_user_data(user):
  ##################################
  #             TURE               #
  ##################################
  # calculate total user km
  ture = Tur.objects.all().filter(user=user)
  user_km = 0
  user_km_cost = 0

  for tur in ture:
    user_km = user_km + tur.delta_km
    user_km_cost = user_km_cost + tur.tur_price


  # km = [tur.odometer for tur in ture]       # km counter registrations
  # users = [tur.user.id for tur in ture[1:]] # by user (omit first entry)
  # # calculate difference between km registrations = km's travelled
  # delta_km = [km[n]-km[n-1] for n in range(1,len(km))]
  
  # # Calculate total user km
  # user_km = 0
  # for i in range(len(users)):
  #   if users[i] == user.id:
  #     user_km = user_km + delta_km[i]

  # # Calculate total km cost
  # user_km_cost = 0
  # for i in range(len(users)):
  #   if users[i] == user.id:
  #     user_km_cost = user_km_cost + delta_km[i]*ture[i+1].km_rate # count from index 1

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
  #             INDSKUD            #
  ##################################
  indskuds = Indskud.objects.filter(user=user)
  user_indskud = 0
  for indskud in indskuds:
    user_indskud = user_indskud + indskud.amount

  ##################################
  #           UDBETALING           #
  ##################################
  udbetalinger = Udbetaling.objects.filter(user=user)
  user_udbetalinger = 0
  for udbetaling in udbetalinger:
    user_udbetalinger = user_udbetalinger + udbetaling.amount

  ##################################
  #             BALANCE            #
  ##################################
  user_balance = user_indbetaling + user_udgift_cost + user_tankning_cost - user_km_cost - user_udbetalinger

  print('----------' + str(user) + '-----------')
  print('km         ', -user_km_cost)
  print('Tankning   ', user_tankning_cost)
  print('Udgift     ', user_udgift_cost)
  print('Indbetaling', user_indbetaling)
  print('Indskud    ', user_indskud)
  print('Udbetaling ', user_udbetalinger)
  print('...............................')
  print('Balance    ', user_balance)

  return {'user': user, 'user_km': user_km, 'balance': user_balance}


def get_bank_account_balance():
  indbetalinger = Indbetaling.objects.all()
  indskuds = Indskud.objects.all()
  udbetalinger = Udbetaling.objects.all()
  bank_account_bal = 0
  for indbetaling in indbetalinger:
    bank_account_bal = bank_account_bal + indbetaling.amount
  for indskud in indskuds:
    bank_account_bal = bank_account_bal + indskud.amount
  for udbetaling in udbetalinger:
    bank_account_bal = bank_account_bal - udbetaling.amount
  return bank_account_bal
