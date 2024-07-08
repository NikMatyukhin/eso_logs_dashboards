from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from db import Base, int_pk

if TYPE_CHECKING:
    from db.models.report import Report
    from db.models.static import Encounter


class Zone(Base):
    __tablename__ = "zone"

    id: Mapped[int_pk]
    name: Mapped[str]

    encounters: Mapped[list["Encounter"]] = relationship(back_populates="zone")
    reports: Mapped[list["Report"]] = relationship(back_populates="zone")
