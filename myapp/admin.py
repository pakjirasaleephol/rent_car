from django.contrib import admin
from .models import Rent, Car, Return

class RentAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Rent._meta.fields]
admin.site.register(Rent,RentAdmin)

class CarAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Car._meta.fields]
admin.site.register(Car,CarAdmin)

class ReturnAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Return._meta.fields]
admin.site.register(Return, ReturnAdmin)