from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins.int_id_pk import IdIntPKMixin


class User(IdIntPKMixin, Base):
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    foo: Mapped[int]
    bar: Mapped[int]

    __table_args__ = (UniqueConstraint('foo', 'bar'),
                      )
