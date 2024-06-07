from datetime import time, date

from sqlalchemy import ForeignKey, PrimaryKeyConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base, str_pk
from db.models.static import Region, Zone, DamageSource
from db.models.fight import Fight
from db.models.actor import Actor


class ReportDamageSources(Base):
    __tablename__ = "report_damage_sources"
    __table_args__ = (PrimaryKeyConstraint("report_code", "damage_source_id"),)

    total: Mapped[int]

    report_code: Mapped[str] = mapped_column(ForeignKey("report.code"))
    damage_source_id: Mapped[int] = mapped_column(ForeignKey("damage_source.id"))


class Report(Base):
    __tablename__ = "report"
    __table_args__ = (
        CheckConstraint(r"start_time <= end_time", "start_less_than_end"),
    )

    code: Mapped[str_pk]
    title: Mapped[str]
    start_time: Mapped[date]
    end_time: Mapped[date]

    trial_score: Mapped[int | None]
    trial_time: Mapped[time | None]

    region_id: Mapped[int] = mapped_column(ForeignKey("region.id"))
    region: Mapped["Region"] = relationship()

    zone_id: Mapped[int] = mapped_column(ForeignKey("zone.id"))
    zone: Mapped["Zone"] = relationship()

    actors: Mapped["list[Actor]"] = relationship(back_populates="report")

    fights: Mapped["list[Fight]"] = relationship(back_populates="report")

    damage_sources: Mapped["list[DamageSource]"] = relationship(
        secondary=ReportDamageSources.__table__,
        back_populates="reports",
    )
