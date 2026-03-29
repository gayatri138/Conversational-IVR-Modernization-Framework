import time
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# =====================================================
# 1) UNIT TESTS
# =====================================================

def test_login_page_loads():
    response = client.get("/")
    assert response.status_code == 200
    assert "IRCTC Smart IVR Login" in response.text


def test_ivr_ui_page_loads():
    response = client.get("/ivr-ui")
    assert response.status_code == 200
    assert "IRCTC" in response.text


def test_welcome_menu():
    response = client.get("/welcome")
    assert response.status_code == 200
    data = response.json()
    assert "Press 1 for PNR Status" in data["text"]
    assert "Press or say 1 for PNR status" in data["speech"]


def test_pnr_prompt():
    response = client.post("/ivr", json={"message": "1"})
    assert response.status_code == 200
    data = response.json()
    assert "Please enter your 10 digit PNR number" in data["text"]


def test_valid_pnr_status():
    response = client.post("/ivr", json={"message": "1234567890"})
    assert response.status_code == 200
    data = response.json()
    assert "PNR Status: Confirmed" in data["text"]
    assert "Mumbai Rajdhani Express" in data["text"]


def test_train_schedule_prompt():
    response = client.post("/ivr", json={"message": "2"})
    assert response.status_code == 200
    data = response.json()
    assert "Please enter your train number" in data["text"]


def test_valid_train_schedule():
    response = client.post("/ivr", json={"message": "12952"})
    assert response.status_code == 200
    data = response.json()
    assert "Mumbai Rajdhani Express" in data["text"]
    assert "Platform: 5" in data["text"]


def test_booking_status():
    response = client.post("/ivr", json={"message": "3"})
    assert response.status_code == 200
    data = response.json()
    assert "Booking Status: Booked Successfully" in data["text"]


def test_complaint_prompt():
    response = client.post("/ivr", json={"message": "4"})
    assert response.status_code == 200
    data = response.json()
    assert "Please enter your complaint ID" in data["text"]


def test_valid_complaint_status():
    response = client.post("/ivr", json={"message": "cmp202"})
    assert response.status_code == 200
    data = response.json()
    assert "Complaint Status: Resolved" in data["text"]


def test_cancellation_prompt():
    response = client.post("/ivr", json={"message": "5"})
    assert response.status_code == 200
    data = response.json()
    assert "Please enter your cancellation request ID" in data["text"]


def test_valid_cancellation_status():
    response = client.post("/ivr", json={"message": "can111"})
    assert response.status_code == 200
    data = response.json()
    assert "Cancellation Status: Cancelled Successfully" in data["text"]


def test_refund_prompt():
    response = client.post("/ivr", json={"message": "6"})
    assert response.status_code == 200
    data = response.json()
    assert "Please enter your refund reference ID" in data["text"]


def test_valid_refund_status():
    response = client.post("/ivr", json={"message": "ref555"})
    assert response.status_code == 200
    data = response.json()
    assert "Refund Status: Refund Processed" in data["text"]


def test_repeat_menu():
    response = client.post("/ivr", json={"message": "7"})
    assert response.status_code == 200
    data = response.json()
    assert "Press 1 for PNR Status" in data["text"]


def test_invalid_input():
    response = client.post("/ivr", json={"message": "999"})
    assert response.status_code == 200
    data = response.json()
    assert "Invalid Input" in data["text"]


# =====================================================
# 2) INTEGRATION TESTS
# =====================================================

def test_pnr_full_flow():
    step1 = client.post("/ivr", json={"message": "1"})
    assert step1.status_code == 200
    assert "Please enter your 10 digit PNR number" in step1.json()["text"]

    step2 = client.post("/ivr", json={"message": "1234567890"})
    assert step2.status_code == 200
    assert "PNR Status: Confirmed" in step2.json()["text"]


def test_complaint_full_flow():
    step1 = client.post("/ivr", json={"message": "4"})
    assert step1.status_code == 200
    assert "Please enter your complaint ID" in step1.json()["text"]

    step2 = client.post("/ivr", json={"message": "cmp101"})
    assert step2.status_code == 200
    assert "Complaint Status: Under Review" in step2.json()["text"]


def test_refund_full_flow():
    step1 = client.post("/ivr", json={"message": "6"})
    assert step1.status_code == 200
    assert "Please enter your refund reference ID" in step1.json()["text"]

    step2 = client.post("/ivr", json={"message": "ref777"})
    assert step2.status_code == 200
    assert "Refund Status: Refund In Progress" in step2.json()["text"]


# =====================================================
# 3) END-TO-END (E2E) TEST
# =====================================================

def test_full_ivr_flow():
    login_page = client.get("/")
    assert login_page.status_code == 200
    assert "IRCTC Smart IVR Login" in login_page.text

    ivr_page = client.get("/ivr-ui")
    assert ivr_page.status_code == 200

    welcome = client.get("/welcome")
    assert welcome.status_code == 200
    assert "Press 1 for PNR Status" in welcome.json()["text"]

    menu = client.post("/ivr", json={"message": "2"})
    assert menu.status_code == 200
    assert "Please enter your train number" in menu.json()["text"]

    result = client.post("/ivr", json={"message": "12627"})
    assert result.status_code == 200
    assert "Karnataka Express" in result.json()["text"]


# =====================================================
# 4) PERFORMANCE TEST
# =====================================================

def test_multiple_requests_performance():
    start_time = time.time()

    for _ in range(50):
        response = client.post("/ivr", json={"message": "1"})
        assert response.status_code == 200

    end_time = time.time()
    total_time = end_time - start_time

    assert total_time < 5