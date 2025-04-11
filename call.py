from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

call = client.calls.create(
    twiml='<Response><Say>Hello, this is a test call from your Python script. Goodbye!</Say></Response>',
    to=os.getenv("TO_PHONE_NUMBER"),
    from_=os.getenv("TWILIO_PHONE_NUMBER")
)

print(f"Call initiated with SID: {call.sid}")
