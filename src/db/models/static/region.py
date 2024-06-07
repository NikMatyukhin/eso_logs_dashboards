from sqlalchemy.orm import Mapped

from db import Base, int_pk


class Region(Base):
    __tablename__ = "region"

    id: Mapped[int_pk]
    name: Mapped[str]
    slug: Mapped[str]
