from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

# Define the ChatRoom model representing chat rooms
class ChatRoom(Base):
    __tablename__ = "chat_rooms"

    id = Column(Integer, primary_key=True, index=True)  # Unique chat room ID
    name = Column(String, unique=True, nullable=False)  # Unique chat room name (required)

# Define the Message model representing messages sent in chat rooms
class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)  # Unique message ID
    content = Column(Text, nullable=False)  # Message content (required)
    timestamp = Column(DateTime, default=datetime.now(datetime.timezone.utc))  # Timestamp when the message was sent
    sender_id = Column(Integer, ForeignKey("users.id"))  # Foreign key linking to the sender (User)
    room_id = Column(Integer, ForeignKey("chat_rooms.id"))  # Foreign key linking to the chat room

    # Define relationships for easier querying
    sender = relationship("User")  # Relationship to fetch sender details
    room = relationship("ChatRoom")  # Relationship to fetch room details

