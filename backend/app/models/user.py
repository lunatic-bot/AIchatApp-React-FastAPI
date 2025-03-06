from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func  # Import necessary SQLAlchemy modules
from sqlalchemy.orm import relationship  # Import relationship for ORM associations
from database.connection import Base  # Import Base from the database connection module


class User(Base):
    """Represents the User table in the database."""

    __tablename__ = "users"  # Define table name

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    # Unique identifier for each user, automatically incremented

    username = Column(String, unique=True, index=True, nullable=False)  
    # Stores the username, must be unique and cannot be null

    hashed_password = Column(String, nullable=False)  
    # Stores the hashed version of the user's password

    tokens = relationship("Token", back_populates="user", cascade="all, delete-orphan")  
    # Establishes a one-to-many relationship with the Token table
    # If a user is deleted, all associated tokens are also deleted


class Token(Base):
    """Represents the Token table in the database, storing user authentication tokens."""

    __tablename__ = "tokens"  # Define table name

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  
    # Unique identifier for each token, automatically incremented

    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)  
    # Foreign key referencing the User table
    # If the associated user is deleted, the token is also deleted

    jwt_token = Column(String, nullable=False, unique=True)  
    # Stores the JWT token string, must be unique

    token_expiry = Column(DateTime, nullable=False)  
    # Stores the token's expiration date and time

    created_at = Column(DateTime, server_default=func.now())  
    # Stores the timestamp when the token was created, defaults to the current time

    user = relationship("User", back_populates="tokens")  
    # Defines the reverse relationship with the User table
