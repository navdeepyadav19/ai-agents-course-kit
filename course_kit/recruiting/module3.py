"""Module 3 practice material: four policy documents, test questions with the file that answers each, and a few tricky cases."""
import os


# Four short hiring documents. A blank line separates paragraphs.
DOCS = {
    "role-csm.md": """# Customer Success Manager

This role is fully remote, open to candidates in the US only. The salary range is $75,000 to $90,000.

You'll need 3+ years in customer success or account management, experience with a CRM such as Salesforce or HubSpot, and clear written communication.""",

    "interview-process.md": """# Interview process

Step 1 is a 30-minute phone screen with a recruiter. Step 2 is a 60-minute panel interview with the team.

The whole process usually takes 2 to 3 weeks. We give feedback within 5 business days of each step.""",

    "benefits.md": """# Benefits

Health, dental and vision insurance from day one. 20 days of paid leave plus public holidays.

401(k) with a 4% company match. A $1,000 yearly learning budget and a $500 home-office allowance.""",

    "accommodations.md": """# Interview accommodations

We're happy to adjust any interview, for example with captions, extra time or a written format.

Email accommodations@brightline.example to ask. Asking never affects our hiring decision.""",
}

def save_docs(folder="docs"):
    """Write every document into a folder, one file each, the way documents arrive in a real project."""
    os.makedirs(folder, exist_ok=True)
    for filename, text in DOCS.items():
        with open(f"{folder}/{filename}", "w") as file:
            file.write(text)

# Three sentences to compare in Cell 6: the question and the close one share no key words.
SIM_QUESTION = "How much will I be paid?"
SIM_CLOSE = "The salary range is $75,000 to $90,000."
SIM_FAR = "Step 2 is a 60-minute panel interview with the team."

# Test questions with the file that holds each answer (Topic 3.6).
TEST_QUESTIONS = [
    ("What's the salary for this job?", "role-csm.md"),
    ("Can I apply from Canada?", "role-csm.md"),
    ("What are the interview steps?", "interview-process.md"),
    ("When will I hear back after my interview?", "interview-process.md"),
    ("Is there a retirement plan?", "benefits.md"),
    ("Do you pay for courses or training?", "benefits.md"),
    ("Can I get captions during my video interview?", "accommodations.md"),
    ("Will asking for an adjustment hurt my chances?", "accommodations.md"),
]

# A question the documents don't answer (Topic 3.5).
OUT_OF_SCOPE = "Is there a signing bonus?"

# Topic 3.4: a question where one exact word matters.
EXACT_QUESTION = "Is there a 401(k)?"
EXACT_WORD = "401(k)"

# Topic 3.5: an old, replaced document that disagrees with a current one.
OLD_DOC_NAME = "benefits-2024.md"
OLD_DOC_TEXT = "# Benefits (2024 version, replaced)\n\n15 days of paid leave plus public holidays. 401(k) with a 2% company match."
CONFLICT_QUESTION = "How many days of paid leave do I get?"

# Topic 3.6: two more questions make a 10-question test set, and each has a key fact a good answer must contain.
TEST_QUESTIONS += [
    ('How many days of paid leave do I get?', 'benefits.md'),
    ('How long does the whole process take?', 'interview-process.md'),
]
ANSWER_KEYS = ['75,000', 'US', 'phone screen', '5 business days', '401(k)', '1,000', 'captions', 'never affects', '20 days', '2 to 3 weeks']
