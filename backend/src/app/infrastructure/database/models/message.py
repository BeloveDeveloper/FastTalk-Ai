from datetime import datetime
from sqlalchemy import BIGINT, String, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class MessageDB(Base):
    __tablename__ = "message"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    chat_id: Mapped[int] = mapped_column(
        BIGINT, ForeignKey("chat.id", ondelete="CASCADE"), nullable=False, index=True
    )
    text: Mapped[str] = mapped_column(String(), nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    is_bot: Mapped[bool] = mapped_column(Boolean, nullable=False)

    chat: Mapped["ChatDB"] = relationship("ChatDB", back_populates="messages")  # type: ignore
