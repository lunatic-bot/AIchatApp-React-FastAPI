from datetime import datetime, timedelta, timezone  # Importing datetime utilities for token expiration handling
from jose import jwt, JWTError  # JWT encoding and decoding
from sqlalchemy.ext.asyncio import AsyncSession  # Asynchronous database session for queries
from models.user import User  # User model for authentication
from sqlalchemy.future import select  # SQLAlchemy's future-compatible select statement
from passlib.hash import bcrypt  # Password hashing and verification
from core.config import settings  # Configuration settings
import os  # OS module to access environment variables
from dotenv import load_dotenv  # Load environment variables from .env file
from pathlib import Path  # Path handling utilities
from database.connection import get_db
    
from fastapi import Depends, HTTPException, status, Request

# Load environment variables from the .env file
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Secret keys for signing JWT tokens
SECRET_KEY = os.getenv("SECRET_KEY")  # Secret key for access token
REFRESH_SECRET_KEY = os.getenv("REFRESH_SECRET_KEY")  # Separate secret key for refresh token

# JWT Algorithm
ALGORITHM = "HS256"

# Token expiration durations
ACCESS_TOKEN_EXPIRE_MINUTES = 2  # Access token expires in 30 minutes
REFRESH_TOKEN_EXPIRE_DAYS = 7  # Refresh token expires in 7 days

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    Creates an access token with a short expiration time.

    Args:
        data (dict): The payload data to encode in the token.
        expires_delta (timedelta, optional): Custom expiration time. Defaults to ACCESS_TOKEN_EXPIRE_MINUTES.

    Returns:
        str: Encoded JWT access token.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})  # Add expiration time to payload
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # Encode and return JWT token

def create_refresh_token(data: dict, expires_delta: timedelta | None = None):
    """
    Creates a refresh token with a longer expiration time.

    Args:
        data (dict): The payload data to encode in the token.
        expires_delta (timedelta, optional): Custom expiration time. Defaults to REFRESH_TOKEN_EXPIRE_DAYS.

    Returns:
        str: Encoded JWT refresh token.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS))
    to_encode.update({"exp": expire})  # Add expiration time to payload
    return jwt.encode(to_encode, REFRESH_SECRET_KEY, algorithm=ALGORITHM)  # Encode and return JWT token

def verify_refresh_token(token: str):
    """
    Verifies the refresh token and returns the username if valid.

    Args:
        token (str): The JWT refresh token to verify.

    Returns:
        str | None: The username if the token is valid, otherwise None.
    """
    try:
        payload = jwt.decode(token, REFRESH_SECRET_KEY, algorithms=[ALGORITHM])  # Decode token
        return payload.get("sub")  # Extract and return the username (subject)
    except JWTError:
        return None  # Return None if token verification fails

async def authenticate_user(db: AsyncSession, username: str, password: str):
    """
    Authenticates a user by verifying their username and password.

    Args:
        db (AsyncSession): Asynchronous database session for querying user data.
        username (str): The username provided by the user.
        password (str): The password provided by the user.

    Returns:
        User | bool: Returns the User object if authentication is successful, otherwise False.
    """
    # Query the database for the user by username
    result = await db.execute(select(User).where(User.username == username))
    user = result.scalars().first()  # Fetch the first matching user
    
    # Verify if user exists and password is correct
    if not user or not bcrypt.verify(password, user.hashed_password):
        return False  # Authentication failed

    return user  # Return authenticated user object


RESET_TOKEN_EXPIRE_MINUTES = 15  # Token validity

def create_reset_token(email: str):
    """Generate a password reset token"""
    expire = datetime.now(timezone.utc) + timedelta(minutes=RESET_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": email, "exp": expire}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str):
    """Decodes and verifies the JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")  # Extract email
    except JWTError:
        return None


async def get_current_user(request: Request, db: AsyncSession = Depends(get_db)):
    """
    Extracts and verifies the JWT token from cookies to get the current user.
    """
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    try:
        # Remove "Bearer " prefix before decoding
        token = token.replace("Bearer ", "")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
            )

        # Query user from the database
        result = await db.execute(select(User).where(User.username == username))
        user = result.scalars().first()

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
            )

        return user  # Successfully authenticated user

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )


