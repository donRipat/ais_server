from typing import Optional

from ..models import Apparatus, ApparatusName, Status
from ..serializers.apparatus_serializers import *


class ApparatusNameService:
    """Класс, содержащий CRUD операции ApparatusName"""

    @staticmethod
    def create_apparatusname(_name: str) -> None:
        p = ApparatusName.objects.create(name=_name)
        p.save()

    @staticmethod
    def get_apparatusname(_id: int) -> Optional[Apparatus]:
        p = ApparatusName.objects.filter(id=_id)
        return p

    @staticmethod
    def update_apparatusname(_id: int, _name: str) -> None:
        ApparatusName.objects.filter(id=_id).update(name=_name)

    @staticmethod
    def delete_apparatusname_by_id(_id: int) -> None:
        ApparatusName.objects.filter(id=_id).delete()


class StatusService:
    """Класс, содержащий CRUD операции Status"""

    @staticmethod
    def create_status(_name: str) -> None:
        p = Status.objects.create(name=_name)
        p.save()

    @staticmethod
    def get_status(_id: int) -> Optional[Status]:
        p = Status.objects.filter(id=_id).first()
        return p

    @staticmethod
    def update_status_meaning(_id: int, _name: str) -> None:
        Status.objects.filter(id=_id).update(meaning=_name)

    @staticmethod
    def delete_status_by_id(_id: int) -> None:
        Status.objects.filter(id=_id).delete()


class ApparatusService:
    """Класс, содержащий CRUD операции Apparatus"""

    @staticmethod
    def create_apparatus(_status_id: Status, _name: ApparatusName) -> None:
        p = Apparatus.objects.create(id_status=_status_id, name=_name)
        p.save()

    @staticmethod
    def get_apparatus(_id: int) -> ApparatusSerializer:
        p = Apparatus.objects.filter(id=_id)
        response = ApparatusSerializer(p, many=True)
        return response

    @staticmethod
    def get_apparatuses_list() -> ApparatusesListSerializer:
        apparatuses_list = Apparatus.objects.all().order_by('status')
        response = ApparatusesListSerializer(apparatuses_list, many=True)
        return response

    @staticmethod
    def update_apparatus_name(_id: int, _name: ApparatusName) -> None:
        Apparatus.objects.filter(id=_id).update(name=_name)

    @staticmethod
    def update_apparatus_status(_a: int, _s: int) -> ApparatusSerializer:
        a = Apparatus.objects.filter(id=_a)
        new_status = StatusService.get_status(_s)
        a.update(status=new_status)
        response = ApparatusSerializer(a, many=True)
        return response

    @staticmethod
    def delete_apparatus_by_id(_id: int) -> None:
        Apparatus.objects.filter(id=_id).delete()
