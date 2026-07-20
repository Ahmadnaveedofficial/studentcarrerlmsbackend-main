import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Load env variables every time send_email is called
def send_email(subject: str, name: str, body: str, to_email: str):
    load_dotenv(override=True)
    Admin_Email = os.getenv("ADMIN_EMAIL")
    Admin_Password = os.getenv("ADMIN_PASSWORD")

    print("EMAIL:", repr(Admin_Email))
    print("PASSWORD:", repr(Admin_Password))

    msg = EmailMessage()
    msg['From'] = f"{name} <{Admin_Email}>"
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(Admin_Email, Admin_Password)
            smtp.send_message(msg)
        print("✅ Email sent")
        return True
    except Exception as e:
        print("❌ Failed to send email:", e)
        return False
