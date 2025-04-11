from dotenv import load_dotenv
from twilio.rest import Client
import os

load_dotenv()

print("SID:", os.getenv("TWILIO_ACCOUNT_SID"))
print("TOKEN:", os.getenv("TWILIO_AUTH_TOKEN"))
print("FROM:", os.getenv("TWILIO_PHONE_NUMBER"))
print("TO:", os.getenv("TO_PHONE_NUMBER"))


client = Client(
    os.getenv("TWILIO_ACCOUNT_SID"),
    os.getenv("TWILIO_AUTH_TOKEN")
)

message = client.messages.create(
    body="Hello from VS Code and Twilio!",
    from_=os.getenv("TWILIO_PHONE_NUMBER"),
    to=os.getenv("TO_PHONE_NUMBER")
)

print(f"Sent message with SID: {message.sid}")