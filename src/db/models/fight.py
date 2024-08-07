from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base, uuid_pk

if TYPE_CHECKING:
    from db.models.report import Report
    from db.models.static import Difficulty, Encounter


class Fight(Base):
    __tablename__ = "fight"

    id: Mapped[uuid_pk]
    name: Mapped[str]
    start_time: Mapped[datetime]
    end_time: Mapped[datetime]
    average_item_level: Mapped[float]
    boss_percentage: Mapped[float | None]

    report_id: Mapped[int] = mapped_column(ForeignKey("report.id"))
    report: Mapped["Report"] = relationship(back_populates="fights")

    encounter_id: Mapped[int | None] = mapped_column(ForeignKey("encounter.id"))
    encounter: Mapped["Encounter | None"] = relationship(back_populates="fights")

    difficulty_id: Mapped[int | None] = mapped_column(ForeignKey("difficulty.id"))
    difficulty: Mapped["Difficulty | None"] = relationship(back_populates="fights")
