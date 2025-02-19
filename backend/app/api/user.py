from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database.connection import get_db  # Import function to get the database session
from models.user import User  # Import User model
from schemas.user import UserCreate, UserResponse, Token  # Import Pydantic schemas for validation
from utils.auth import create_access_token, authenticate_user  # Import authentication utility functions
from passlib.hash import bcrypt  # Library for hashing passwords

# Create a router for authentication-related endpoints
auth_router = APIRouter()

@auth_router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    Registers a new user.
    
    - Hashes the user's password before storing it.
    - Saves the user in the database.
    - Returns the newly created user (excluding sensitive fields like the password).
    """
    hashed_password = bcrypt.hash(user.password)  # Hash the password before storing
    new_user = User(username=user.username, hashed_password=hashed_password)  # Create a new User object
    db.add(new_user)  # Add user to the session
    await db.commit()  # Commit the transaction
    await db.refresh(new_user)  # Refresh the instance to get updated data
    return new_user  # Return the created user data (as per UserResponse schema)

@auth_router.post("/login", response_model=Token)
async def login_for_access_token(username: str, password: str, db: AsyncSession = Depends(get_db)):
    """
    Authenticates a user and returns an access token.
    
    - Checks if the provided username and password match a registered user.
    - If authentication fails, raises an HTTP 401 Unauthorized error.
    - If successful, generates and returns a JWT access token.
    """
    user = await authenticate_user(db, username, password)  # Authenticate the user
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.username})  # Generate JWT token
    return {"access_token": access_token, "token_type": "bearer"}  # Return token response
