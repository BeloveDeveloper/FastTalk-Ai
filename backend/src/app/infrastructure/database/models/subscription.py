from sqlalchemy import BIGINT, String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class SubscriptionDB(Base):
    __tablename__ = "subscription"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), unique=True)
    description: Mapped[str] = mapped_column(String())
    price: Mapped[int] = mapped_column(Integer)
    req_limit: Mapped[int] = mapped_column(Integer)
