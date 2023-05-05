from typing import Optional
from ..models import Device, DeviceName, Apparatus

from ..serializers.device_serializers import DeviceSerializer

class DeviceNameService:
    """Класс, содержащий CRUD операции DeviceName"""

    @staticmethod
    def create_devicename(_n: str) -> None:
        p = DeviceName.objects.create(name=_n)
        p.save()

    @staticmethod
    def get_devicename(_id: int) -> Optional[DeviceName]:
        p = DeviceName.objects.filter(id=_id)
        return p

    @staticmethod
    def update_devicename(_id: int, _name: str) -> None:
        DeviceName.objects.filter(id=_id).update(name=_name)

    @staticmethod
    def delete_devicename_by_id(_id: int) -> None:
        DeviceName.objects.filter(id=_id).delete()


class DeviceService:
    """Класс, содержащий CRUD операции Device"""

    @staticmethod
    def create_device(_a: Apparatus, _n: DeviceName) -> None:
        p = Device.objects.create(apparatus=_a, name=_n)
        p.save()

    @staticmethod
    def get_device(_id: int) -> Optional[Device]:
        p = Device.objects.filter(id=_id)
        return p

    @staticmethod
    def get_devices_list(_a: int) -> DeviceSerializer:
        devices_list = Device.objects.filter(apparatus=_a)
        response = DeviceSerializer(devices_list, many=True)
        return response

    @staticmethod
    def update_device_apparatus(_id: int, _apparatus: Apparatus) -> None:
        Device.objects.filter(id=_id).update(apparatus=_apparatus)

    @staticmethod
    def update_device_name(_id: int, _name: DeviceName) -> None:
        Device.objects.filter(id=_id).update(name=_name)

    @staticmethod
    def delete_device_by_id(_id: int) -> None:
        Device.objects.filter(id=_id).delete()
