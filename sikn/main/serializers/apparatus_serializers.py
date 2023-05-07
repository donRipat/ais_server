from rest_framework import serializers
from ..models import Apparatus, Status
from .device_serializers import DeviceSerializer
from .sensor_serializers import SensorSerializer


class ApparatusesListSerializer(serializers.ModelSerializer):
    apparatus = serializers.CharField(source='name')
    status = serializers.CharField(source='status.abbreviation')

    class Meta:
        model = Apparatus
        exclude = ['name']


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ['id', 'abbreviation', 'meaning']


class ApparatusSerializer(serializers.ModelSerializer):
    apparatus = serializers.CharField(source='name')
    status = StatusSerializer()
    class Meta:
        model = Apparatus
        exclude = ['name']

