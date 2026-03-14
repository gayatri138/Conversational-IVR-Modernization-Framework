# Conversational-IVR-Modernization-Framework
## Module 1 – Legacy System Analysis

This repository contains documentation related to:
- Traditional VXML-Based IVR Architecture (IRCTC Use Case)
- Integration with ACS and BAP
- Technical Challenges and Compatibility Gaps
- System Constraints and Modernization Requirements

## Milestone 2 – IVR System Implementation
This milestone focuses on implementing a basic IVR system using a web-based simulator. The goal was to replicate a traditional IVR workflow similar to the IRCTC customer care system and demonstrate menu-driven interaction using API endpoints.

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

This milestone demonstrates how a traditional menu-driven IVR system works using API-based backend logic.

## Milestone 3 – Conversational AI Integration
This milestone enhances the traditional IVR system by introducing conversational AI capabilities. Instead of only relying on keypad-based menu selection, the system can now understand natural voice commands from users.

#Features Implemented

-Speech-to-Text conversion for capturing voice input
-Text-to-Speech generation for system responses
-Intent recognition for identifying user requests
-Rule-based matching for command detection
-Regular expression processing
-Entity extraction (e.g., detecting PNR numbers)
-Conversational dialogue flow integrated with the existing IVR logic

#Technologies Used : 
Python
FastAPI
SpeechRecognition library
Pyttsx3 for text-to-speech
Regular Expressions (Regex) for entity extraction

#Example Conversational Flow

User:
|
Check my PNR status
|
System:
|
Please provide your 10-digit PNR number.

This milestone demonstrates how traditional IVR systems can be modernized using conversational AI to enable natural voice interaction instead of only keypad input.
