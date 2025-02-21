from sqlalchemy import Column, Integer, String, Boolean
from utils.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True)
    phone_number = Column(String, nullable=True)
    is_verified = Column(Boolean, default=False)