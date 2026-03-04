from fastapi import APIRouter
from model import ContactForm
import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = os.getenv("EMAIL_TO")


@router.post("/send-message")
def send_message(data: ContactForm):

    body = f"""
New Contact Form Message

Name: {data.first_name} {data.last_name}
Email: {data.email}
Phone: {data.phone}

Message:
{data.message}
"""

    msg = MIMEText(body)

    msg["Subject"] = "New Website Contact Message"
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_TO
    msg["Reply-To"] = data.email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASS)
    server.sendmail(EMAIL_USER, EMAIL_TO, msg.as_string())
    server.quit()

    return {"status": "Message sent successfully"}