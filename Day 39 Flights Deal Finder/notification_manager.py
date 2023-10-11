import ssl
import smtplib
import os
from dotenv import load_dotenv

load_dotenv(".env")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
USER = os.getenv("USER")

class NotificationManager:
    def __init__(self):
        pass

    def send_email(self, message):
        server = smtplib.SMTP('smtp.gmail.com', port=587)
        context = ssl.create_default_context()
        server.starttls(context=context)
        server.login(user=MY_EMAIL, password=MY_PASSWORD)
        server.sendmail(from_addr=MY_EMAIL, to_addrs=USER, message=message)