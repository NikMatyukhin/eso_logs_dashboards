from sqlalchemy.orm import Mapped

from db import Base, int_pk


class Gear(Base):
    __tablename__ = "gear"

    id: Mapped[int_pk]
    slot: Mapped[int]
    icon: Mapped[str]
    name: Mapped[str]
    set_id: Mapped[int]
    set_name: Mapped[str]
