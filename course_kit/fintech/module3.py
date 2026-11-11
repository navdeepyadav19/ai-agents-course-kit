"""Module 3 practice material: four policy documents, test questions with the file that answers each, and a few tricky cases."""
import os


# Four short policy documents. A blank line separates paragraphs.
DOCS = {
    "billing-policy.md": """# Billing policy

Invoices are issued on the 1st of each month and are due 30 days later.

Customers can pay by card, bank transfer or ACH, using the payment link in the invoice email.

A receipt is emailed as soon as a payment is received.""",

    "late-fees.md": """# Late fees and reminders

There is no late fee in the first 30 days after the due date. After that, a fee of 1.5% of the balance is added each month.

Only a billing manager can waive a late fee.

We send reminders 1, 7, 14 and 30 days after the due date, by email first and then by SMS.""",

    "payment-plans.md": """# Payment plans

Balances over $500 can be split into up to 3 monthly payments. The first payment is due within 7 days of agreeing the plan.

If a plan payment is missed, the plan is canceled and the full balance is due.

Customers in hardship can ask to pause payments for up to 60 days, with a billing manager's approval.""",

    "disputes.md": """# Disputes

Customers can dispute a charge within 60 days of the invoice date.

While a dispute is reviewed, all reminders and calls about that invoice stop.

Reviews take up to 10 business days. Refunds go back to the original payment method.""",
}

def save_docs(folder="docs"):
    """Write every document into a folder, one file each, the way documents arrive in a real project."""
    os.makedirs(folder, exist_ok=True)
    for filename, text in DOCS.items():
        with open(f"{folder}/{filename}", "w") as file:
            file.write(text)

# Three sentences to compare in Cell 6: the question and the close one share no key words.
SIM_QUESTION = "Is there a penalty if I pay late?"
SIM_CLOSE = "There is no late fee in the first 30 days after the due date."
SIM_FAR = "A receipt is emailed as soon as a payment is received."

# Test questions with the file that holds each answer (Topic 3.6).
TEST_QUESTIONS = [
    ("When is an invoice due?", "billing-policy.md"),
    ("Can I pay by bank transfer?", "billing-policy.md"),
    ("How much is the late fee?", "late-fees.md"),
    ("Who can waive a late fee?", "late-fees.md"),
    ("Can I split a $900 balance into installments?", "payment-plans.md"),
    ("What happens if I miss a plan payment?", "payment-plans.md"),
    ("How long do I have to dispute a charge?", "disputes.md"),
    ("Do reminders stop while a dispute is reviewed?", "disputes.md"),
]

# A question the documents don't answer (Topic 3.5).
OUT_OF_SCOPE = "Do you give a discount for paying a whole year in advance?"

# Topic 3.4: a question where one exact word matters.
EXACT_QUESTION = "Can I pay by ACH?"
EXACT_WORD = "ACH"

# Topic 3.5: an old, replaced document that disagrees with a current one.
OLD_DOC_NAME = "late-fees-2024.md"
OLD_DOC_TEXT = "# Late fees (2024 version, replaced)\n\nA late fee of 5% of the balance is added from the first day after the due date."
CONFLICT_QUESTION = "How much is the late fee?"

# Topic 3.6: two more questions make a 10-question test set, and each has a key fact a good answer must contain.
TEST_QUESTIONS += [
    ('How often do you send reminders?', 'late-fees.md'),
    ('How long does a dispute review take?', 'disputes.md'),
]
ANSWER_KEYS = ['30 days', 'bank transfer', '1.5%', 'billing manager', '3', 'canceled', '60 days', 'stop', '1, 7, 14 and 30', '10 business days']
