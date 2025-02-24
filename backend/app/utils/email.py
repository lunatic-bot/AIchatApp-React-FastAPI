from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

conf = ConnectionConfig(
    MAIL_USERNAME="your-email@example.com",
    MAIL_PASSWORD="your-password",
    MAIL_FROM="your-email@example.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.your-email-provider.com",
    MAIL_TLS=True,
    MAIL_SSL=False
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
