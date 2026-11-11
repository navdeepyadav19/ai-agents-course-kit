"""HR & recruiting: the company. Its rules, data, tools and specialists. Shared by every module."""
COMPANY = "Brightline"
RULES = "Be warm and clear. Never make hiring decisions or offers. Never comment on protected traits."
FACTS = "Customer Success Manager, remote (US only), salary range $75,000-$90,000. Only hiring managers make offers."

AGENT_RULES = ("You are a recruiting assistant for Brightline. Be warm and clear. Never make hiring decisions or "
               "comment on protected traits. Facts: Customer Success Manager, remote (US only), $75,000-$90,000. "
               "Process: 30-minute phone screen, then a 60-minute panel. Feedback within 5 business days.")

CANDIDATES = {"CAND-3": {"name": "Luis Ortega", "stage": "phone screen"}}
INTERVIEWS = []
ROLE_INFO = {"salary": "$75,000-$90,000", "location": "remote, US only",
             "process": "30-minute phone screen, then a 60-minute panel"}

def get_candidate(candidate_id: str) -> dict:
    """Get a candidate's name and hiring stage, e.g. CAND-3."""
    return CANDIDATES.get(candidate_id, {"error": f"No candidate {candidate_id}"})

def book_interview(candidate_id: str, time: str) -> dict:
    """Book an interview for a candidate at a time like 2026-11-04 10:00."""
    INTERVIEWS.append({"candidate_id": candidate_id, "time": time})
    return {"booked": True, "candidate_id": candidate_id, "time": time}

def get_role_info(topic: str) -> dict:
    """Facts about the role: salary, location or process."""
    return {"topic": topic, "answer": ROLE_INFO.get(topic, "unknown")}

# Two specialists. "handles" is what the triage agent reads to choose between them.
SPECIALISTS = [
    {"name": "Scheduling specialist", "handles": "booking or moving interviews",
     "instructions": AGENT_RULES + " You schedule interviews. Use the tools.",
     "tools": [get_candidate, book_interview]},
    {"name": "Role questions specialist", "handles": "questions about the job, pay and process",
     "instructions": AGENT_RULES + " You answer questions about the role. Use the tools.",
     "tools": [get_role_info]},
]
TRIAGE_RULES = "You greet the candidate and hand them to the right specialist. Don't answer scheduling or role questions yourself."


def reset_data():
    """Undo what the write tool changed, so every demo starts from the same data."""
    INTERVIEWS.clear()   # cancel every booked interview


def describe():
    """Print the company and its rules, so you know what the notebook has loaded."""
    print(COMPANY)
    print("Rules:", RULES)
    print("Facts:", FACTS)


def describe_team():
    """Print the ready-made specialists and the tools each one owns (Module 5)."""
    for s in SPECIALISTS:
        print(f"{s['name']}: handles {s['handles']} | tools: {', '.join(f.__name__ for f in s['tools'])}")
