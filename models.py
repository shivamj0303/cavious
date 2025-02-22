from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    user_input = Column(String, nullable=False)
    intent = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
