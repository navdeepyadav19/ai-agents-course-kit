"""Shared setup and small helpers for the AI Agents course notebooks.

Each helper was written out in full in the module that first taught it. From then on the notebooks
import it from here, so a cell can show only the new idea.
"""

MODEL = "gpt-6-luna"             # cheap and fast: the course's default
STRONG_MODEL = "gpt-6.1-terra"   # stronger and dearer: REPLACE with your provider's current larger model
PRICES = {MODEL: (0.10, 0.50), STRONG_MODEL: (1.00, 5.00)}   # dollars per 1M tokens (input, output). REPLACE with today's.

USAGE = []        # one row per ask(): (model, input tokens, output tokens)
_client = None


def connect():
    """Read OPENAI_API_KEY from Colab Secrets and return the client. Module 1, Cell 2 did this by hand."""
    global _client
    from google.colab import userdata
    from openai import OpenAI
    key = userdata.get("OPENAI_API_KEY")
    if not key:
        raise SystemExit("No OPENAI_API_KEY found. Click the key icon in Colab's left sidebar, add it, "
                         "and switch on 'Notebook access'.")
    try:   # the Agents SDK (Module 4 onward) uses the same key
        from agents import set_default_openai_key
        set_default_openai_key(key)
    except ImportError:
        pass
    _client = OpenAI(api_key=key)
    print("Connected. Default model:", MODEL, "| strong model:", STRONG_MODEL)
    return _client


def no_thinking():
    """Agents SDK settings with reasoning switched off, as in every module (Module 1, Topic 1.4)."""
    from agents import ModelSettings
    from openai.types.shared import Reasoning
    return ModelSettings(reasoning=Reasoning(effort="none"))


def ask(model, instructions, question, effort="none"):
    """One model call, as written out in Module 1. Returns the text and records the tokens in USAGE."""
    response = _client.responses.create(model=model, instructions=instructions, input=question,
                                        reasoning={"effort": effort})
    USAGE.append((model, response.usage.input_tokens, response.usage.output_tokens))
    return response.output_text


def cost(rows):
    """Dollars for a list of (model, input tokens, output tokens) rows, using PRICES (Module 1, Topic 1.2)."""
    return sum(t_in * PRICES[model][0] + t_out * PRICES[model][1] for model, t_in, t_out in rows) / 1_000_000


def show_steps(result):
    """Print every step of an Agents SDK run with the agent that took it (the trace table from Module 4)."""
    from agents import ItemHelpers
    for item in result.new_items:
        kind = type(item).__name__
        if kind == "HandoffCallItem":
            print(f"{item.agent.name:<26} asks to hand off: {item.raw_item.name}")
        elif kind == "HandoffOutputItem":
            print(f"{'':<26} handoff done: {item.source_agent.name} -> {item.target_agent.name}")
        elif kind == "ToolCallItem":
            print(f"{item.agent.name:<26} calls a tool: {item.raw_item.name}({item.raw_item.arguments})")
        elif kind == "ToolCallOutputItem":
            print(f"{item.agent.name:<26} tool result: {str(item.output)[:80]}")
        elif kind == "MessageOutputItem":
            print(f"{item.agent.name:<26} says: {ItemHelpers.text_message_output(item)[:80]}")


def customer_messages(history):
    """The customer's own messages inside a conversation history (a string or a list of items)."""
    if isinstance(history, str):
        return [history]
    return [item["content"] for item in history if isinstance(item, dict) and item.get("role") == "user"]


ARRIVED = {}      # filter name -> the customer messages the next agent received (filled by watch)


def watch(passes):
    """Wrap a handoff filter so we can see its effect: run it, and note which customer messages came out."""
    def input_filter(data):
        data = passes(data)
        ARRIVED[passes.__name__] = customer_messages(data.input_history)
        return data
    return input_filter


__all__ = ["MODEL", "STRONG_MODEL", "PRICES", "USAGE", "connect", "no_thinking", "ask", "cost",
           "show_steps", "customer_messages", "ARRIVED", "watch"]
