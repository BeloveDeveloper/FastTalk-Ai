from datetime import datetime
from sqlalchemy import BIGINT, ForeignKey, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class ChatDB(Base):
    __tablename__ = "chat"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey("user.id", ondelete="CASCADE"), nullable=False, index=True
    )
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)

    user: Mapped["UserDB"] = relationship("UserDB", back_populates="chats")  # type: ignore
    messages: Mapped[list["MessageDB"]] = relationship(  # type: ignore
        "MessageDB", back_populates="chat", cascade="all, delete-orphan"
    )
