from fastapi import APIRouter, HTTPException
from model import ContactForm
import smtplib
import os
from email.mime.text import MIMEText

router = APIRouter()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = os.getenv("EMAIL_TO")


@router.post("/send-message")
def send_message(data: ContactForm):

    if not EMAIL_USER or not EMAIL_PASS or not EMAIL_TO:
        raise HTTPException(status_code=500, detail="Email configuration missing")

    body = f"""
New Contact Form Message

Name: {data.first_name} {data.last_name}
Email: {data.email}
Phone: {data.phone}

Message:
{data.message}
"""

    try:
        msg = MIMEText(body)
        msg["Subject"] = "New Website Contact Form"
        msg["From"] = EMAIL_USER
        msg["To"] = EMAIL_TO

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)

        server.sendmail(EMAIL_USER, EMAIL_TO, msg.as_string())
        server.quit()

        return {"status": "Email sent successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))