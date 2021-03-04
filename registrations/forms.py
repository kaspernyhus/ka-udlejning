from django import forms
from django.db.models import fields
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class TurForm(forms.ModelForm):
  class Meta:
    model = Ture
    fields = (
      'date', 
      'km_count', 
      'user',
    )
    widgets = {
      'date': DateInput(attrs={'class': 'input'}),
      'km_count': forms.NumberInput(attrs={'class': 'input', 'pattern': "\d*"})
    }
    labels = {
      'date': 'Dato',
      'km_count': 'Kilometertæller',
      'user': 'Bruger'
    }


class TankningForm(forms.ModelForm):
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
  class Meta:
    model = Indbetaling
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