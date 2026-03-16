from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv
import os
import random
import smtplib
from email.message import EmailMessage
from datetime import datetime, timedelta

from app.core.security import create_access_token

from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db
from app.models.admin_user import AdminUser

load_dotenv()

router = APIRouter(prefix="/auth", tags=["Auth"])

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
FROM_EMAIL = os.getenv("FROM_EMAIL")

# Store OTP with expiry
otp_store = {}


def send_otp_email(otp: str):
    msg = EmailMessage()
    msg["Subject"] = "Your Admin Login OTP"
    msg["From"] = FROM_EMAIL
    msg["To"] = ADMIN_EMAIL
    msg.set_content(f"Your OTP is: {otp}\n\nValid for 5 minutes.")

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)


@router.post("/login")
def request_otp():
    otp = str(random.randint(100000, 999999))
    expiry = datetime.utcnow() + timedelta(minutes=5)

    otp_store["admin"] = {
        "otp": otp,
        "expires": expiry
    }

    send_otp_email(otp)

    return {
        "message": "OTP sent to admin email",
        "expires_in_seconds": 300
    }

@router.post("/verify-otp")
def verify_otp(data: dict, db: Session = Depends(get_db)):
    otp = data.get("otp")

    stored = otp_store.get("admin")

    if not stored:
        raise HTTPException(status_code=400, detail="No OTP requested")

    if datetime.utcnow() > stored["expires"]:
        raise HTTPException(status_code=400, detail="OTP expired")

    if stored["otp"] != otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    # 🔹 Fetch admin from database
    admin = db.query(AdminUser).filter(AdminUser.email == ADMIN_EMAIL).first()

    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")

    # 🔹 Create JWT token with admin id
    access_token = create_access_token({"sub": str(admin.id)})

    # Clear OTP
    otp_store.pop("admin", None)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }