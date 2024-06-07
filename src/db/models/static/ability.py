from sqlalchemy.orm import Mapped, mapped_column

from db import Base, int_pk


class Ability(Base):
    __tablename__ = "ability"

    id: Mapped[int_pk]
    name: Mapped[str] = mapped_column(default="Unknown Ability")
    icon: Mapped[str]
    flags: Mapped[int]
    _type: Mapped[int]
