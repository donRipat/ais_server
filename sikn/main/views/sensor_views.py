from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from ..serializers.sensor_serializers import SensorSerializer
from ..services.sensor_service import SensorService


class GetSensorsListAPIView(GenericAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = SensorSerializer

    def get(self, request: Request, _d: int) -> Response:
        """Getting sensors list"""
        response = SensorService.get_sensors_list(_d)
        return Response(data=response.data, status=status.HTTP_200_OK)


class UpdateSensorsReadingAPIView(GenericAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = SensorSerializer

    def post(self, request: Request, _id: int, _c: float) -> Response:
        """Updating sensor's reading"""
        response = SensorService.update_sensor_reading(_id, _c)
        return Response(data=response.data, status=status.HTTP_200_OK)
