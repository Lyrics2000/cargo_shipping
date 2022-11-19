
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class vehicleCategory(BaseModel):
    category_name = models.CharField(max_length = 255)
    location = models.CharField(max_length = 255,blank = True,null = True)
    lat = models.DecimalField(max_digits=20,decimal_places=10,default=0.00)
    lon = models.DecimalField(max_digits=20,decimal_places=10,default=0.00)



    def __str__(self) -> str:
        return self.category_name


class Cargo(BaseModel):
    user =  models.ForeignKey(User,on_delete = models.CASCADE)
    vehicle_type = models.ForeignKey(vehicleCategory,on_delete = models.CASCADE)
    phone_number = models.CharField(max_length = 255)
    pick_up = models.CharField(max_length = 255)
    cargo_name = models.CharField(max_length = 255,blank =True,null = True)
    desitnation = models.CharField(max_length = 255)
    arrived =  models.BooleanField(default= False)
    accepted = models.BooleanField(default=False)
    location_description = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits=20, decimal_places=2)


    def __str__(self) -> str:
        return self.cargo_name


class TrackCargo(BaseModel):
    cargos = models.ForeignKey(Cargo,on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.cargos)


class CurrentLocation(BaseModel):
    user =  models.ForeignKey(User,on_delete = models.CASCADE)
    lat = models.DecimalField(max_digits=20,decimal_places=10)
    lon = models.DecimalField(max_digits=20,decimal_places=10)

    def __str__(self) -> str:
        return str(self.user)



