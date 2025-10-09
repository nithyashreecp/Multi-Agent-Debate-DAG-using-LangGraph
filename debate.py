from typing import TypedDict
from langgraph.graph import StateGraph, END

# node functions
from nodes.agent_a import agent_a
from nodes.agent_b import agent_b
from nodes.memory_node import memory_node
from nodes.judge_node import judge_node


class DebateState(TypedDict, total=False):
    topic: str
    round: int
    history: list
    memory_summary: str
    winner: str


def main():
    print("Welcome to the AI Debate Simulation!")
    topic = input("Enter topic for debate: ").strip()
    print(f"\nStarting debate between Scientist and Philosopher on: {topic}\n")

    # initial state (topic set once here)
    initial_state = {"topic": topic, "round": 1, "history": []}

    # build graph (sequential, no cycles)
    graph = StateGraph(DebateState)
    graph.add_node("round_1", agent_a)
    graph.add_node("round_2", agent_b)
    graph.add_node("round_3", agent_a)
    graph.add_node("round_4", agent_b)
    graph.add_node("round_5", agent_a)
    graph.add_node("round_6", agent_b)
    graph.add_node("round_7", agent_a)
    graph.add_node("round_8", agent_b)
    graph.add_node("memory", memory_node)
    graph.add_node("judge", judge_node)

    graph.add_edge("round_1", "round_2")
    graph.add_edge("round_2", "round_3")
    graph.add_edge("round_3", "round_4")
    graph.add_edge("round_4", "round_5")
    graph.add_edge("round_5", "round_6")
    graph.add_edge("round_6", "round_7")
    graph.add_edge("round_7", "round_8")
    graph.add_edge("round_8", "memory")
    graph.add_edge("memory", "judge")

    graph.set_entry_point("round_1")
    graph.add_edge("judge", END)

    app = graph.compile()
    result = app.invoke(initial_state)  # pass initial state with topic

    print("\n✅ Debate completed. Logs saved in logs/debate_log.txt")
    print(f"🏆 Winner: {result.get('winner', 'Unknown')}")


if __name__ == "__main__":
    main()







