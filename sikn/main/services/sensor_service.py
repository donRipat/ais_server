from typing import Optional
import datetime

from ..models import Sensor, Device
from ..serializers.sensor_serializers import SensorSerializer


class SensorService:
    """Класс, содержащий CRUD операции Sensor"""

    @staticmethod
    def create_sensor(_n: str, _d: Device, _p: str, _l: float, _u: float, _c: float, _t: datetime) -> None:
        p = Sensor.objects.create(name=_n, device=_d, parameter=_p, lower=_l, upper=_u, current=_c, time=_t)
        p.save()

    @staticmethod
    def get_sensor(_id: int) -> Optional[Sensor]:
        p = Sensor.objects.filter(id=_id)
        return p

    @staticmethod
    def get_sensors_list(_d: int) -> SensorSerializer:
        p = Sensor.objects.filter(device=_d)
        response = SensorSerializer(p, many=True)
        return response

    @staticmethod
    def update_sensor(_id: int, _n: str, _d: Device, _p: str, _l: float, _u: float, _c: float, _t: datetime) -> None:
        Sensor.objects.filter(id=_id).update(name=_n, device=_d, parameter=_p, lower=_l, upper=_u, current=_c, time=_t)

    @staticmethod
    def update_sensor_reading(_id: int, _c: float) -> SensorSerializer:
        Sensor.objects.filter(id=_id).update(current=_c)
        p = Sensor.objects.filter(id=_id)
        response = SensorSerializer(p, many=True)
        return response

    @staticmethod
    def delete_sensor_by_id(_id: int) -> None:
        Sensor.objects.filter(id=_id).delete()
