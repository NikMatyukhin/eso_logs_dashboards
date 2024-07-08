from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base, int_pk

if TYPE_CHECKING:
    from db.models.fight import Fight
    from db.models.static import Difficulty, Zone


class Encounter(Base):
    __tablename__ = "encounter"

    id: Mapped[int_pk]
    name: Mapped[str]
    is_final: Mapped[bool]

    zone_id: Mapped[int] = mapped_column(ForeignKey("zone.id"))
    zone: Mapped["Zone"] = relationship(back_populates="encounters")

    vhm_difficulty_id: Mapped[int] = mapped_column(ForeignKey("difficulty.id"))
    vhm_difficulty: Mapped["Difficulty"] = relationship(back_populates="encounters")

    fights: Mapped[list["Fight"]] = relationship(back_populates="encounter")
