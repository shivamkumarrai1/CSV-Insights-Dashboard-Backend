from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from .database import Base


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    summary = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
