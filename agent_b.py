def agent_b(state):
    topic = state["topic"]
    responses = [
        f"As a Philosopher, I believe {topic} should remain open to human creativity and moral evolution.",
        f"Regulation of {topic} might hinder philosophical and intellectual freedom.",
        f"History shows that overregulation of ideas like {topic} suppresses progress.",
        f"{topic} is as much a moral question as a practical one; excessive rules could stunt human growth."
    ]
    round_idx = (state["round"])//2 - 1
    message = responses[round_idx]
    print(f"[Round {state['round']}] Philosopher: {message}")
    state["history"].append(("Philosopher", message))
    state["round"] += 1
    return state
