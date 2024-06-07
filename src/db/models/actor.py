from uuid import UUID
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base, uuid_pk

if TYPE_CHECKING:
    from db.models.static import Spec, Gear, Ability
    from db.models.report import Report


class ActorSpecs(Base):
    __tablename__ = "actor_specs"
    __table_args__ = (PrimaryKeyConstraint("actor_id", "spec_id"),)

    actor_id: Mapped[UUID] = mapped_column(ForeignKey("actor.id"))
    spec_id: Mapped[int] = mapped_column(ForeignKey("spec.id"))


class ActorAbilities(Base):
    __tablename__ = "actor_abilities"
    __table_args__ = (PrimaryKeyConstraint("actor_id", "ability_id"),)

    actor_id: Mapped[UUID] = mapped_column(ForeignKey("actor.id"))
    ability_id: Mapped[int] = mapped_column(ForeignKey("ability.id"))


class ActorGearSets(Base):
    __tablename__ = "actor_gear_sets"
    __table_args__ = (PrimaryKeyConstraint("actor_id", "gear_id"),)

    trait: Mapped[int]
    enchant: Mapped[int]

    actor_id: Mapped[UUID] = mapped_column(ForeignKey("actor.id"))
    gear_id: Mapped[int] = mapped_column(ForeignKey("gear.id"))


class Actor(Base):
    __tablename__ = "actor"

    id: Mapped[uuid_pk]
    name: Mapped[str]
    display_name: Mapped[str]
    damage_done: Mapped[int]
    healing_done: Mapped[int]
    _type: Mapped[str]
    sub_type: Mapped[str]

    report_code: Mapped[str] = mapped_column(ForeignKey("report.code"))
    report: Mapped["Report"] = relationship(back_populates="actors")

    specs: Mapped["list[Spec]"] = relationship(
        secondary=ActorSpecs.__table__,
        back_populates="actors",
    )
    abilities: Mapped["list[Ability]"] = relationship(
        secondary=ActorAbilities.__table__,
        back_populates="actors",
    )
    gear_sets: Mapped["list[Gear]"] = relationship(
        secondary=ActorGearSets.__table__,
        back_populates="actors",
    )
