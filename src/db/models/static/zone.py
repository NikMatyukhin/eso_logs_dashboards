from sqlalchemy.orm import Mapped

from db import Base, int_pk


class Zone(Base):
    __tablename__ = "zone"

    id: Mapped[int_pk]
    name: Mapped[str]
