from datetime import datetime
from sqlalchemy import Integer, String, Float, Text, DateTime                  
from sqlalchemy.orm import Mapped, mapped_column
from services.db import Base

class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    title: Mapped[str] = mapped_column(String(100),index=True)
    description: Mapped[str|None] = mapped_column(Text,nullable=True)
    price: Mapped[float|None] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(DateTime,default=datetime.utcnow)                                                    