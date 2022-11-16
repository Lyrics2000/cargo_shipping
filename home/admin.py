from django.contrib import admin
from .models import vehicleCategory,Cargo,TrackCargo,CurrentLocation
# Register your models here.

admin.site.register(vehicleCategory)
admin.site.register(Cargo)
admin.site.register(TrackCargo)
admin.site.register(CurrentLocation)
