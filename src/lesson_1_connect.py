import os
from langchain.agents import create_agent
from dotenv import load_dotenv

# 1. Cargar las variables del archivo .env de forma local
load_dotenv()

# Verificar si la API key existe en el entorno
if not os.getenv("GEMINI_API_KEY"):
    raise ValueError("❌ ERROR: La variable 'GEMINI_API_KEY' no está configurada o está vacía. Verifica tu .env.")

print("✅ API Key detectada correctamente. Conectando al LLM...")

# Configuramos la variable que LangChain busca automáticamente por detrás
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME")

# 2. Inicializamos el modelo y arnés conversacional (System Prompt en inglés, instrucción de idioma al final)
agent = create_agent(
    model=GEMINI_MODEL_NAME,
    system_prompt="You are an AI agent. Answer the question short, concise and friendly. Respond in Spanish."
)

# 3. El arnés se ejecuta enviando el estado de la conversación (messages)
response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Explain what Artificial Intelligence is in one sentence."
            }
        ]
    }
)

# 4. Inspeccionamos el Output del LLM
last_message = response["messages"][-1]

# Output - Content_blocks y Content (en futuras lecciones usaremos estructuras mejoradas y modeladas)
# Opción A: Inspección de la estructura interna unificada (content_blocks)
print("\n--- Content Blocks Structure ---")
# Accedemos al texto del bloque interno usando el atributo o un mapeo seguro
if hasattr(last_message, 'content_blocks') and last_message.content_blocks:
    # Si viene como objeto con atributo 'text'
    print(f"PROMPT AI: {last_message.content_blocks[0].text if hasattr(last_message.content_blocks[0], 'text') else last_message.content_blocks[0].get('text', '')}")

# Opción B: Extracción del texto limpio (La recomendada para producción)
print("\n--- Final Text Output ---")
print(f"PROMPT AI: {last_message.content[0].get('text', '')}")




