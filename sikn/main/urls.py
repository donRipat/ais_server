from django.contrib import admin
from django.urls import path, re_path, register_converter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views.apparatus_views import *
from .views.device_views import *
from .views.sensor_views import *
from .cringe.path_converter import *

schema_view = get_schema_view(
   openapi.Info(
      title="SIKN",
      default_version='v1',
      description="SIKN API",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

register_converter(FloatUrlParameterConverter, 'float')

urlpatterns = [
   path('apparatuses', GetApparatusesListAPIView.as_view()),
   path('apparatus/<int:_a>', GetApparatusAPIView.as_view()),
   path('apparatus/<int:_a>/status/<int:_s>/', SetApparatusStatusAPIView.as_view()),
   path('devices/<int:_a>', GetDevicesListAPIView.as_view()),
   path('sensors/<int:_d>', GetSensorsListAPIView.as_view()),
   path('sensor/<int:_id>/reading/<float:_c>', UpdateSensorsReadingAPIView.as_view()),
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
