import os
from dotenv import load_dotenv
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

# Load environment variables from .env file
load_dotenv()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=int(os.getenv("MAIL_PORT", 587)),  # Default to 587 if not set
    MAIL_SERVER=os.getenv("MAIL_SERVER"),
    MAIL_TLS=os.getenv("MAIL_TLS", "True").lower() == "true",
    MAIL_SSL=os.getenv("MAIL_SSL", "False").lower() == "true"
)

async def send_reset_email(email: str, reset_link: str):
    """Sends password reset email"""
    message = MessageSchema(
        subject="Password Reset Request",
        recipients=[email],
        body=f"Click the link to reset your password: {reset_link}",
        subtype="html",
    )

    fm = FastMail(conf)
    await fm.send_message(message)
