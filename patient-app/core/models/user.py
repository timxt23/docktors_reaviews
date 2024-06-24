import enum
from datetime import datetime, timezone
from typing import Annotated

from sqlalchemy import UniqueConstraint, func, text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins.int_id_pk import IdIntPKMixin

created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.now(timezone.utc),
    )]


class UserStatus(enum.Enum):
    NEW = 'NEW',
    MODERATE = 'MODERATE',
    ACTIVE = 'ACTIVE',


class Spec(Base, IdIntPKMixin):
    title: Mapped[str]

    users: Mapped[list["users"]] = relationship(
        back_populates='users'
    )


class User(IdIntPKMixin, Base):
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(unique=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    speciality: Mapped[str] = mapped_column(ForeignKey('specs.id'), nullable=False)
    tg_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    prodoctor_url: Mapped[str]
    is_active: Mapped[UserStatus] = mapped_column(nullable=False, default=UserStatus.NEW)
    is_banned: Mapped[bool] = mapped_column(nullable=False, default=False)
    files: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    specs: Mapped["specs"] = relationship(
        back_populates="specs"
    )
