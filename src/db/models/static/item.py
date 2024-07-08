from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base, int_pk
from db.models.actor import ActorItem

if TYPE_CHECKING:
    from db.models.actor import Actor


class ItemSet(Base):
    __tablename__ = "item_set"

    id: Mapped[int_pk]
    name: Mapped[str]

    items: Mapped[list["Item"]] = relationship(back_populates="item_set")


class Item(Base):
    __tablename__ = "item"

    id: Mapped[int_pk]
    icon: Mapped[str]
    name: Mapped[str]

    item_set_id: Mapped[int] = mapped_column(ForeignKey("item_set.id"))
    item_set: Mapped["ItemSet"] = relationship(back_populates="items")

    actors: Mapped[list["Actor"]] = relationship(
        secondary=ActorItem.__table__,
        back_populates="items",
    )
