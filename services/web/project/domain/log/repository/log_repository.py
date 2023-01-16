from abc import ABC

from project.domain.log.log import Log


class ITLogRepository(ABC):
    def getAll(self) -> None:
        ...
    def get(self, log_id: int) -> Log:
        ...

    def create(self, log: Log) -> Log:
        ...