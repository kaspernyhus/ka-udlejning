from django.db import models

class KmPrice(models.Model):
  class Meta:
    verbose_name_plural = 'Km-Price'
  price = models.FloatField(default=2.0)
