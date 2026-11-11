"""Fintech: Acme Software, the made-up company used in every module.

Its rules, a tiny fake database, and the tools that read and change it. Everything is invented for teaching.
You wrote the first three tools yourself in Module 4; from Module 5 on they are imported from here.
"""
COMPANY = "Acme Software"
RULES = "Be polite. Never threaten the customer. Only a manager can waive fees or balances."
FACTS = "Dana Lee owes $1,250 on invoice INV-1042, due 2026-09-30. Nothing has been waived."

# ---- A tiny fake database (Module 4). In Module 7 this becomes a real database and Stripe. ----
CUSTOMERS = {
    "C-101": {"name": "Dana Lee", "email": "dana@example.com"},
    "C-102": {"name": "Omar Haddad", "email": "omar@example.com"},
    "C-103": {"name": "Mei Tan", "email": "mei@example.com"},
}
INVOICES = [
    {"id": "INV-1042", "customer_id": "C-101", "amount": 1250.00, "due": "2026-09-30", "status": "unpaid"},
    {"id": "INV-1043", "customer_id": "C-102", "amount": 480.00, "due": "2026-10-15", "status": "unpaid"},
    {"id": "INV-1044", "customer_id": "C-103", "amount": 2100.00, "due": "2026-08-31", "status": "unpaid"},
    {"id": "INV-1045", "customer_id": "C-102", "amount": 300.00, "due": "2026-09-01", "status": "paid"},
]
DISPUTES = []   # disputes opened so far (Module 5)


# ---- The tools: ordinary Python functions. The docstring tells the model what each one does. ----
def get_unpaid_invoices(min_amount: float) -> list:
    """List unpaid invoices of at least min_amount dollars. Use 0 to list them all."""
    return [inv for inv in INVOICES if inv["status"] == "unpaid" and inv["amount"] >= min_amount]


def get_customer(customer_id: str) -> dict:
    """Look up a customer's name and email by customer ID, for example C-101."""
    return CUSTOMERS.get(customer_id, {"error": f"No customer {customer_id}"})


def create_payment_link(invoice_id: str) -> dict:
    """Create a payment link for an unpaid invoice, for example INV-1042."""
    return {"invoice_id": invoice_id, "url": f"https://pay.example.com/{invoice_id}"}


def get_invoice(invoice_id: str) -> dict:
    """Look up one invoice by its ID, for example INV-1042."""
    for inv in INVOICES:
        if inv["id"] == invoice_id:
            return inv
    return {"error": f"No invoice {invoice_id}"}


def open_dispute(invoice_id: str, reason: str) -> dict:
    """Open a dispute on an invoice. Reminders stop while it's reviewed."""
    DISPUTES.append({"invoice_id": invoice_id, "reason": reason})
    return {"dispute_opened": True, "invoice_id": invoice_id}


def reset_data():
    """Undo what the write tools changed, so every demo starts from the same data."""
    DISPUTES.clear()


def describe():
    """Print the company, its rules and its data, so you know what the notebook has loaded."""
    print(COMPANY)
    print("Rules:", RULES)
    print("Facts:", FACTS)
    print(len(CUSTOMERS), "customers and", len(INVOICES), "invoices, for example:", INVOICES[0])
