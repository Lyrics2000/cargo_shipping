from rest_framework.serializers import ModelSerializer
from .models import vehicleCategory,Cargo,TrackCargo

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


class CargoTrackSerializer(ModelSerializer):
    class Meta:
        model = TrackCargo
        fields = '__all__'
        depth = 1