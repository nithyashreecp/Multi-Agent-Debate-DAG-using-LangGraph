# Multi-Agent-Debate-DAG-using-LangGraph

## Overview
This project implements a **multi-agent debate system** using **LangGraph**. Two AI agents (Scientist and Philosopher) debate a user-provided topic over **8 structured rounds**. The system maintains **memory**, enforces **turn-based rules**, ensures **logical coherence**, and generates an **automated judgment** declaring a winner.

---

## Features
- CLI-based interaction for entering debate topics
- Two profession-specific AI agents with alternating turns
- Memory storage of arguments and summaries
- Judge node that evaluates debate logically and declares a winner
- Full logging of messages, state transitions, memory updates, and final verdict
- DAG diagram visualizing LangGraph workflow

---

## Requirements
- Python 3.10+
- [LangGraph](https://pypi.org/project/langgraph/)
- Other dependencies:
  ```bash
  pip install langgraph graphviz
  ```

---

## Project Structure
```
multi-agent-debate/
│
├─ debate.py                # Main script to run the debate
├─ nodes/
│   ├─ user_input_node.py   # UserInputNode definition
│   ├─ agent_a_node.py      # AgentA (Scientist) node
│   ├─ agent_b_node.py      # AgentB (Philosopher) node
│   ├─ memory_node.py       # MemoryNode definition
│   └─ judge_node.py        # JudgeNode definition
├─ logs/
│   └─ debate_log.txt       # Full log of debate sessions
├─ dag_diagram.png          # DAG diagram of LangGraph workflow
└─ README.md
```

---

## How to Run
1. Clone the repository or unzip the folder:
   ```bash
   git clone <repo_url>
   cd multi-agent-debate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the debate simulation:
   ```bash
   python debate.py
   ```

4. Enter a topic when prompted:
   ```
   Enter topic for debate: Should AI be regulated like medicine?
   ```

5. Follow the CLI as the debate progresses through **8 rounds**. The judge will summarize and declare a winner at the end.

---

## LangGraph DAG Workflow
The debate is structured using a **Directed Acyclic Graph (DAG)** with the following nodes:

1. **UserInputNode**: Receives debate topic from user
2. **AgentA & AgentB**: Alternate arguments for 8 rounds
3. **MemoryNode**: Stores and updates relevant dialogue
4. **JudgeNode**: Evaluates debate and declares winner



---

## Logging
All debate interactions, memory updates, and final verdicts are saved in:
```
logs/debate_log.txt
```

Example:
```
[Round 1] Scientist: AI must be regulated due to high-risk applications.
[Round 2] Philosopher: Regulation could stifle philosophical progress and autonomy.
...
[Judge] Summary of debate: ...
[Judge] Winner: Scientist
Reason: Presented grounded, risk-based arguments aligned with public safety.
```

---

## Notes
- Each agent speaks only in its assigned turn
- Arguments cannot be repeated
- Logical consistency is validated at each turn
- CLI interface ensures smooth user interaction
