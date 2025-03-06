from pydantic import BaseModel, EmailStr

# Base schema for user-related data
class UserBase(BaseModel):
    username: str  # Represents the username of the user

# Schema for creating a new user (includes password)
class UserCreate(UserBase):
    email: EmailStr
    password: str  # Password required for user creation

# Create a schema for login requests
class UserLogin(BaseModel):
    username: str
    password: str

# Schema for returning user details in API responses
class UserResponse(UserBase):
    id: int  # Unique user ID returned in responses
    email: str
    class Config:
        # Enable ORM mode to allow SQLAlchemy models to be serialized as Pydantic models
        # orm_mode = True  
        
        # Required for Pydantic v2+ to properly handle attribute conversion
        from_attributes = True  



from pydantic import BaseModel  # Import BaseModel for data validation and serialization


class Token(BaseModel):
    """Schema for representing authentication tokens."""

    access_token: str  # The access token used for authentication
    refresh_token: str  # The refresh token used to generate a new access token
    token_type: str  # The type of token, typically "Bearer"


class TokenRefresh(BaseModel):
    """Schema for refreshing an expired access token."""

    access_token: str  # A newly generated access token
    token_type: str  # The type of token, typically "Bearer"


from pydantic import BaseModel, EmailStr  # Import EmailStr for email validation


class ForgotPasswordRequest(BaseModel):
    """Schema for requesting a password reset."""

    email: EmailStr  # User's email for sending a password reset link


class ResetPasswordRequest(BaseModel):
    """Schema for resetting a user's password."""

    token: str  # The password reset token sent to the user
    new_password: str  # The new password the user wants to set

