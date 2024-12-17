from sqlalchemy import BIGINT, Boolean, String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class SubcriptionDB(Base):
    __tablename__ = "subcription"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), unique=True)
    description: Mapped[str] = mapped_column(String())
    price: Mapped[int] = mapped_column(Integer)
    total_req: Mapped[int] = mapped_column(Integer)
