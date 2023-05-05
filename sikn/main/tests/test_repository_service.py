from typing import Optional

from .models.py import Parameters


class AccessLevelService:
    """Класс, содержащий CRUD операции AccessLevel model"""

    @staticmethod
    def create_access_level(_level: int, _name: str) -> None:
        access_level = AccessLevel.objects.create(
            name=_name
        )
        access_level.save()