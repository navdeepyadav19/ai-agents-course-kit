"""Module 5 practice material: the agent rules, two ready-made specialists, and test messages for handoffs, memory, routing and fallbacks."""
from .company import *

# The instructions every agent in this module starts from.
AGENT_RULES = ("You are an assistant for Acme Software's billing team. Be polite and brief. Never threaten. "
               "Facts: Dana Lee (customer C-101) owes $1,250 on INV-1042, due 2026-09-30. "
               "Late fee: 1.5% a month after 30 days overdue. Plans: up to 3 monthly payments on balances over $500. "
               "Only a manager can waive fees.")

# Two specialists. "handles" is what the triage agent reads to choose between them.
SPECIALISTS = [
    {"name": "Billing specialist", "handles": "paying an invoice, payment links, balances",
     "instructions": AGENT_RULES + " You help customers pay. Use the tools.",
     "tools": [get_invoice, create_payment_link]},
    {"name": "Disputes specialist", "handles": "customers who say a charge is wrong",
     "instructions": AGENT_RULES + " You record disputes calmly and explain that reminders stop during review.",
     "tools": [get_invoice, open_dispute]},
]
TRIAGE_RULES = "You greet the customer and hand them to the right specialist. Don't answer billing questions yourself."


def describe_team():
    """Print the ready-made specialists and the tools each one owns."""
    for s in SPECIALISTS:
        print(f"{s['name']}: handles {s['handles']} | tools: {', '.join(f.__name__ for f in s['tools'])}")

HANDOFF_QUESTIONS = ["Can you send me a link to pay INV-1042?",
                     "INV-1042 is wrong, I canceled in August."]

# Memory demo (Topic 5.3): the same customer in two separate conversations.
CUSTOMER_ID = "C-101"
MEMORY_FIRST = "Hi, this is Dana, customer C-101. Please only contact me by email, I work nights."
MEMORY_LATER = "It's Dana again, customer C-101. How will you contact me about my invoice?"

# Routing demo (Topic 5.4).
EASY_QUESTION = "When was INV-1042 due?"
HARD_QUESTION = ("If Dana pays $400 now and splits the rest over the longest plan allowed, "
                 "what are the payments, and is any late fee due if her first plan payment is 45 days after the due date?")

# Topic 5.1: six messages and the agent that should end up answering each one.
ROUTE_MESSAGES = [
    ('Can you send me a link to pay INV-1042?', 'Billing specialist'),
    ('How much do I still owe on INV-1042?', 'Billing specialist'),
    ("I'd like to pay invoice INV-1044 today.", 'Billing specialist'),
    ('INV-1042 is wrong, I canceled in August.', 'Disputes specialist'),
    ('I was charged twice for the same month on INV-1044.', 'Disputes specialist'),
    ('Do you have any job openings in your billing team?', 'Triage'),
]

# Topic 5.2: a two-message conversation. The detail the specialist needs is in the FIRST message.
LOST_DETAIL_TURNS = ["Hi, I'm Dana Lee, customer C-101. I have a question about invoice INV-1042.",
                     "It's wrong: I canceled in August. Please open a dispute."]
BOTH_QUESTION = 'Send me a link to pay INV-1044, and open a dispute on INV-1042 because I canceled in August.'   # needs both specialists

# Topic 5.3: the same customer later changes a preference, then shares something we must not keep.
MEMORY_CHANGE = "It's Dana, customer C-101. I've changed jobs, so phone calls are fine now, any time after 6pm."
MEMORY_PRIVATE = "Dana again, C-101. I'll pay INV-1042 on the 28th. My card ends in 4421, and I was late because I was in hospital."
NEVER_REMEMBER = ['card', 'cvv', 'password', 'hospital', 'illness', 'diagnos']   # parts of words that mark a detail we must never store

# Topic 5.4: six questions and the model each one deserves. Words that mean "the stakes are high".
ROUTER_QUESTIONS = [
    ('When was INV-1042 due?', 'small'),
    ('How much does Dana owe on INV-1042?', 'small'),
    ('What is your late fee?', 'small'),
    (HARD_QUESTION, 'strong'),
    ("Can you waive my late fee just this once? I've been a customer for six years.", 'strong'),
    ("What's the longest payment plan you offer?", 'small'),
]
HIGH_STAKES_WORDS = ['waive', 'lawyer', 'legal', 'hardship', 'close my account']

# Topic 5.5: what the customer sees when no model can answer.
BROKEN_MODEL = "model-that-is-down"        # a model name that doesn't exist, to fake an outage
SAFE_REPLIES = {                           # fixed answers a person approved in advance, for exact common questions
    'what is your late fee': 'Our late fee is 1.5% a month once an invoice is 30 days overdue.',
    'how do i pay': 'You can pay any invoice at pay.example.com with your invoice number.',
}
DEGRADE_QUESTION = 'What is your late fee?'
HUMAN_MESSAGE = "Sorry, we can't answer right now. Your message is with our billing team, who will reply within one business day."
