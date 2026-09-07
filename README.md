# 🤖 Modern LangChain: The Agent Harness Era (2026)

[![LangChain](https://img.shields.io/badge/LangChain-2026_Modern_Architecture-1C3C3C?logo=langchain&logoColor=white)](https://docs.langchain.com)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org)
[![Google Colab](https://img.shields.io/badge/Google_Colab-Interactive-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Master LangChain using the modern `create_agent` architecture. No legacy chains, no outdated patterns—just production-ready Agent Harness engineering.**

---

## 🌐 Languages / Idiomas

Este curso está disponible en dos idiomas. Selecciona tu versión preferida para acceder a las guías de estudio y los notebooks interactivos:

- 🇪🇸 **Español**: [Ir a `src/es/`](src/es/) (Incluye `lesson_1_connect_es.ipynb`)
- 🇬🇧 **English**: [Go to `src/en/`](src/en/) (Includes `lesson_1_connect_en.ipynb`)

---

## 📖 About This Course / Sobre este Curso

This repository contains a **step-by-step, hands-on curriculum** designed to teach you how to build AI agents using LangChain's **2026 modern architecture**. 

Unlike traditional courses that start with basic LLM wrappers or sequential chains, we begin directly with the **Agent Harness paradigm**—the industry standard for building autonomous, tool-using, and stateful AI systems.

### 🎯 What You'll Learn / Qué aprenderás
- **Agent Harness Architecture**: The "chassis" that wraps around LLMs to enable autonomous behavior, tool calling, and memory.
- **Model Agnostic Development**: Switch between OpenAI, Anthropic, Google, and more with a single string configuration.
- **Production Patterns**: Clean, maintainable, and fault-tolerant code (`init_chat_model` + `create_agent`).
- **Safety & Observability**: Guardrails, Human-in-the-Loop, and LangSmith tracing for enterprise-grade deployments.

### 🌟 Key Features
- ✅ **100% Modern**: Zero legacy `LLMChain` or outdated sequential patterns.
- ✅ **Provider Agnostic**: Learn once, deploy anywhere.
- ✅ **Interactive**: All lessons are Google Colab notebooks ready to run.
- ✅ **Bilingual**: Complete curriculum and documentation in English and Spanish.
- ✅ **Progressive Difficulty**: Basic and advanced versions for each lesson.

---

## 📚 Curriculum / Temario

### **Level 1: Core Agent Harness (Fundamentos)**
| Lesson | Topic / Tema | Status |
|--------|--------------|--------|
| **01** | **Agent Harness Fundamentals** (`create_agent` + `init_chat_model`) | ✅ Complete |
| **02** | **Tools & Tool Calling** - `@tool`, custom tools, dynamic selection | 🚧 Coming Soon |
| **03** | **Messages & Conversation State** - History, state management | 🚧 Coming Soon |
| **04** | **Short-term Memory** - Checkpointers, session memory | 🚧 Coming Soon |
| **05** | **Structured Output** - Pydantic schemas, JSON extraction | 🚧 Coming Soon |
| **06** | **Streaming** - Real-time token streaming, async execution | 🚧 Coming Soon |
| **07** | **Middleware** - Dynamic behavior, Harness Profiles, interceptors |  Coming Soon |

### **Level 2: Production & Advanced Patterns (Producción)**
| Lesson | Topic / Tema | Status |
|--------|--------------|--------|
| **08** | **Runtime Context** - `context=`, `context_schema`, advanced injection | 🚧 Coming Soon |
| **09** | **Long-term Memory** - `Store`, cross-session persistence | 🚧 Coming Soon |
| **10** | **Human-in-the-Loop** - Interrupts, approval flows, safety brakes | 🚧 Coming Soon |
| **11** | **Guardrails** - Input/Output validation, safety filters, content moderation | 🚧 Coming Soon |
| **12** | **Observability** - LangSmith tracing, debugging, monitoring | 🚧 Coming Soon |

### **Level 3: Optional / Next Level (Avanzado)**
| Lesson | Topic / Tema | Status |
|--------|--------------|--------|
| **13** | **Deep Agents** - "Batteries-included" agents, planning, subagents |  Coming Soon |

---

## 🚀 Quick Start / Inicio Rápido

### 1. Prerequisites / Prerrequisitos
- A **Google Account** (to run notebooks in Colab).
- An **API Key** from your preferred LLM provider:
  - [Google AI Studio](https://aistudio.google.com/) (Free tier available for Gemini)
  - [OpenAI API](https://platform.openai.com/)
  - [Anthropic API](https://console.anthropic.com/)

### 2. Running the Notebooks / Ejecutar los Notebooks
1. Navigate to your preferred language folder: [`src/es/`](src/es/) or [`src/en/`](src/en/).
2. Click on any `.ipynb` file (e.g., `lesson_1_connect_en.ipynb`).
3. Click the **"Open in Colab"** badge at the top of the file.
4. In Google Colab, go to the **Secrets** (🔑) tab on the left sidebar.
5. Add your API key (e.g., `GEMINI_API_KEY`).
6. Run the cells sequentially.

### 3. Example Snippet / Ejemplo de Código
```python
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
import os

# 1. THE MOTOR (Model Agnostic)
model = init_chat_model("google_genai:gemini-3.6-flash", temperature=0.3)

# 2. THE HARNESS (Agent Loop)
agent = create_agent(
    model=model,
    system_prompt="You are an expert AI tutor. Answer concisely."
)

# 3. EXECUTION
response = agent.invoke({
    "messages": [{"role": "user", "content": "Explain the Agent Harness paradigm."}]
})

print(response["messages"][-1].content)


📁 Repository Structure / Estructura del Repositorio
 langchain-agent-harness-2026/
├── 📄 README.md                               ← You are here (Course overview)
├── 📄 .env.example                            ← Template for local environment variables
├── 📄 pyproject.toml                          ← Python dependencies (uv/pip)
├── 📄 LICENSE
└── 📂 src/
    ├── 📂 es/                                 ← 🇪🇸 Spanish version
    │   ├── 📄 README.md                       ← Guía de estudio detallada (ES)
    │   ├──  lesson_1_connect_es.ipynb       ← Nivel Básico (Métodos A y B)
    │   ├── 📄 lesson_1_connect_advanced_es.ipynb  ← Nivel Avanzado (Método C)
    │   ├── 📄 lesson_1_connect_es.py
    │   └── 📄 lesson_2_tools_es.ipynb         ← Tools & Tool Calling (Coming Soon)
    └──  en/                                 ← 🇬🇧 English version
        ├── 📄 README.md                       ← Detailed study guide (EN)
        ├── 📄 lesson_1_connect_en.ipynb       ← Basic Level (Methods A & B)
        ├── 📄 lesson_1_connect_advanced_en.ipynb  ← Advanced Level (Method C)
        └── 📄 lesson_2_tools_en.ipynb         ← Tools & Tool Calling (Coming Soon)

## 🎓 Who Is This Course For? / ¿Para quién es este curso?
- **Developers** transitioning from traditional LLM wrappers to modern agent architectures.
- **AI Engineers** building production-ready, autonomous systems.
- **Students** who want to learn LangChain the right way (2026 standards).
- **Technical Leaders** evaluating agent frameworks for their teams.
---

## 🤝 Contributing / Contribuir

Contributions, translations, and suggestions are highly welcome! 
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'Add amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Built with ❤️ for the AI engineering community**  
*Last updated: September 2026*
```

---

### ✅ Cambios aplicados:

1. **Estructura de repositorio corregida**: Ahora refleja exactamente tu directorio actual con los nombres correctos (`lesson_1_connect_advanced_es.ipynb`, `lesson_1_connect_advanced_en.ipynb`, etc.).
2. **Lección 2 añadida**: `lesson_2_tools_es.ipynb` y `lesson_2_tools_en.ipynb` ya están en la estructura como "Coming Soon".
3. **Formato limpio**: La estructura del árbol ahora es consistente y profesional.

---
