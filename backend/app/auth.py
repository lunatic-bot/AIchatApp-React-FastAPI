from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import AsyncSessionLocal
from models import User
from schemas import UserCreate, UserResponse, Token
from passlib.hash import bcrypt
from datetime import datetime, timedelta
from jose import JWTError, jwt
import os
from dotenv import load_dotenv
from pathlib import Path


env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)
SECRET_KEY = os.getenv("SECRET_KEY")  

# Secret key for JWT signing
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

auth_router = APIRouter()

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as db:
        yield db
        await db.close()

@auth_router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    hashed_password = bcrypt.hash(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def authenticate_user(db: AsyncSession, username: str, password: str):
    user = await db.execute(User.__table__.select().where(User.username == username))
    user = user.scalars().first()
    if not user or not bcrypt.verify(password, user.hashed_password):
        return None
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@auth_router.post("/login", response_model=Token)
async def login_for_access_token(username: str, password: str, db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(db, username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}



# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.ext.asyncio import AsyncSession
# from database import AsyncSessionLocal
# from models import User
# from schemas import UserCreate, UserResponse
# from passlib.hash import bcrypt

# # Create an APIRouter instance for authentication-related endpoints
# auth_router = APIRouter()

# # Dependency to get an async database session
# async def get_db() -> AsyncSession:
#     async with AsyncSessionLocal() as db:
#         yield db  # Yield the session for dependency injection
#         await db.close()  # Ensure the session is closed after use

# @auth_router.post("/register", response_model=UserResponse)
# async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
#     """
#     Registers a new user by:
#     1. Hashing the provided password.
#     2. Creating a new User instance.
#     3. Adding and committing the user to the database.
#     4. Returning the created user.

#     Args:
#         user (UserCreate): The user details received in the request body.
#         db (AsyncSession): The database session dependency.

#     Returns:
#         UserResponse: The created user details (excluding the password).
#     """

#     # Hash the user's password using bcrypt
#     hashed_password = bcrypt.hash(user.password)

#     # Create a new user instance with the hashed password
#     new_user = User(username=user.username, hashed_password=hashed_password)

#     # Add the new user to the database session
#     db.add(new_user)
    
#     # Commit the transaction to save the user in the database
#     await db.commit()

#     # Refresh the user instance to get updated values from the database
#     await db.refresh(new_user)
#     return new_user  # Return the created user (response schema ensures sensitive data is excluded)
