from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base, int_pk

if TYPE_CHECKING:
    from db.models.static.zone import Zone


class Encounter(Base):
    __tablename__ = "encounter"

    id: Mapped[int_pk]
    name: Mapped[str]

    zone_id: Mapped[int] = mapped_column(ForeignKey("zone.id"))
    zone: Mapped["Zone"] = relationship()
