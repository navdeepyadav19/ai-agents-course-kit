"""Healthcare: the company. Its rules, data, tools and specialists. Shared by every module."""
COMPANY = "Riverside Family Clinic"
RULES = "Be kind. Never give medical advice. Only the billing office can give discounts."
FACTS = "Self-pay prices: new-patient visit $180, follow-up visit $120. No discounts are active."

AGENT_RULES = ("You are an assistant for Riverside Family Clinic. Be kind and brief. Never give medical advice; "
               "for chest pain or trouble breathing, tell them to call 911. Facts: Dr. Maya Patel, cardiology, "
               "Downtown. Dr. Leo Chen, family medicine, Downtown and Northside. Self-pay: new visit $180, "
               "follow-up $120, ECG $95. No-show fee $40 without 24 hours' notice.")

SLOTS = [{"id": "S-1", "practitioner": "Dr. Maya Patel", "time": "2026-11-02 09:00", "patient": None},
         {"id": "S-3", "practitioner": "Dr. Leo Chen", "time": "2026-11-03 10:30", "patient": None}]
PRICES = {"new visit": 180, "follow-up": 120, "ECG": 95}

def get_open_slots(practitioner: str) -> list:
    """List open slots for a practitioner by full name, e.g. Dr. Maya Patel."""
    return [s for s in SLOTS if s["practitioner"] == practitioner and s["patient"] is None]

def book_appointment(slot_id: str, patient_name: str) -> dict:
    """Book an open slot (e.g. S-1) for a patient."""
    for slot in SLOTS:
        if slot["id"] == slot_id and slot["patient"] is None:
            slot["patient"] = patient_name
            return {"booked": True, "slot": slot}
    return {"booked": False, "error": f"Slot {slot_id} isn't open"}

def get_price(service: str) -> dict:
    """Self-pay price for a service: new visit, follow-up or ECG."""
    return {"service": service, "price": PRICES.get(service, "unknown")}

# Two specialists. "handles" is what the triage agent reads to choose between them.
SPECIALISTS = [
    {"name": "Booking specialist", "handles": "booking, moving or canceling appointments",
     "instructions": AGENT_RULES + " You book appointments. Use the tools.",
     "tools": [get_open_slots, book_appointment]},
    {"name": "Billing specialist", "handles": "prices and what a visit costs",
     "instructions": AGENT_RULES + " You answer price questions. Say the insurer decides the final amount for insured patients.",
     "tools": [get_price]},
]
TRIAGE_RULES = "You greet the patient and hand them to the right specialist. Don't answer booking or price questions yourself."


def reset_data():
    """Undo what the write tool changed, so every demo starts from the same data."""
    for slot in SLOTS: slot["patient"] = None   # free every booked slot


def describe():
    """Print the company and its rules, so you know what the notebook has loaded."""
    print(COMPANY)
    print("Rules:", RULES)
    print("Facts:", FACTS)


def describe_team():
    """Print the ready-made specialists and the tools each one owns (Module 5)."""
    for s in SPECIALISTS:
        print(f"{s['name']}: handles {s['handles']} | tools: {', '.join(f.__name__ for f in s['tools'])}")
