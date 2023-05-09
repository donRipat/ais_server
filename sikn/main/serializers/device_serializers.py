from rest_framework import serializers
from ..models import Device
from .sensor_serializers import SensorSerializer


class DeviceSerializer(serializers.ModelSerializer):
    queryset = Device.objects.all()
    name = serializers.CharField(source='name.name')
    sensors = SensorSerializer(many=True)

    class Meta:
        model = Device
        exclude = ['apparatus']
