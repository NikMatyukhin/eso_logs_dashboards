from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from db import Base, int_pk

if TYPE_CHECKING:
    from db.models.report import Report


class Region(Base):
    __tablename__ = "region"

    id: Mapped[int_pk]
    name: Mapped[str]
    slug: Mapped[str]

    reports: Mapped[list["Report"]] = relationship(back_populates="region")
