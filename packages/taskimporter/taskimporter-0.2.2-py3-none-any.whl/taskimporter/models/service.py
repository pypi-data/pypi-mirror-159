from typing import List
from abc import ABC, abstractmethod

from taskimporter.models.task import Task


class Service(ABC):
    service_type: str
    name: str
    project_key: str

    @property
    @abstractmethod
    def service_type(self) -> str:
        pass

    @property
    @abstractmethod
    def config_keys(self) -> List[str]:
        pass

    @abstractmethod
    async def get_open_tasks(self) -> List[Task]:
        pass

    @abstractmethod
    async def get_closed_tasks(self) -> List[Task]:
        pass
