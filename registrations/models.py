from django.db import models
from django.conf import settings
from datetime import date


class Tur(models.Model):
  class Meta:
    verbose_name_plural = 'Ture'
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
  date = models.DateField(default=date.today)
  odometer = models.IntegerField(default=0)
  delta_km = models.IntegerField(default=0)
  km_rate = models.FloatField(default=2.0)
  tur_price = models.FloatField(default=0.0)


class Tankning(models.Model):
  class Meta:
    verbose_name_plural = 'Tankninger'
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
  date = models.DateField(default=date.today)
  amount = models.FloatField()


class Udgift(models.Model):
  class Meta:
    verbose_name_plural = 'Udgifter'
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
  date = models.DateField(default=date.today)
  amount = models.FloatField()
  description = models.CharField(max_length=200)
  

class Indbetaling(models.Model):
  class Meta:
    verbose_name_plural = 'Indbetalinger'
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
  date = models.DateField(default=date.today)
  amount = models.FloatField()


class Indskud(models.Model):
  class Meta:
    verbose_name_plural = 'Indskud'
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
  date = models.DateField(default=date.today)
  amount = models.FloatField()


class Udbetaling(models.Model):
  class Meta:
    verbose_name_plural = 'Udbetalinger'
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
  date = models.DateField(default=date.today)
  amount = models.FloatField()
  description = models.CharField(max_length=200, blank=True, null=True)
