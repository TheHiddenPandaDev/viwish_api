from dataclasses import dataclass

from project import db
from project.domain.log.repository.log_repository import ITLogRepository
from project.domain.log.log import Log


@dataclass
class LogRepository(ITLogRepository):
    def getAll(self) -> list[Log]:
        return Log.query.all()
    def get(self, log_id: int) -> Log:
        print('LOG ID: '+log_id)
        return Log.query.get(log_id)

    def create(self, log: Log) -> Log:
        db.session.add(log)
        db.session.commit()
        return log