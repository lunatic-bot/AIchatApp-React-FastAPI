from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User
from sqlalchemy.future import select
from passlib.hash import bcrypt
from core.config import settings
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

SECRET_KEY = os.getenv("SECRET_KEY")
REFRESH_SECRET_KEY = os.getenv("REFRESH_SECRET_KEY")  # Separate key for refresh token
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7  # Longer validity for refresh token

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    Creates an access token with a short expiration time.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(data: dict, expires_delta: timedelta | None = None):
    """
    Creates a refresh token with a longer expiration time.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, REFRESH_SECRET_KEY, algorithm=ALGORITHM)

def verify_refresh_token(token: str):
    """
    Verifies the refresh token and returns the username if valid.
    """
    try:
        payload = jwt.decode(token, REFRESH_SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")  # Return username
    except JWTError:
        return None


async def authenticate_user(db: AsyncSession, username: str, password: str):
    result = await db.execute(select(User).where(User.username == username))
    user = result.scalars().first()
    
    if not user or not bcrypt.verify(password, user.hashed_password):
        return False
    return user

# def create_access_token(data: dict, expires_delta: timedelta | None = None):
#     to_encode = data.copy()
#     expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
