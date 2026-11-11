"""Healthcare: one made-up company for the whole course. Its rules, data, tools and test messages.
Everything here is invented for teaching. Notebooks load it with: from course_kit.healthcare import *"""
COMPANY = "Riverside Family Clinic"
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
HANDOFF_QUESTIONS = ["Can I book the first open slot with Dr. Patel? My name is Sam Rivera.",
                     "How much is an ECG if I pay myself?"]

# Memory demo (Topic 5.3): the same patient in two separate conversations.
CUSTOMER_ID = "P-2001"
MEMORY_FIRST = "Hi, this is Sam Rivera, patient P-2001. I can only come in on mornings, and I prefer the Downtown clinic."
MEMORY_LATER = "It's Sam, patient P-2001, again. When and where would suit me for my next visit?"

# Routing demo (Topic 5.4).
EASY_QUESTION = "How much is a follow-up visit if I pay myself?"
HARD_QUESTION = ("I'm a new self-pay patient. If I book a new visit plus an ECG, then miss a follow-up without notice, "
                 "what's my total, and which charges could my insurer cover if I add insurance later?")

def reset_data():
    """Undo what the write tool changed, so every demo starts from the same data."""
    for slot in SLOTS: slot["patient"] = None   # free every booked slot

# Topic 5.1: six messages and the agent that should end up answering each one.
ROUTE_MESSAGES = [
    ('Can I book the first open slot with Dr. Patel? My name is Sam Rivera.', 'Booking specialist'),
    ('Does Dr. Leo Chen have anything open this week?', 'Booking specialist'),
    ('I need to see Dr. Chen, my name is Ana Gomez. Any slot is fine.', 'Booking specialist'),
    ('How much is an ECG if I pay myself?', 'Billing specialist'),
    ('What does a first visit cost without insurance?', 'Billing specialist'),
    ('Can you tell me if this rash looks serious?', 'Triage'),
]

# Topic 5.2: a two-message conversation. The detail the specialist needs is in the FIRST message.
LOST_DETAIL_TURNS = ["Hi, my name is Sam Rivera and I'd like to see Dr. Maya Patel.",
                     'Please book me her first open slot.']
BOTH_QUESTION = "How much is a new visit, and can you book me the first open slot with Dr. Leo Chen? I'm Ana Gomez."   # needs both specialists

# Topic 5.3: the same patient later changes a preference, then shares something we must not keep.
MEMORY_CHANGE = "It's Sam, patient P-2001. I've changed shifts: afternoons suit me now, not mornings."
MEMORY_PRIVATE = "Sam again, P-2001. Please remind me by text message. My card ends in 4421, and my employer mustn't know about my heart condition."
NEVER_REMEMBER = ['card', 'cvv', 'password', 'employer', 'condition', 'diagnos']   # parts of words that mark a detail we must never store

# Topic 5.4: six questions and the model each one deserves. Words that mean "the stakes are high".
ROUTER_QUESTIONS = [
    ('How much is a follow-up visit if I pay myself?', 'small'),
    ('Which doctor does cardiology?', 'small'),
    ('What is the no-show fee?', 'small'),
    (HARD_QUESTION, 'strong'),
    ('I want to make a complaint: I was charged a no-show fee but I did call the day before.', 'strong'),
    ('Does Dr. Chen work at Northside?', 'small'),
]
HIGH_STAKES_WORDS = ['complaint', 'lawyer', 'legal', 'refund', 'appeal']

# Topic 5.5: what the patient sees when no model can answer.
BROKEN_MODEL = "model-that-is-down"        # a model name that doesn't exist, to fake an outage
SAFE_REPLIES = {                           # fixed answers a person approved in advance, for exact common questions
    'how much is': 'Self-pay prices: a new visit is $180, a follow-up $120 and an ECG $95.',
    'how do i book': 'You can book by calling the front desk on 555-0100, 8am to 5pm on weekdays.',
}
DEGRADE_QUESTION = 'How much is an ECG?'
HUMAN_MESSAGE = "Sorry, we can't answer right now. Your message is with our front desk, who will call you back today. If this is an emergency, call 911."


def describe():
    """Print what this file gives you, so you know what the notebook can use."""
    print(COMPANY)
    print("Rules:", AGENT_RULES[:110] + "...")
    for s in SPECIALISTS:
        print(f"  {s['name']}: handles {s['handles']} | tools: {', '.join(f.__name__ for f in s['tools'])}")
    print("Test messages:", len(ROUTE_MESSAGES), "to route,", len(ROUTER_QUESTIONS), "to send to a model")
