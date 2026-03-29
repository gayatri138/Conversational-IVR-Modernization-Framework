from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from ivr_data import railway_data

# ----------------------------
# CONFIGURATION
# ----------------------------
APP_NAME = "IRCTC Smart IVR"
APP_VERSION = "4.0"

WELCOME_PROMPT = (
    "Welcome to IRCTC customer support system. "
    "Press or say 1 for PNR status, "
    "2 for train schedule, "
    "3 for booking status, "
    "4 for complaint status, "
    "5 for cancellation details, "
    "6 for refund status, "
    "7 to repeat the menu."
)

WELCOME_TEXT = (
    "Welcome to IRCTC Customer Support System\n\n"
    "Press 1 for PNR Status\n"
    "Press 2 for Train Schedule\n"
    "Press 3 for Booking Status\n"
    "Press 4 for Complaint Status\n"
    "Press 5 for Cancellation Details\n"
    "Press 6 for Refund Status\n"
    "Press 7 to Repeat Menu"
)

app = FastAPI(title=APP_NAME, version=APP_VERSION)

# ----------------------------
# REQUEST MODEL
# ----------------------------
class UserInput(BaseModel):
    message: str

# ----------------------------
# FRONTEND ROUTE
# ----------------------------
@app.get("/")
def login_page():
    return FileResponse("login.html")


@app.get("/ivr-ui")
def ivr_ui():
    return FileResponse("index.html")

# ----------------------------
# WELCOME ROUTE
# ----------------------------
@app.get("/welcome")
def welcome():
    return {
        "text": WELCOME_TEXT,
        "speech": WELCOME_PROMPT
    }

# ----------------------------
# MAIN IVR ROUTE
# ----------------------------
@app.post("/ivr")
def ivr_response(user_input: UserInput):
    msg = user_input.message.strip().lower()

    # -------- PNR STATUS --------
    if msg in ["1", "pnr", "check pnr", "pnr status"]:
        return {
            "text": "Please enter your 10 digit PNR number.",
            "speech": "Please enter your ten digit PNR number."
        }

    elif msg in railway_data["pnr"]:
        data = railway_data["pnr"][msg]
        return {
            "text": (
                f"PNR Status: {data['status']}\n"
                f"Train Number: {data['train_number']}\n"
                f"Train Name: {data['train_name']}\n"
                f"From: {data['from']}\n"
                f"To: {data['to']}\n"
                f"Journey Date: {data['date']}\n"
                f"Departure Time: {data['departure_time']}"
            ),
            "speech": (
                f"Your PNR status is {data['status']}. "
                f"Train number {data['train_number']}, {data['train_name']}, "
                f"from {data['from']} to {data['to']}, "
                f"on {data['date']} at {data['departure_time']}."
            )
        }

    # -------- TRAIN SCHEDULE --------
    elif msg in ["2", "train schedule", "schedule", "train timing"]:
        return {
            "text": "Please enter your train number.",
            "speech": "Please enter your train number."
        }

    elif msg in railway_data["train_schedule"]:
        data = railway_data["train_schedule"][msg]
        return {
            "text": (
                f"Train Number: {msg}\n"
                f"Train Name: {data['train_name']}\n"
                f"From: {data['from']}\n"
                f"To: {data['to']}\n"
                f"Departure: {data['departure']}\n"
                f"Arrival: {data['arrival']}\n"
                f"Platform: {data['platform']}"
            ),
            "speech": (
                f"Train number {msg}, {data['train_name']}, "
                f"runs from {data['from']} to {data['to']}. "
                f"Departure is at {data['departure']}, "
                f"arrival is at {data['arrival']}, "
                f"from platform {data['platform']}."
            )
        }

    # -------- BOOKING STATUS --------
    elif msg in ["3", "booking", "booking status", "ticket booking"]:
        data = railway_data["booking"]["book123"]
        return {
            "text": (
                f"Booking Status: {data['status']}\n"
                f"Route: {data['route']}\n"
                f"Journey Date: {data['date']}\n"
                f"Class: {data['class']}"
            ),
            "speech": (
                f"Your booking status is {data['status']}. "
                f"Route is {data['route']}, "
                f"on {data['date']}, "
                f"class {data['class']}."
            )
        }

    # -------- COMPLAINT STATUS --------
    elif msg in ["4", "complaint", "complaint status", "register complaint"]:
        return {
            "text": "Please enter your complaint ID.",
            "speech": "Please enter your complaint ID."
        }

    elif msg in railway_data["complaints"]:
        data = railway_data["complaints"][msg]
        return {
            "text": (
                f"Complaint Issue: {data['issue']}\n"
                f"Complaint Status: {data['status']}\n"
                f"Registered Date: {data['registered_date']}\n"
                f"Expected Resolution: {data['expected_resolution']}"
            ),
            "speech": (
                f"Your complaint is for {data['issue']}. "
                f"Current status is {data['status']}. "
                f"Registered on {data['registered_date']}. "
                f"Expected resolution is {data['expected_resolution']}."
            )
        }

    # -------- CANCELLATION DETAILS --------
    elif msg in ["5", "cancellation", "cancel ticket", "cancellation status"]:
        return {
            "text": "Please enter your cancellation request ID.",
            "speech": "Please enter your cancellation request ID."
        }

    elif msg in railway_data["cancellation"]:
        data = railway_data["cancellation"][msg]
        return {
            "text": (
                f"PNR Number: {data['pnr']}\n"
                f"Cancellation Status: {data['status']}\n"
                f"Refund Amount: {data['refund_amount']}\n"
                f"Processed Date: {data['processed_date']}"
            ),
            "speech": (
                f"Your cancellation status is {data['status']}. "
                f"Refund amount is {data['refund_amount']}. "
                f"Processed date is {data['processed_date']}."
            )
        }

    # -------- REFUND STATUS --------
    elif msg in ["6", "refund", "refund status"]:
        return {
            "text": "Please enter your refund reference ID.",
            "speech": "Please enter your refund reference ID."
        }

    elif msg in railway_data["refund"]:
        data = railway_data["refund"][msg]
        return {
            "text": (
                f"PNR Number: {data['pnr']}\n"
                f"Refund Status: {data['refund_status']}\n"
                f"Refund Amount: {data['amount']}\n"
                f"Credited Date: {data['credited_date']}"
            ),
            "speech": (
                f"Your refund status is {data['refund_status']}. "
                f"Refund amount is {data['amount']}. "
                f"Credited date is {data['credited_date']}."
            )
        }

    # -------- REPEAT MENU --------
    elif msg in ["7", "repeat menu", "menu"]:
        return {
            "text": WELCOME_TEXT,
            "speech": WELCOME_PROMPT
        }

    # -------- INVALID INPUT --------
    else:
        return {
            "text": (
                "Invalid Input\n\n"
                "Press 1 for PNR Status\n"
                "Press 2 for Train Schedule\n"
                "Press 3 for Booking Status\n"
                "Press 4 for Complaint Status\n"
                "Press 5 for Cancellation Details\n"
                "Press 6 for Refund Status\n"
                "Press 7 to Repeat Menu"
            ),
            "speech": (
                "Invalid input. Please press 1 for PNR status, "
                "2 for train schedule, 3 for booking status, "
                "4 for complaint status, 5 for cancellation details, "
                "6 for refund status, or 7 to repeat the menu."
            )
        }