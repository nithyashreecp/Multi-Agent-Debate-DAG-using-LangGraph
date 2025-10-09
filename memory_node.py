def memory_node(state):
    # Summarize debate so far
    summary = "\n".join([f"{s[0]}: {s[1]}" for s in state["history"]])
    state["memory_summary"] = summary
    return state
