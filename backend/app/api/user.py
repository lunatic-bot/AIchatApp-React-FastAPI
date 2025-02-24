from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database.connection import get_db  # Import function to get the database session
from models.user import User  # Import User model
from schemas.user import UserCreate, UserResponse, Token , TokenRefresh, ResetPasswordRequest, ForgotPasswordRequest # Import Pydantic schemas for validation
from passlib.hash import bcrypt  # Library for hashing passwords
from utils.auth import create_access_token, create_refresh_token, verify_refresh_token, authenticate_user, verify_token, create_reset_token

from utils.email import send_reset_email

from sqlalchemy.future import select

# Create a router for authentication-related endpoints
auth_router = APIRouter()

@auth_router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    Registers a new user.
    - Hashes the user's password before storing it.
    - Saves the user in the database.
    - Returns the newly created user.
    """
    hashed_password = bcrypt.hash(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@auth_router.post("/login", response_model=Token)
async def login_for_access_token(username: str, password: str, db: AsyncSession = Depends(get_db)):
    """
    Authenticates a user and returns both an access token and a refresh token.
    """
    user = await authenticate_user(db, username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.username})
    refresh_token = create_refresh_token(data={"sub": user.username})  # Generate refresh token

    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@auth_router.post("/refresh", response_model=TokenRefresh)
async def refresh_access_token(refresh_token: str):
    """
    Generates a new access token using a valid refresh token.
    """
    username = verify_refresh_token(refresh_token)  # Validate and decode refresh token
    if not username:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    new_access_token = create_access_token(data={"sub": username})
    return {"access_token": new_access_token, "token_type": "bearer"}



@auth_router.post("/forgot-password")
async def forgot_password(request: ForgotPasswordRequest, db: AsyncSession = Depends(get_db)):
    """Handles forgot password requests"""
    result = await db.execute(select(User).where(User.email == request.email))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    reset_token = create_reset_token(user.email)
    reset_link = f"http://yourfrontend.com/reset-password?token={reset_token}"

    # Send email
    await send_reset_email(user.email, reset_link)

    return {"message": "Password reset link sent to your email"}



@auth_router.post("/reset-password")
async def reset_password(request: ResetPasswordRequest, db: AsyncSession = Depends(get_db)):
    """Resets the user's password"""
    email = verify_token(request.token)  # Extract email from token

    if not email:
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    result = await db.execute(select(User).where(User.email == email))
    user = result.scalars().first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Hash new password
    hashed_password = bcrypt.hash(request.new_password)
    user.hashed_password = hashed_password

    await db.commit()
    return {"message": "Password reset successful"}