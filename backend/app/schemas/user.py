from pydantic import BaseModel

# Base schema for user-related data
class UserBase(BaseModel):
    username: str  # Represents the username of the user

# Schema for creating a new user (includes password)
class UserCreate(UserBase):
    password: str  # Password required for user creation

# Schema for returning user details in API responses
class UserResponse(UserBase):
    id: int  # Unique user ID returned in responses

    class Config:
        # Enable ORM mode to allow SQLAlchemy models to be serialized as Pydantic models
        # orm_mode = True  
        
        # Required for Pydantic v2+ to properly handle attribute conversion
        from_attributes = True  



from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class TokenRefresh(BaseModel):
    access_token: str
    token_type: str

from pydantic import BaseModel, EmailStr

class ForgotPasswordRequest(BaseModel):
    email: EmailStr

class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str
