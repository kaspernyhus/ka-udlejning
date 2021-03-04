from django.db import models
from django.conf import settings
from django.utils import timezone


class Ture(models.Model):
  class Meta:
    verbose_name_plural = 'Ture'
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
  timestamp = models.DateTimeField(default=timezone.now)
  km_count = models.IntegerField(default=0)


class Tankning(models.Model):
  class Meta:
    verbose_name_plural = 'Tankninger'
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
  timestamp = models.DateTimeField(default=timezone.now)
  amount = models.FloatField()


class Betaling(models.Model):
  class Meta:
    verbose_name_plural = 'Betalinger'
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
  timestamp = models.DateTimeField(default=timezone.now)
  amount = models.FloatField()
  is_indskud = models.BooleanField(blank=True)
  description = models.CharField(default=None, max_length=200, blank=True, null=True)


class Udgift(models.Model):
  class Meta:
    verbose_name_plural = 'Udgifter'
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
  timestamp = models.DateTimeField(default=timezone.now)
  amount = models.FloatField()
  description = models.CharField(max_length=200)