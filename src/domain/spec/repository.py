from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models.static import Spec


class SpecRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def get_by_name(self, name: str) -> Spec:
        query = select(Spec).where(Spec.name == name)
        result = self._session.execute(query)
        return result.scalar_one()
