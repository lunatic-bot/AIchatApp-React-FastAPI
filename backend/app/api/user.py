from fastapi import APIRouter, Depends, HTTPException, status, Response
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

# @auth_router.post("/login", response_model=Token)
# async def login_for_access_token(username: str, password: str, db: AsyncSession = Depends(get_db)):
#     """
#     Authenticates a user and returns both an access token and a refresh token.
#     """
#     user = await authenticate_user(db, username, password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

#     access_token = create_access_token(data={"sub": user.username})
#     refresh_token = create_refresh_token(data={"sub": user.username})  # Generate refresh token

#     return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@auth_router.post("/login")
async def login_for_access_token(
    response: Response, username: str, password: str, db: AsyncSession = Depends(get_db)
):
    """
    Authenticates a user and stores the access token in a secure HTTP-only cookie.
    """
    # Verify user credentials
    user = await authenticate_user(db, username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Generate access and refresh tokens
    access_token = create_access_token(data={"sub": user.username})
    refresh_token = create_refresh_token(data={"sub": user.username})

    # Store access token in an HTTP-only cookie
    response.set_cookie(
        key="access_token",
        value=f"Bearer {access_token}",
        httponly=True,  # Prevent JavaScript access (XSS protection)
        secure=True,  # Ensure it's only sent over HTTPS
        samesite="Strict",  # Prevent CSRF
    )

    return {"refresh_token": refresh_token, "message": "Login successful"}



@auth_router.post("/refresh", response_model=TokenRefresh)
async def refresh_access_token(refresh_token: str):
    """
    Generates a new access token using a valid refresh token.
    """
    # Verify the provided refresh token and extract the associated username
    username = verify_refresh_token(refresh_token)  
    
    # If verification fails, raise an unauthorized error
    if not username:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    # Generate a new access token for the user
    new_access_token = create_access_token(data={"sub": username})

    # Return the new access token
    return {"access_token": new_access_token, "token_type": "bearer"}


@auth_router.post("/forgot-password")
async def forgot_password(request: ForgotPasswordRequest, db: AsyncSession = Depends(get_db)):
    """
    Handles forgot password requests by generating a reset link and sending an email.
    """
    # Query the database to find the user with the given email
    result = await db.execute(select(User).where(User.email == request.email))
    user = result.scalars().first()

    # If no user is found, return a 404 error
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Generate a password reset token for the user
    reset_token = create_reset_token(user.email)

    # Construct the password reset link with the generated token
    reset_link = f"http://yourfrontend.com/reset-password?token={reset_token}"

    # Send the reset link via email
    await send_reset_email(user.email, reset_link)

    # Return a success message
    return {"message": "Password reset link sent to your email"}


@auth_router.post("/reset-password")
async def reset_password(request: ResetPasswordRequest, db: AsyncSession = Depends(get_db)):
    """
    Resets the user's password using a valid reset token.
    """
    # Verify the reset token and extract the email associated with it
    email = verify_token(request.token)

    # If the token is invalid or expired, return a 400 error
    if not email:
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    # Query the database to find the user with the extracted email
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalars().first()

    # If no user is found, return a 404 error
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Hash the new password before storing it
    hashed_password = bcrypt.hash(request.new_password)
    user.hashed_password = hashed_password

    # Commit the updated password to the database
    await db.commit()

    # Return a success message
    return {"message": "Password reset successful"}
