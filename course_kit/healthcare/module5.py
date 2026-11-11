"""Module 5 practice material: the agent rules, two ready-made specialists, and test messages for handoffs, memory, routing and fallbacks."""
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
