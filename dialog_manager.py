def generate_response(intent):

    if intent == "pnr_status":
        return "Please tell your ten digit PNR number"

    if intent == "train_availability":
        return "Please tell the train number"

    if intent == "ticket_booking":
        return "Ticket booking service selected"

    if intent == "ticket_cancellation":
        return "Ticket cancellation selected"

    if intent == "refund_status":
        return "Checking refund status"

    if intent == "complaint":
        return "Please describe your complaint"

    if intent == "agent":
        return "Connecting to customer care agent"

    return "Sorry I did not understand your request"