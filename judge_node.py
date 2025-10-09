def judge_node(state):
    print("\n[Judge] Reviewing arguments...\n")

    sci_points = sum("regulation" in s[1].lower() or "safety" in s[1].lower() for s in state["history"])
    phi_points = sum("freedom" in s[1].lower() or "moral" in s[1].lower() for s in state["history"])

    winner = "Scientist" if sci_points >= phi_points else "Philosopher"
    reason = "Presented more grounded, risk-based arguments aligned with public safety principles." \
        if winner == "Scientist" else "Advocated freedom and philosophical progress persuasively."

    print("[Judge] Summary of debate:\n", state["memory_summary"])
    print(f"\n[Judge] Winner: {winner}")
    print(f"Reason: {reason}")

    # Log all results
    with open("logs/debate_log.txt", "w", encoding="utf-8") as f:
        f.write("Debate Log\n===========\n")
        for line in state["history"]:
            f.write(f"{line[0]}: {line[1]}\n")
        f.write(f"\nFinal Verdict: {winner}\nReason: {reason}\n")

    state["winner"] = winner
    return state
