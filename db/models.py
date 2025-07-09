from sqlalchemy import Column, Integer, String, Text
from .base import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    sentiment = Column(String, nullable=False)
    created_at = Column(String, nullable=False)
