from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base, int_pk

if TYPE_CHECKING:
    from db.models.actor import Actor
    from db.models.fight import Fight
    from db.models.static import Region, Zone


class Report(Base):
    __tablename__ = "report"
    __table_args__ = (
        CheckConstraint(r"start_time <= end_time", "start_less_than_end"),
    )

    id: Mapped[int_pk]
    code: Mapped[str]
    title: Mapped[str]
    start_time: Mapped[datetime]
    end_time: Mapped[datetime]
    trial_score: Mapped[int | None]
    trial_time: Mapped[datetime | None]

    region_id: Mapped[int] = mapped_column(ForeignKey("region.id"))
    region: Mapped["Region"] = relationship(back_populates="reports")

    zone_id: Mapped[int] = mapped_column(ForeignKey("zone.id"))
    zone: Mapped["Zone"] = relationship(back_populates="reports")

    actors: Mapped[list["Actor"]] = relationship(back_populates="report")

    fights: Mapped[list["Fight"]] = relationship(back_populates="report")
