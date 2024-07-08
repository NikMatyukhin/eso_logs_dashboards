from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from db import Base, int_pk

if TYPE_CHECKING:
    from db.models.fight import Fight
    from db.models.static import Encounter


class Difficulty(Base):
    __tablename__ = "difficulty"

    id: Mapped[int_pk]
    name: Mapped[str]

    encounters: Mapped[list["Encounter"]] = relationship(
        back_populates="vhm_difficulty"
    )

    fights: Mapped[list["Fight"]] = relationship(back_populates="difficulty")
