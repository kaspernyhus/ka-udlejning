from django.contrib import admin
from .models import *

class TurAdmin(admin.ModelAdmin):
  list_display = ('id', 'date', 'user', 'odometer', 'delta_km', 'tur_price')

class TankningAdmin(admin.ModelAdmin):
  list_display = ('id', 'date', 'user', 'amount')

class UdgiftAdmin(admin.ModelAdmin):
  list_display = ('id', 'date', 'user', 'amount', 'description')

class IndbetalingAdmin(admin.ModelAdmin):
  list_display = ('id', 'date', 'user', 'amount')

class IndskudAdmin(admin.ModelAdmin):
  list_display = ('id', 'date', 'user', 'amount', 'description')

class UdbetalingAdmin(admin.ModelAdmin):
  list_display = ('id', 'date', 'user', 'amount', 'description')


admin.site.register(Tur, TurAdmin)
admin.site.register(Tankning, TankningAdmin)
admin.site.register(Udgift, UdgiftAdmin)
admin.site.register(Indbetaling, IndbetalingAdmin)
admin.site.register(Indskud, IndskudAdmin)
admin.site.register(Udbetaling, UdbetalingAdmin)
