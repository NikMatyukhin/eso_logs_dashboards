from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from db import Base, int_pk
from db.models.actor import ActorAbility, ActorDeathEvent

if TYPE_CHECKING:
    from db.models.actor import Actor


class Ability(Base):
    __tablename__ = "ability"

    id: Mapped[int_pk]
    name: Mapped[str]
    base_name: Mapped[str]
    icon: Mapped[str]
    _type: Mapped[str]

    dead_actors: Mapped[list["Actor"]] = relationship(
        secondary=ActorDeathEvent.__table__,
        back_populates="death_events",
    )
    actors: Mapped[list["Actor"]] = relationship(
        secondary=ActorAbility.__table__,
        back_populates="abilities",
    )
