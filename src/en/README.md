# 🇬🇧 LangChain Modern: Study Guide (English)

Welcome to the English study guide for "LangChain Modern: The Agent Harness Era (2026)". This folder contains the interactive Google Colab notebooks and helper scripts for the English track. Use this README as the primary entrypoint for running lessons, understanding the curriculum, and finding helpful links.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RACPSC2025/langchain-agent-harness-2026/blob/main/src/en/lesson_1_connect_en.ipynb)

---

## 📚 Curriculum — Lessons Overview

### Level 1: Core Agent Harness (Fundamentals)

| Lesson | Topic | Status |
|--------:|:------|:------:|
| **01** | **Agent Harness Fundamentals** (`create_agent` + `init_chat_model`) | ✅ Complete |
| **02** | **Tools & Tool Calling** — `@tool`, custom tools, dynamic selection | 🚧 Coming Soon |
| **03** | **Messages & Conversation State** — History, state management | 🚧 Coming Soon |
| **04** | **Short-term Memory** — Checkpointers, session memory | 🚧 Coming Soon |
| **05** | **Structured Output** — Pydantic schemas, JSON extraction | 🚧 Coming Soon |
| **06** | **Streaming** — Real-time token streaming, async execution | 🚧 Coming Soon |
| **07** | **Middleware** — Dynamic behavior, Harness profiles, interceptors | 🚧 Coming Soon |

### Level 2: Production & Advanced Patterns (Production)

| Lesson | Topic | Status |
|--------:|:------|:------:|
| **08** | **Runtime Context** — `context=`, `context_schema`, advanced injection | 🚧 Coming Soon |
| **09** | **Long-term Memory** — `Store`, cross-session persistence | 🚧 Coming Soon |
| **10** | **Human-in-the-Loop** — Interrupts, approval flows, safety brakes | 🚧 Coming Soon |
| **11** | **Guardrails** — Input/Output validation, safety filters, content moderation | 🚧 Coming Soon |
| **12** | **Observability** — LangSmith tracing, debugging, monitoring | 🚧 Coming Soon |

### Level 3: Optional / Next Level (Advanced)

| Lesson | Topic | Status |
|--------:|:------|:------:|
| **13** | **Deep Agents** — "Batteries-included" agents, planning, subagents | 🚧 Coming Soon |

---

## 🚀 Quick Start (English)

Recommended: run the notebooks in Google Colab — they are preconfigured to accept secrets and run interactively.

1. Open `src/en/lesson_1_connect_en.ipynb` and click the "Open in Colab" badge.
2. In Colab: open the Secrets panel (🔑) and add the required API keys (e.g., `GEMINI_API_KEY`, `OPENAI_API_KEY`, or `ANTHROPIC_API_KEY`).
3. Run cells sequentially. The notebooks use `init_chat_model` + `create_agent` patterns and include both Basic and Advanced versions where available.

Local execution (advanced):

- Ensure Python 3.11+.
- Copy `.env.example` from the repo root to `.env` and add your API keys.
- Install dependencies via `pip install -r requirements.txt` or `pip install .` if using the project packaging.
- Run a lesson script (if provided): `python src/en/lesson_1_connect.py` or open the `.ipynb` in Jupyter.

---

## 🔧 Example Usage (Python snippet)

```python
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

# 1. Initialize a model (provider-agnostic)
model = init_chat_model("google_genai:gemini-3.6-flash", temperature=0.3)

# 2. Create the Agent Harness
agent = create_agent(
    model=model,
    system_prompt="You are an expert AI tutor. Provide concise, accurate answers."
)

# 3. Invoke
response = agent.invoke({
    "messages": [{"role": "user", "content": "Explain the Agent Harness paradigm in one paragraph."}]
})

print(response["messages"][-1].content)
```

Notes:
- Use `init_chat_model` for provider-agnostic initialization.
- Prefer middleware and runtime `context` for runtime profile injection and production flexibility.

---

## 📁 Repository Structure (short)

```
langchain-agent-harness-2026/
├── README.md
├── .env.example
├── pyproject.toml
├── LICENSE
└── src/
    ├── es/         ← Spanish track (localized notebooks + README)
    └── en/         ← English track (this folder)
        ├── README.md
        ├── lesson_1_connect_en.ipynb
        ├── lesson_1_connect_advanced_en.ipynb
        └── lesson_2_tools_en.ipynb
```

---

## 🎯 Who is this for?

- Developers moving from legacy chain patterns to modern agent-based architectures.
- AI engineers building production-grade autonomous systems with tools and memory.
- Students and practitioners who want an opinionated, up-to-date LangChain workflow.

---

## 📚 Helpful Links

- LangChain Agents: https://docs.langchain.com/oss/python/langchain/agents
- LangChain Models: https://docs.langchain.com/oss/python/langchain/models
- LangChain Runtime & Middleware: https://docs.langchain.com/oss/python/langchain/runtime

---

## 🤝 Contributing

Contributions are welcome. To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/my-improvement`).
3. Add or improve notebooks and README content.
4. Open a pull request describing your changes.

If you improve one language track, please mirror the same structural changes in the other language folder to keep both tracks in sync.

---

If you want, I can also:
- Add direct "Open in Colab" badges next to each notebook file.
- Mirror this structure and wording in `src/es/README.md` (Spanish translation).
- Add a short 