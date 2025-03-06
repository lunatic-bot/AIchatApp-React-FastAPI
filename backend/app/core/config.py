import os  # Importing OS module to access environment variables
from dotenv import load_dotenv  # Load environment variables from .env file
from pathlib import Path  # Path handling utilities

# Define the path to the .env file (located three levels up from the current file)
env_path = Path(__file__).parent.parent.parent / '.env'

# Load environment variables from the .env file
load_dotenv(dotenv_path=env_path)

class Settings:
    """
    Configuration settings for the application.
    """
    SECRET_KEY: str = os.getenv("SECRET_KEY")  # Secret key for signing JWT tokens
    ALGORITHM: str = "HS256"  # Algorithm used for JWT encoding/decoding
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Access token expiration time in minutes

# Create a settings instance to be used throughout the application
settings = Settings()

