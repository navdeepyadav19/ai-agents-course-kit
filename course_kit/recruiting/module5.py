"""Module 5 practice material: test messages for handoffs, memory, routing and fallbacks."""
HANDOFF_QUESTIONS = ["I'm candidate CAND-3. Can you book my panel interview for 2026-11-04 at 10:00?",
                     "What's the salary range for this role?"]

# Memory demo (Topic 5.3): the same candidate in two separate conversations.
CUSTOMER_ID = "CAND-3"
MEMORY_FIRST = "Hi, I'm Luis, candidate CAND-3. I can only interview after 3pm Eastern, and I prefer video calls."
MEMORY_LATER = "It's Luis, CAND-3, again. When and how should we schedule my panel interview?"

# Routing demo (Topic 5.4).
EASY_QUESTION = "Is this role remote?"
HARD_QUESTION = ("I'm in Toronto but could move to Seattle in six months, and I'd need the top of the salary range. "
                 "Can I apply now, and how should I raise salary without hurting my chances?")

# Topic 5.1: six messages and the agent that should end up answering each one.
ROUTE_MESSAGES = [
    ("I'm candidate CAND-3. Can you book my panel interview for 2026-11-04 at 10:00?", 'Scheduling specialist'),
    ("I'm CAND-3. Which stage am I at?", 'Scheduling specialist'),
    ('CAND-3 here: please book my interview for 2026-11-06 at 15:30.', 'Scheduling specialist'),
    ("What's the salary range for this role?", 'Role questions specialist'),
    ('Is the job remote, and what are the interview steps?', 'Role questions specialist'),
    ("Can you tell me why my friend's application was rejected?", 'Triage'),
]

# Topic 5.2: a two-message conversation. The detail the specialist needs is in the FIRST message.
LOST_DETAIL_TURNS = ["Hi, I'm Luis Ortega, candidate CAND-3, applying for the Customer Success Manager role.",
                     'Can you book my panel interview for 2026-11-04 at 10:00?']
BOTH_QUESTION = "I'm CAND-3. What's the salary range, and can you book my panel interview for 2026-11-04 at 10:00?"   # needs both specialists

# Topic 5.3: the same candidate later changes a preference, then shares something we must not keep.
MEMORY_CHANGE = "It's Luis, CAND-3. My schedule changed: mornings before 11am Eastern work best now."
MEMORY_PRIVATE = "Luis again, CAND-3. I can start on March 2. I should mention I'm 52 years old and my current salary is $68,000."
NEVER_REMEMBER = ['years old', 'current salary', 'pregnan', 'religio', 'disab', 'married']   # parts of words that mark a detail we must never store

# Topic 5.4: six questions and the model each one deserves. Words that mean "the stakes are high".
ROUTER_QUESTIONS = [
    ('Is this role remote?', 'small'),
    ("What's the salary range?", 'small'),
    ('How long until I hear back after an interview?', 'small'),
    (HARD_QUESTION, 'strong'),
    ('I think I was rejected because of my age. What can I do?', 'strong'),
    ('How long is the phone screen?', 'small'),
]
HIGH_STAKES_WORDS = ['discriminat', 'lawyer', 'legal', 'rejected', 'visa']

# Topic 5.5: what the candidate sees when no model can answer.
BROKEN_MODEL = "model-that-is-down"        # a model name that doesn't exist, to fake an outage
SAFE_REPLIES = {                           # fixed answers a person approved in advance, for exact common questions
    "what's the salary range": 'The salary range for the Customer Success Manager role is $75,000-$90,000.',
    'is this role remote': 'The role is remote, for people based in the US.',
}
DEGRADE_QUESTION = 'Is this role remote?'
HUMAN_MESSAGE = "Sorry, we can't answer right now. Your message is with our recruiting team, who will reply within one business day."
