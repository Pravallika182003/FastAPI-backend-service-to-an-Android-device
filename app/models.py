import enum
from datetime import datetime  ,  timezone

from sqlalchemy import Column, Integer, String, DateTime, Enum,DateTime, ForeignKey,Text
from sqlalchemy.orm import relationship


from app.database import Base

class NotificationStatus(str, enum.Enum):
    SENT  = "sent"
    FAILED = "failed"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at =Column(DateTime, default =lambda: datetime.now(timezone.utc))
    notifications = relationship("Notification", back_populates="user")

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    fcm_message_id = Column(String, nullable=True)
    status = Column(Enum(NotificationStatus), default=NotificationStatus.SENT)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    user = relationship("User", back_populates="notifications")