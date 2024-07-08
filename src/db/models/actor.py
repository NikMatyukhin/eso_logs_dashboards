from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base, uuid_pk

if TYPE_CHECKING:
    from db.models.report import Report
    from db.models.static import Ability, Item, Spec


class ActorSpec(Base):
    __tablename__ = "actor_spec"
    __table_args__ = (PrimaryKeyConstraint("actor_id", "spec_name"),)

    actor_id: Mapped[UUID] = mapped_column(ForeignKey("actor.id"))
    spec_name: Mapped[str] = mapped_column(ForeignKey("spec.name"))


class ActorAbility(Base):
    __tablename__ = "actor_ability"
    __table_args__ = (PrimaryKeyConstraint("actor_id", "ability_id"),)

    actor_id: Mapped[UUID] = mapped_column(ForeignKey("actor.id"))
    ability_id: Mapped[int] = mapped_column(ForeignKey("ability.id"))


class ActorItem(Base):
    __tablename__ = "actor_item"
    __table_args__ = (PrimaryKeyConstraint("actor_id", "item_id", "slot"),)

    trait: Mapped[int]
    enchant: Mapped[int]
    slot: Mapped[int]

    actor_id: Mapped[UUID] = mapped_column(ForeignKey("actor.id"))
    item_id: Mapped[int] = mapped_column(ForeignKey("item.id"))


class ActorDeathEvent(Base):
    __tablename__ = "death_event"

    id: Mapped[uuid_pk]
    death_time: Mapped[datetime]

    actor_id: Mapped[UUID] = mapped_column(ForeignKey("actor.id"))
    ability_id: Mapped[int] = mapped_column(ForeignKey("ability.id"))


class Actor(Base):
    __tablename__ = "actor"

    id: Mapped[uuid_pk]
    name: Mapped[str]
    display_name: Mapped[str]
    damage_done: Mapped[int]
    healing_done: Mapped[int]
    _type: Mapped[str]
    sub_type: Mapped[str]

    report_id: Mapped[int] = mapped_column(ForeignKey("report.id"))
    report: Mapped["Report"] = relationship(back_populates="actors")

    specs: Mapped[list["Spec"]] = relationship(
        secondary=ActorSpec.__table__,
        back_populates="actors",
    )
    abilities: Mapped[list["Ability"]] = relationship(
        secondary=ActorAbility.__table__,
        back_populates="actors",
    )
    items: Mapped[list["Item"]] = relationship(
        secondary=ActorItem.__table__,
        back_populates="actors",
    )
    death_events: Mapped[list["Ability"]] = relationship(
        secondary=ActorDeathEvent.__table__,
        back_populates="dead_actors",
    )
