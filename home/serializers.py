from rest_framework.serializers import ModelSerializer
from .models import vehicleCategory,Cargo

class VehicleSerializers(ModelSerializer):
    class Meta:
        model = vehicleCategory
        fields = "__all__"
        depth = 1


class CargoSerializer(ModelSerializer):
    class Meta:
        model = Cargo
        fields ="__all__"
        depth = 1
