from django.contrib import admin
from .models import vehicleCategory,Cargo,TrackCargo
# Register your models here.

admin.site.register(vehicleCategory)
admin.site.register(Cargo)
admin.site.register(TrackCargo)
