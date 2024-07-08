from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from db import Base, str_pk
from db.models.actor import ActorSpec

if TYPE_CHECKING:
    from db.models.actor import Actor


class Spec(Base):
    __tablename__ = "spec"

    name: Mapped[str_pk]
    role: Mapped[str]

    actors: Mapped[list["Actor"]] = relationship(
        secondary=ActorSpec.__table__,
        back_populates="specs",
    )
