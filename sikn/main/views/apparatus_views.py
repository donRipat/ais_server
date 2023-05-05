from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from ..serializers.apparatus_serializers import ApparatusesListSerializer
from ..services.apparatus_service import ApparatusService


class GetApparatusesListAPIView(GenericAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ApparatusesListSerializer

    def get(self, request: Request) -> Response:
        """Getting apparatuses list"""
        response = ApparatusService.get_apparatuses_list()
        print(response)
        return Response(data=response.data, status=status.HTTP_200_OK)


class SetApparatusStatusAPIView(GenericAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = ApparatusesListSerializer

    def get(self, request: Request, _a: int, _s: int) -> Response:
        """Updating apparatus' status"""
        response = ApparatusService.update_apparatus_status(_a, _s)
        return Response(data=response.data, status=status.HTTP_200_OK)
