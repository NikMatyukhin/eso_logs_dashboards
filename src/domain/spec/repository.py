import inject
from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models.static import Spec


class SpecRepository:
    _session: Session = inject.attr(Session)

    def get_by_id(self, spec_id: int) -> Spec:
        query = select(Spec).where(Spec.id == spec_id)
        result = self._session.execute(query)
        return result.scalar_one()

    def get_by_name(self, name: str) -> Spec:
        query = select(Spec).where(Spec.name == name)
        result = self._session.execute(query)
        return result.scalar_one()
