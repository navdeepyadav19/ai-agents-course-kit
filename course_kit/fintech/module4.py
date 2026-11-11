"""Module 4 practice material: the agent's rules, the questions, tasks to sort, vague and clear tool menus, a failed call and a stuck tool."""
from course_kit import tool

# The instructions the agent starts from in this module, and three questions.
AGENT_RULES = ("You are the collections assistant for Acme Software. Use the tools to look things up; "
               "never invent invoice or customer details. Keep answers short.")
TOOL_QUESTION = "Which invoices are unpaid?"
NO_TOOL_QUESTION = "In one sentence, what does 'overdue' mean?"
MULTI_STEP_QUESTION = ("Find the largest unpaid invoice, tell me who owes it and their email, "
                       "and create a payment link for it.")

# Topic 4.1: eight tasks to sort into: code, one model call, workflow, agent.
TASKS = [
    ('Add a 1.5% late fee to an invoice that is 30 days overdue.',
     'code', 'A fixed rule and arithmetic. Code is exact, free and instant.'),
    ('Send the reminder email on day 1, 7, 14 and 30.',
     'code', 'A schedule never changes its mind. No model needed.'),
    ("Sort a customer's reply into promise to pay, dispute or hardship.",
     'one model call', "Reading messy language is the model's job, and one call does it (Module 2)."),
    ('Rewrite a stiff reminder so it sounds polite but firm.',
     'one model call', 'One input, one output, no lookups.'),
    ('Read a reply, pull out the promised date, then save it to the invoice.',
     'workflow', 'Two fixed steps: the model extracts, code saves. The order never changes.'),
    ('Answer a policy question from the billing documents, with a source.',
     'workflow', 'Retrieve, then answer: the same steps every time (Module 3).'),
    ("'I can't pay all of it, what can we do?' Look up the invoice, check the policy, propose a plan, create the link.",
     'agent', 'The next step depends on what each lookup returns.'),
    ('Work out why INV-1044 is still unpaid and take the next sensible step.',
     'agent', 'Open-ended: nobody can list the steps in advance.'),
]

# Topic 4.3: the same two tools, described badly and described well.
VAGUE_TOOLS = [
    tool("invoice_search", "Search invoices.", value="number"),
    tool("invoice_lookup", "Look up invoices.", id="string"),
]
CLEAR_TOOLS = [
    tool("get_unpaid_invoices", "List unpaid invoices of at least min_amount dollars. Use 0 to list them all.", min_amount="number"),
    tool("get_invoices_for_customer", "List every invoice, paid and unpaid, for ONE customer ID such as C-101. Not for finding who owes money.", customer_id="string"),
]
DESIGN_QUESTIONS = [TOOL_QUESTION, 'Show me every invoice for customer C-102.']

# Topic 4.3: a tool call that failed, and two ways the tool could report it.
RECOVER_QUESTION = "What is Dana Lee's email?"
BAD_CALL = {"name": 'get_customer', "inputs": {"customer_id": "Dana Lee"}}
UNHELPFUL_ERROR = 'Error: not found.'
HELPFUL_ERROR = "No customer with ID 'Dana Lee'. customer_id looks like C-101, not a name. Known IDs: C-101, C-102, C-103."

# Topic 4.4: a tool that never gives a final answer, to show a runaway loop.
STUCK_TOOL = tool('check_payment_status', 'Check whether the payment for an invoice has cleared, for example INV-1042.', invoice_id="string")
STUCK_QUESTION = 'The customer says they paid INV-1042 a minute ago. Keep checking the payment status until it is final, then tell me the result.'
