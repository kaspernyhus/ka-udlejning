from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.models import User



class DateInput(forms.DateInput):
    input_type = 'date'


class TurForm(forms.ModelForm):
  def __init__(self, user, *args, **kwargs):
    super(TurForm, self).__init__(*args, **kwargs)
    if not user.is_staff:
      del self.fields['user']

  class Meta:
    model = Tur
    fields = (
      'date', 
      'odometer',
      'user'
    )
    widgets = {
      'date': DateInput(attrs={'class': 'input'}),
      'odometer': forms.NumberInput(attrs={'class': 'input', 'pattern': "\d*"}),
    }
    labels = {
      'date': 'Dato',
      'odometer': 'Kilometertæller',
      'user': 'Bruger'
    }


class TankningForm(forms.ModelForm):
  def __init__(self, user, *args, **kwargs):
    super(TankningForm, self).__init__(*args, **kwargs)
    if not user.is_staff:
      del self.fields['user']
    
  class Meta:
    model = Tankning
    fields = (
      'date',
      'amount',
      'user',
    )
    widgets = {
      'date': DateInput(attrs={'class': 'input'}),
      'amount': forms.NumberInput(attrs={'class': 'input', 'pattern': "\d*"})
    }
    labels = {
      'date': 'Dato',
      'amount': 'Beløb',
      'user': 'Bruger'
    }


class UdgiftForm(forms.ModelForm):
  def __init__(self, user, *args, **kwargs):
    super(UdgiftForm, self).__init__(*args, **kwargs)
    if not user.is_staff:
      del self.fields['user']
  
  class Meta:
    model = Udgift
    fields = (
      'date',
      'amount',
      'description',
      'user',
    )
    widgets = {
      'date': DateInput(attrs={'class': 'input'}),
      'amount': forms.NumberInput(attrs={'class': 'input', 'pattern': "\d*"}),
      'description': forms.Textarea(attrs={'class': 'text-input', 'rows':1, 'cols':30})
    }
    labels = {
      'date': 'Dato',
      'amount': 'Beløb',
      'description': 'Beskrivelse',
      'user': 'Bruger'
    }


class IndbetalingForm(forms.ModelForm):
  def __init__(self, user, *args, **kwargs):
    super(IndbetalingForm, self).__init__(*args, **kwargs)
    if not user.is_staff:
      del self.fields['user']
  
  class Meta:
    model = Indbetaling
    fields = (
      'date',
      'amount',
      'user',
    )
    widgets = {
      'date': DateInput(attrs={'class': 'input'}),
      'amount': forms.NumberInput(attrs={'class': 'input', 'pattern': "\d*"}),
    }
    labels = {
      'date': 'Dato',
      'amount': 'Beløb',
      'user': 'Bruger'
    }


class GomoreForm(forms.ModelForm):
  class Meta:
    model = Indbetaling
    fields = (
      'amount',
    )
    widgets = {
      'amount': forms.NumberInput(attrs={'class': 'input', 'pattern': "\d*"})
    }
    labels = {
      'amount': 'GoMore beløb'
    }