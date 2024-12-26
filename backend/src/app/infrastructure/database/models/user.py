from sqlalchemy import BIGINT, Boolean, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class UserDB(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(255), unique=True)
    email: Mapped[str | None] = mapped_column(String(255), unique=True)
    telegram_id: Mapped[int | None] = mapped_column(Integer, nullable=True, unique=True)
    phone_number: Mapped[str | None] = mapped_column(String(255))
    password_hash: Mapped[str | None] = mapped_column(String, nullable=True)
    total_req: Mapped[int] = mapped_column(Integer, default=0)
    is_premium: Mapped[bool] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    chats: Mapped[list["ChatDB"]] = relationship(
        "ChatDB", back_populates="user", cascade="all, delete-orphan"  # type: ignore
    )
