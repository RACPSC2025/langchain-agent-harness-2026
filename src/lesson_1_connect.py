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


# 5. Parametros Cognitivos de los Modelos (HiperParametros)
"""
En la arquitectura moderna de LangChain, el método create_agent está diseñado con una filosofía minimalista: 
el arnés no debe duplicar los parámetros del modelo.

Por lo tanto, create_agent se divide en dos tipos de propiedades: los parámetros estructurales del 
arnés y los parámetros de generación de hiperparámetros (que se inyectan a través del string de 
configuración o diccionarios).

Parámetros de Estructura (Directos en create_agent)
Son las propiedades nativas que definen qué puede hacer el arnés del agente:

model (str | BaseChatModel): El identificador único ("google:gemini-2.5-flash", "openai:gpt-4o-mini").

system_prompt (str | SystemMessage): Define las reglas del sistema, el rol, las restricciones 
y el idioma de respuesta.

tools (list[Callable | BaseTool]): Lista de funciones nativas de Python que el agente puede invocar 
en su bucle operativo.

response_format (BaseModel | TypedDict | dict): (¡Muy importante en 2026!) Fuerza al agente a retornar
un formato estructurado (usando una clase Pydantic) en lugar de texto plano, ideal para extraer 
JSON estructurado automáticamente.

middleware (list): Lista de capas o interceptores para auditar costos, inyectar seguridad, formatear 
el historial o detener ejecuciones inapropiadas.

Existen 2 soluciones:
Método A: Al inicializar el modelo (Para scripts locales avanzados)
Método B: Mediante Perfiles de Arnés (Harness Profiles) - Este metodo tiene un nivel de dificultad
medio - avanzado por lo que se explicara en capitulos posteriores, solo abordaremos el Metodo A, pero
si quieres ir leyendo informacion al respecto 
https://learn.microsoft.com/en-us/agent-framework/concepts/agents/running-agents?pivots=programming-language-python

uv add langchain-google-genai

from langchain_google_genai import ChatGoogleGenerativeAI

# Aquí se configuran los hiperparámetros individuales del motor cognitivo
custom_model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0.1,       # Más determinista (0.0) o más creativo (1.0)
    max_tokens=150,        # Límite estricto de tamaño de la respuesta
    top_p=0.95,            # Muestreo por núcleo (Nucleus sampling)
    max_retries=3          # Reintentos automáticos si la API de Google falla
)

agent = create_agent(
    model = custom_model,
    system_prompt="You are an expert Artificial Intelligence tutor. Provide concise and clear explanations. Answer in spanish",
)


"""


