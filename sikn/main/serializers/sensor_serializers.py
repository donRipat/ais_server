from rest_framework import serializers
from ..models import Sensor


class SensorSerializer(serializers.ModelSerializer):
    queryset = Sensor.objects.all()

    class Meta:
        model = Sensor
        exclude = ['device']
