from rest_framework import serializers
from ..models import Device


class DeviceSerializer(serializers.ModelSerializer):
    queryset = Device.objects.all()
    device = serializers.CharField(source='name.name')
    apparatus = serializers.CharField(source='apparatus.name')

    class Meta:
        model = Device
        exclude = ['name']
