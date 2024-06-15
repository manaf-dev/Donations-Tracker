import os
from dotenv import load_dotenv
load_dotenv()
import requests
# from twilio.rest import Client

#sending using TWILIO
# def send_sms(recipient, message):
#     account_sid = str(os.getenv('TWILIO_SID'))
#     auth_token = str(os.getenv('TWILIO_AUTH_TOKEN'))

#     try:
#         client = Client(account_sid, auth_token)
#         message = client.messages.create(
#             body=message,
#             from_=str(os.getenv('TWILIO_NUM')),
#             to=recipient
#         )
#         print(message.sid)
#     except Exception as e:
#         print(f'Error: {e}')

#sending using mNotify
def send_sms(recipient, message):
    url = "https://apps.mnotify.net/smsapi"
    params = {
        'key': str(os.getenv('MNOTIFY_KEY')),
        'to': recipient,
        'msg': message,
        'sender_id': str(os.getenv('MNOTIFY_ID'))
    }
    try:
        response = requests.get(url, params=params)
        print(response)
    except Exception as e:
        print(f'Error: {e}')
    
