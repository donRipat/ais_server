from rest_framework import serializers
from ..models import Apparatus, Status, ApparatusName
from .device_serializers import DeviceSerializer
from .sensor_serializers import SensorSerializer


# class ApparatusesListSerializer(serializers.ModelSerializer):
#     apparatus = serializers.CharField(source='name')
#     status = serializers.CharField(source='status.abbreviation')
#
#     class Meta:
#         model = Apparatus
#         exclude = ['name']


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ['id', 'abbreviation', 'meaning']


class ApparatusNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApparatusName
        exclude = []


class ApparatusSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='name.name')
    status = StatusSerializer()
    devices = DeviceSerializer(many=True)

    class Meta:
        model = Apparatus
        fields = ['id', 'name', 'status', 'devices']

