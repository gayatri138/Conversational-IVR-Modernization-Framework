# Conversational-IVR-Modernization-Framework
## Module 1 – Legacy System Analysis

This repository contains documentation related to:
- Traditional VXML-Based IVR Architecture (IRCTC Use Case)
- Integration with ACS and BAP
- Technical Challenges and Compatibility Gaps
- System Constraints and Modernization Requirements

## Module 2 – IVR System Implementation
This focuses on implementing a basic IVR system using a web-based simulator. The goal was to replicate a traditional IVR workflow similar to the IRCTC customer care system and demonstrate menu-driven interaction using API endpoints.

#Features Implemented

-IVR welcome prompt for users
-Menu options for common railway services
-Menu/key handling for user selections
-API-based interaction using FastAPI
-Web simulator testing using FastAPI documentation interface
-JSON request and response handling

#Technologies Used

-Python , FastAPI, Uvicorn server , JSON-based API responses 

#IVR Menu :-
Example 
-Check PNR Status
-Train Schedule Information
-Ticket Booking
-Ticket Cancellation
-Fare Enquiry
-Complaint Registration
-Talk to Customer Support

This module demonstrates how a traditional menu-driven IVR system works using API-based backend logic.

## Module 3 – Conversational AI Integration
This enhances the traditional IVR system by introducing conversational AI capabilities. Instead of only relying on keypad-based menu selection, the system can now understand natural voice commands from users.

#Features Implemented

-Speech-to-Text conversion for capturing voice input
-Text-to-Speech generation for system responses
-Intent recognition for identifying user requests
-Rule-based matching for command detection
-Regular expression processing
-Entity extraction (e.g., detecting PNR numbers)
-Conversational dialogue flow integrated with the existing IVR logic

#Technologies Used : 
Python,
FastAPI,
SpeechRecognition library.
Pyttsx3 for text-to-speech,
Regular Expressions (Regex) for entity extraction.

#Example Conversational Flow

User:
|
Check my PNR status
|
System:
|
Please provide your 10-digit PNR number.

This module demonstrates how traditional IVR systems can be modernized using conversational AI to enable natural voice interaction instead of only keypad input.

# Milestone 4 – Testing, Deployment and Monitoring

## Objective
The fourth milestone focused on validating the complete IRCTC Smart IVR system through different levels of testing, deploying the application to a production-like cloud environment, and monitoring the system after deployment.

---

## Work Completed in Milestone 4

### 1. Full-Cycle Testing
The system was tested using four major testing layers:

#### Unit Testing
Individual backend endpoints and IVR functionalities were tested separately to verify correctness.

Tested modules included:
- Login page loading
- IVR UI loading
- Welcome prompt generation
- PNR status response
- Train schedule response
- Booking status response
- Complaint status response
- Cancellation status response
- Refund status response
- Invalid input handling

#### Integration Testing
Integration testing was performed to ensure smooth interaction between:
- Frontend UI
- FastAPI backend
- Structured IVR data logic

Example flows tested:
- Press 1 → Enter PNR → Receive PNR details
- Press 4 → Enter Complaint ID → Receive complaint status
- Press 6 → Enter Refund ID → Receive refund status

#### End-to-End (E2E) Testing
End-to-end testing was performed to validate the complete user journey from:
- Login page access
- IVR dashboard opening
- Welcome menu generation
- User option selection
- Final result display

This confirmed that the complete simulated IVR call flow worked correctly in browser-based interaction.

#### Performance Testing
Basic performance testing was conducted by sending multiple requests to the IVR backend in a loop to verify:
- response consistency
- system stability
- acceptable response time under repeated requests

---

### 2. Deployment
The project was successfully deployed on a free cloud hosting platform (**Render**) to simulate a production-ready deployment environment.

#### Deployed Project Link
👉 **[Open Live IVR Project Here] (https://conversational-irctc-ivr.onrender.com/)**


## Sample Test Inputs

Use the following sample inputs to test the deployed IVR system:

### Login
- Username: `admin`
- Password: `1234`

### PNR Status
- `1234567890`
- `9876543210`

### Train Schedule
- `12952`
- `12627`

### Complaint Status
- `cmp101`
- `cmp202`

### Cancellation Status
- `can111`
- `can222`

### Refund Status
- `ref555`
- `ref777`

