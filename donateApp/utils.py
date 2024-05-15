import os
from dotenv import load_dotenv
load_dotenv()
from twilio.rest import Client
from DonationTracker import settings


def send_sms(recipient, message):
    account_sid = str(os.getenv('TWILIO_SID'))
    auth_token = str(os.getenv('TWILIO_AUTH_TOKEN'))

    try:
        client = Client(account_sid, auth_token)
        client = client.messages.create(
            body=message,
            from_=str(os.getenv('TWILIO_NUM')),
            to=recipient
        )
    except Exception as e:
        return ''