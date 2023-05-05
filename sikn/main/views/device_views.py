from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from ..serializers.device_serializers import DeviceSerializer
from ..services.device_service import DeviceService


class GetDevicesListAPIView(GenericAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = DeviceSerializer

    def get(self, request: Request, _a: int) -> Response:
        """Getting devices list"""
        response = DeviceService.get_devices_list(_a)
        return Response(data=response.data, status=status.HTTP_200_OK)
