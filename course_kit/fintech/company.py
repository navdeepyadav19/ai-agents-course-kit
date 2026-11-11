"""Fintech: the company. Its rules, data, tools and specialists. Shared by every module."""
COMPANY = "Acme Software"
RULES = "Be polite. Never threaten the customer. Only a manager can waive fees or balances."
FACTS = "Dana Lee owes $1,250 on invoice INV-1042, due 2026-09-30. Nothing has been waived."

AGENT_RULES = ("You are an assistant for Acme Software's billing team. Be polite and brief. Never threaten. "
               "Facts: Dana Lee (customer C-101) owes $1,250 on INV-1042, due 2026-09-30. "
               "Late fee: 1.5% a month after 30 days overdue. Plans: up to 3 monthly payments on balances over $500. "
               "Only a manager can waive fees.")

INVOICES = {"INV-1042": {"customer_id": "C-101", "amount": 1250.00, "status": "unpaid"},
            "INV-1044": {"customer_id": "C-103", "amount": 2100.00, "status": "unpaid"}}
DISPUTES = []

def get_invoice(invoice_id: str) -> dict:
    """Look up an invoice by ID, for example INV-1042."""
    return INVOICES.get(invoice_id, {"error": f"No invoice {invoice_id}"})

def create_payment_link(invoice_id: str) -> dict:
    """Create a payment link for an unpaid invoice."""
    return {"invoice_id": invoice_id, "url": f"https://pay.example.com/{invoice_id}"}

def open_dispute(invoice_id: str, reason: str) -> dict:
    """Open a dispute on an invoice. Reminders stop while it's reviewed."""
    DISPUTES.append({"invoice_id": invoice_id, "reason": reason})
    return {"dispute_opened": True, "invoice_id": invoice_id}

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


def reset_data():
    """Undo what the write tool changed, so every demo starts from the same data."""
    DISPUTES.clear()   # forget every dispute opened so far


def describe():
    """Print the company and its rules, so you know what the notebook has loaded."""
    print(COMPANY)
    print("Rules:", RULES)
    print("Facts:", FACTS)


def describe_team():
    """Print the ready-made specialists and the tools each one owns (Module 5)."""
    for s in SPECIALISTS:
        print(f"{s['name']}: handles {s['handles']} | tools: {', '.join(f.__name__ for f in s['tools'])}")
