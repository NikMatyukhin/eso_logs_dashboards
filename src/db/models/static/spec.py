from sqlalchemy.orm import Mapped

from db import Base, int_pk


class Spec(Base):
    __tablename__ = "spec"

    id: Mapped[int_pk]
    name: Mapped[str]
    role: Mapped[str]
