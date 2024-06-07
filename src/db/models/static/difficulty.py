from sqlalchemy.orm import Mapped

from db import Base, int_pk


class Difficulty(Base):
    __tablename__ = "difficulty"

    id: Mapped[int_pk]
    name: Mapped[str]
