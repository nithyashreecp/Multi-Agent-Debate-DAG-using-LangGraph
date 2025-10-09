import random

def agent_a(state):
    topic = state["topic"]
    responses = [
        f"As a Scientist, I argue that {topic} requires empirical regulation to ensure public safety.",
        f"From a scientific perspective, {topic} must be controlled to prevent harm from unpredictable outcomes.",
        f"Scientific ethics demand careful oversight when it comes to {topic}.",
        f"Without regulation, the misuse of {topic} could be catastrophic."
    ]
    round_idx = (state["round"] + 1)//2 - 1
    message = responses[round_idx]
    print(f"[Round {state['round']}] Scientist: {message}")
    state["history"].append(("Scientist", message))
    state["round"] += 1
    return state
