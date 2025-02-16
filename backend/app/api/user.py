from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database.connection import get_db
from auth.models import User
from auth.schemas import UserCreate, UserResponse, Token
from auth.utils import create_access_token, authenticate_user
from passlib.hash import bcrypt
from sqlalchemy.future import select

auth_router = APIRouter()

@auth_router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    hashed_password = bcrypt.hash(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

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
