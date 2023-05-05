from rest_framework import serializers
from ..models import Sensor


class SensorSerializer(serializers.ModelSerializer):
    queryset = Sensor.objects.all()
    sensor = serializers.CharField(source='name')
    device = serializers.CharField(source='device.name')

    class Meta:
        model = Sensor
        exclude = ['name']
