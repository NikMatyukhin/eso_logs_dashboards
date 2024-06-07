from typing import TYPE_CHECKING
from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base, uuid_pk

if TYPE_CHECKING:
    from db.models.static import Encounter, Difficulty
    from db.models.report import Report


class Fight(Base):
    __tablename__ = "fight"

    id: Mapped[uuid_pk]
    name: Mapped[str]
    start_time: Mapped[date]
    end_time: Mapped[date]

    average_item_level: Mapped[float]
    boss_percentage: Mapped[float | None]

    report_code: Mapped[str] = mapped_column(ForeignKey("report.code"))
    report: Mapped["Report"] = relationship(back_populates="fights")

    encounter_id: Mapped[int | None] = mapped_column(ForeignKey("encounter.id"))
    encounter: Mapped["Encounter | None"] = relationship()

    difficulty_id: Mapped[int | None] = mapped_column(ForeignKey("difficulty.id"))
    difficulty: Mapped["Difficulty | None"] = relationship()
