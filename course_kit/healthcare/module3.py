"""Module 3 practice material: four policy documents, test questions with the file that answers each, and a few tricky cases."""
import os


# Four short clinic documents. A blank line separates paragraphs.
DOCS = {
    "locations.md": """# Locations and hours

Downtown clinic: 200 Main Street. Open Monday to Friday, 8am to 6pm. Parking is in the garage on 2nd Street, free for 2 hours with validation.

Northside clinic: 45 Oak Avenue. Open Monday to Saturday, 9am to 5pm. Free parking at the front.""",

    "practitioners.md": """# Our practitioners

Dr. Maya Patel, cardiology, sees patients at Downtown on Mondays, Wednesdays and Fridays.

Dr. Leo Chen, family medicine, works at both locations.

Sam Ortiz, nurse practitioner, family medicine, works at Northside only.

Dr. Grace Kim, pediatrics, sees children at Downtown on Tuesdays and Thursdays.""",

    "prices.md": """# Self-pay prices

New-patient visit: $180. Follow-up visit: $120. ECG heart test: $95.

For insured patients, your insurer decides the final amount.

Payment is taken at check-in by card or cash.""",

    "visit-prep.md": """# Preparing for your visit

Please bring a photo ID, your insurance card and a list of your current medicines. Arrive 15 minutes early for your first visit.

To cancel or move an appointment, give at least 24 hours' notice. Missed appointments without notice are charged a $40 no-show fee.

If you have chest pain, trouble breathing or another emergency, call 911. Do not book an appointment.""",
}

def save_docs(folder="docs"):
    """Write every document into a folder, one file each, the way documents arrive in a real project."""
    os.makedirs(folder, exist_ok=True)
    for filename, text in DOCS.items():
        with open(f"{folder}/{filename}", "w") as file:
            file.write(text)

# Three sentences to compare in Cell 6: the question and the close one share no key words.
SIM_QUESTION = "How much does it cost if I don't show up?"
SIM_CLOSE = "Missed appointments without notice are charged a $40 no-show fee."
SIM_FAR = "Free parking at the front."

# Test questions with the file that holds each answer (Topic 3.6).
TEST_QUESTIONS = [
    ("Is Northside open on Saturday?", "locations.md"),
    ("Where do I park at the Downtown clinic?", "locations.md"),
    ("Which days does Dr. Patel see patients?", "practitioners.md"),
    ("Do you have a doctor for children?", "practitioners.md"),
    ("How much is an ECG?", "prices.md"),
    ("When do I pay for my visit?", "prices.md"),
    ("What should I bring to my first appointment?", "visit-prep.md"),
    ("Is there a fee if I cancel late?", "visit-prep.md"),
]

# A question the documents don't answer (Topic 3.5).
OUT_OF_SCOPE = "Do you offer dental cleanings?"

# Topic 3.4: a question where one exact word matters.
EXACT_QUESTION = "How much is an ECG?"
EXACT_WORD = "ECG"

# Topic 3.5: an old, replaced document that disagrees with a current one.
OLD_DOC_NAME = "prices-2024.md"
OLD_DOC_TEXT = "# Self-pay prices (2024 version, replaced)\n\nNew-patient visit: $150. Follow-up visit: $90."
CONFLICT_QUESTION = "How much is a new-patient visit?"

# Topic 3.6: two more questions make a 10-question test set, and each has a key fact a good answer must contain.
TEST_QUESTIONS += [
    ('How early should I arrive for my first visit?', 'visit-prep.md'),
    ('How much is a follow-up visit?', 'prices.md'),
]
ANSWER_KEYS = ['Saturday', 'garage', 'Monday', 'Kim', '95', 'check-in', 'photo ID', '40', '15 minutes', '120']
