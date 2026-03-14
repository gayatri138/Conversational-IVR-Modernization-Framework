import re

def detect_intent(text):

    text = text.lower()

    if "pnr" in text:
        return "pnr_status"

    if "train" in text and "availability" in text:
        return "train_availability"

    if "book" in text:
        return "ticket_booking"

    if "cancel" in text:
        return "ticket_cancellation"

    if "refund" in text:
        return "refund_status"

    if "complaint" in text:
        return "complaint"

    if "agent" in text:
        return "agent"

    return "unknown"


def extract_pnr(text):

    match = re.search(r"\d{10}", text)

    if match:
        return match.group()

    return None