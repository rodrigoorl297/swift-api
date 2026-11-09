from datetime import datetime

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Sku(Base):
    __tablename__ = "skus"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    sku: Mapped[str] = mapped_column(String(120), index=True)
    title: Mapped[str] = mapped_column(String(120))
    quantity: Mapped[str] = mapped_column(String(120))
    status: Mapped[str] = mapped_column(String(40), default="in_stock")
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
