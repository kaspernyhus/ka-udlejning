from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .data import *
from django.contrib.auth import get_user_model
from itertools import chain
import operator


@login_required(login_url='login')
def oversigt(request):
  if request.user.is_staff:
    User = get_user_model()
    users = User.objects.all()
    users_data = [get_user_data(user) for user in users]
    context = {'users': users_data[1:], 'bank_account_balance': get_bank_account_balance()} # remove admin user
    return render(request, 'oversigter/admin_oversigt.html', context)
  else:
    user_data = get_user_data(request.user)
    context = {'user': request.user, 'user_data': user_data}
    return render(request, 'oversigter/user_oversigt.html', context)


@login_required(login_url='login')
def all_transactions(request):
  ture = Tur.objects.all()
  tankninger = Tankning.objects.all()
  indbetalinger = Indbetaling.objects.all()
  udgifter = Udgift.objects.all()
  indbetalinger = Indbetaling.objects.all()
  indskud = Indskud.objects.all()
  udbetalinger = Udbetaling.objects.all()
  all_transactions = list(chain(ture, tankninger, udgifter, indbetalinger, indskud, udbetalinger))
  all_transactions = sorted(all_transactions[1:], key=operator.attrgetter('date')) # remove initial odometer entry
  context = {'all_transactions': all_transactions}
  return render(request, 'oversigter/all_transactions.html', context)


@login_required(login_url='login')
def user_transactions(request, id):
  # Get all transaction data
  ture = Tur.objects.all().filter(user=id)
  tankninger = Tankning.objects.all().filter(user=id)
  udgifter = Udgift.objects.all().filter(user=id)
  indbetalinger = Indbetaling.objects.all().filter(user=id)
  indskud = Indskud.objects.all().filter(user=id)
  udbetalinger = Udbetaling.objects.all().filter(user=id)
  all_transactions = list(chain(ture, tankninger, udgifter, indbetalinger, indskud, udbetalinger))
  all_transactions = sorted(all_transactions, key=operator.attrgetter('date'))
  # Calculate saldo
  user_saldo = [0]
  for i, transaction in enumerate(all_transactions):
    if transaction.__class__.__name__ == 'Tur':
      user_saldo.append(user_saldo[i]-transaction.tur_price)
    elif transaction.__class__.__name__ == 'Tankning':
      user_saldo.append(user_saldo[i]+transaction.amount)
    elif transaction.__class__.__name__ == 'Udgift':
      user_saldo.append(user_saldo[i]+transaction.amount)
    elif transaction.__class__.__name__ == 'Indbetaling':
      user_saldo.append(user_saldo[i]+transaction.amount)
    elif transaction.__class__.__name__ == 'Indskud':
      user_saldo.append(user_saldo[i])
    elif transaction.__class__.__name__ == 'Udbetaling':
      user_saldo.append(user_saldo[i]-transaction.amount)
  all_transactions = list(zip(all_transactions, user_saldo[1:]))
  context = {'all_transactions': all_transactions}
  return render(request, 'oversigter/user_transactions.html', context)



def bank_account_oversigt(request):
  indbetalinger = Indbetaling.objects.all()
  indskud = Indskud.objects.all()
  udbetalinger = Udbetaling.objects.all()
  all_transactions = list(chain(indbetalinger, indskud, udbetalinger))
  all_transactions = sorted(all_transactions, key=operator.attrgetter('date'))
  # Calculate saldo
  bank_saldo = [0]
  for i, transaction in enumerate(all_transactions):
    if transaction.__class__.__name__ == 'Indbetaling':
      bank_saldo.append(bank_saldo[i]+transaction.amount)
    elif transaction.__class__.__name__ == 'Indskud':
      bank_saldo.append(bank_saldo[i]+transaction.amount)
    elif transaction.__class__.__name__ == 'Udbetaling':
      bank_saldo.append(bank_saldo[i]-transaction.amount)
  all_transactions = list(zip(all_transactions, bank_saldo[1:]))
  context = {'all_transactions': all_transactions}
  return render(request, 'oversigter/bank_account.html', context)