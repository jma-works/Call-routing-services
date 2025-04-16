import os
from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse
import openai

app = Flask(__name__)

# Make sure you have set these in your .env file (see Step 3)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configure OpenAI client
openai.api_key = OPENAI_API_KEY

@app.route("/incoming-call", methods=["POST"])
def incoming_call():
    # Create a new TwiML response
    response = VoiceResponse()
    
    # For demonstration, say a welcome message.
    response.say("Hello. Please hold while we connect you to the AI assistant.", voice="alice")
    
    # In a more advanced version you could use <Gather> to capture spoken input,
    # then send the transcription to OpenAI via openai.ChatCompletion.create(...)

    # Return the XML
    return Response(str(response), mimetype="text/xml")

if __name__ == '__main__':
    # Run on port 5000 (or use environment variable PORT if needed)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
