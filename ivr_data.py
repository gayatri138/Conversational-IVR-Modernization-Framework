railway_data = {
    "pnr": {
        "1234567890": {
            "train_number": "12952",
            "train_name": "Mumbai Rajdhani Express",
            "from": "New Delhi",
            "to": "Mumbai Central",
            "date": "12 April 2026",
            "departure_time": "16:55",
            "status": "Confirmed"
        },
        "9876543210": {
            "train_number": "12627",
            "train_name": "Karnataka Express",
            "from": "New Delhi",
            "to": "Bengaluru",
            "date": "15 April 2026",
            "departure_time": "20:00",
            "status": "Waiting List 12"
        }
    },

    "train_schedule": {
        "12952": {
            "train_name": "Mumbai Rajdhani Express",
            "from": "New Delhi",
            "to": "Mumbai Central",
            "departure": "16:55",
            "arrival": "08:35",
            "platform": "5"
        },
        "12627": {
            "train_name": "Karnataka Express",
            "from": "New Delhi",
            "to": "Bengaluru",
            "departure": "20:00",
            "arrival": "06:40",
            "platform": "3"
        }
    },

    "booking": {
        "book123": {
            "route": "Delhi to Lucknow",
            "date": "18 April 2026",
            "class": "3AC",
            "status": "Booked Successfully"
        }
    },

    "complaints": {
        "cmp101": {
            "issue": "Train Delay",
            "status": "Under Review",
            "registered_date": "10 April 2026",
            "expected_resolution": "Within 24 Hours"
        },
        "cmp202": {
            "issue": "Ticket Booking Failure",
            "status": "Resolved",
            "registered_date": "08 April 2026",
            "expected_resolution": "Completed"
        }
    },

    "cancellation": {
        "can111": {
            "pnr": "1234567890",
            "status": "Cancelled Successfully",
            "refund_amount": "850 Rupees",
            "processed_date": "11 April 2026"
        },
        "can222": {
            "pnr": "9876543210",
            "status": "Cancellation Pending",
            "refund_amount": "0 Rupees",
            "processed_date": "In Progress"
        }
    },

    "refund": {
        "ref555": {
            "pnr": "1234567890",
            "refund_status": "Refund Processed",
            "amount": "850 Rupees",
            "credited_date": "13 April 2026"
        },
        "ref777": {
            "pnr": "9876543210",
            "refund_status": "Refund In Progress",
            "amount": "620 Rupees",
            "credited_date": "Expected in 3 Working Days"
        }
    }
}