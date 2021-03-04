from django.db import models
from django.conf import settings
from datetime import date


class Ture(models.Model):
  class Meta:
    verbose_name_plural = 'Ture'
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
  date = models.DateField(default=date.today)
  km_count = models.IntegerField(default=0)
  km_rate = models.FloatField(default=2.0)


class Tankning(models.Model):
  class Meta:
    verbose_name_plural = 'Tankninger'
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
  date = models.DateField(default=date.today)
  amount = models.FloatField()


class Indbetaling(models.Model):
  class Meta:
    verbose_name_plural = 'Indbetalinger'
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
  date = models.DateField(default=date.today)
  amount = models.FloatField()
  is_indskud = models.BooleanField(blank=True, default=False)


class Udgift(models.Model):
  class Meta:
    verbose_name_plural = 'Udgifter'
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
  date = models.DateField(default=date.today)
  amount = models.FloatField()
  description = models.CharField(max_length=200)