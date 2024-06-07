from sqlalchemy.orm import Mapped, mapped_column

from db import Base, int_pk


class Partition(Base):
    __tablename__ = "partition"

    id: Mapped[int_pk]
    name: Mapped[str]
    compact_name: Mapped[str]
    default: Mapped[bool] = mapped_column(default=False)
