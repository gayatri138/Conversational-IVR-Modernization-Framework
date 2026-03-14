# from fastapi import FastAPI
# from pydantic import BaseModel


# Importing libraries for Milestone 3 modules
from modules.dialog_manager import generate_response
from modules.nlu_engine import detect_intent
from modules.speech_service import listen, speak

# -----------------------------
# IVR SYSTEM CONFIGURATION
# -----------------------------

IVR_CONFIG = {
    "system_name": "Conversational IVR System",
    "version": "1.0",
    "default_language": "English",
    "mode": "simulation",
    "welcome_message": "Welcome to IRCTC Customer Care IVR"
}


# Importing Libraries
""" 
fastapi : Used to create the API (the backend IVR system)
uvicorn : Used to run the FastAPI server
pydantic (BaseModel) : Used to define the JSON input format.
"""

from fastapi import FastAPI
from pydantic import BaseModel

# Using FastAPI

app = FastAPI(title=IVR_CONFIG["system_name"])

# Input Model(JSON structure)
class UserInput(BaseModel):
    digit: int


# Welcome API

@app.get("/ivr/start")
def start_call():
    return {
        "message": IVR_CONFIG["welcome_message"],
        "menu": {
            "1": "PNR Status",
            "2": "Train Availability",
            "3": "Ticket Booking",
            "4": "Ticket Cancellation",
            "5": "Refund Status",
            "6": "Complaint Support",
            "7": "Talk to Customer Agent"
        }
    }

# Menu Handling code

@app.post("/ivr/menu")
def handle_menu(user: UserInput):

    if user.digit == 1:
        return {"response": "Please enter your PNR Number"}

    elif user.digit == 2:
        return {"response": "Please enter Train Number"}

    elif user.digit == 3:
        return {"response": "Ticket Booking Service Selected"}

    elif user.digit == 4:
        return {"response": "Ticket Cancellation Service Selected"}

    elif user.digit == 5:
        return {"response": "Refund Status Service Selected"}

    elif user.digit == 6:
        return {"response": "Complaint Support Selected"}

    elif user.digit == 7:
        return {"response": "Connecting to Customer Care Agent"}

    else:
        return {"response": "Invalid Option"}

#new endpoint

@app.get("/ivr/voice")
def voice_interaction():

    user_text = listen()

    intent = detect_intent(user_text)

    response = generate_response(intent)

    speak(response)

    return {
        "user_input": user_text,
        "intent": intent,
        "response": response
    }

# To Get Output Run :
# uvicorn main:app --reload
# Open Browser --- >
# http://127.0.0.1:8000/docs
