from sqlalchemy.orm import Mapped

from db import Base, int_pk


class DamageSource(Base):
    __tablename__ = "damage_source"

    id: Mapped[int_pk]
    name: Mapped[str]
    icon: Mapped[str]
    _type: Mapped[int]
