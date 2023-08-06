from abc import ABC, abstractmethod

from taskimporter.models.task import Task


class TaskManager(ABC):
    name: str

    @staticmethod
    @abstractmethod
    async def add_task(task: Task, project: str) -> None:
        pass

    @staticmethod
    @abstractmethod
    async def mark_done(task: Task, project: str) -> None:
        pass