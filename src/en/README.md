import os
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from google.colab import userdata

# 1. Configuración de la API Key
os.environ["GEMINI_API_KEY"] = userdata.get('GEMINI_API_KEY')

# 2. Definición del Middleware (El "Gestor de Perfiles")
def apply_harness_profile(runtime):
    """
    Middleware que intercepta el contexto de ejecución para inyectar perfiles de 
    hiperparámetros directamente en la llamada al modelo en tiempo real.
    """
    # Recuperamos el contexto dinámico enviado en el .invoke()
    context = runtime.context if hasattr(runtime, 'context') else {}
    profile_options = context.get("generation_config", {})

    # Si el usuario especificó parámetros, los vinculamos al modelo sobre la marcha
    if profile_options:
        runtime.model = runtime.model.bind(**profile_options)
    
    return runtime

# 3. Inicializamos el agente UNA SOLA VEZ con el middleware registrado
# Usamos init_chat_model para máxima flexibilidad
base_model = init_chat_model("google_genai:gemini-3.6-flash")

agent = create_agent(
    model=base_model,
    system_prompt="Eres un asistente de IA versátil. Adapta tu estilo al perfil solicitado.",
    middleware=[apply_harness_profile] # El arnés ahora procesa perfiles dinámicos
)

# 4. EJECUCIÓN: PERFIL 1 (Creativo)
creative_profile = {"temperature": 0.9, "max_output_tokens": 100}

print("🔥 Ejecutando con Perfil Creativo (Temperatura 0.9)...")
creative_response = agent.invoke(
    {"messages": [{"role": "user", "content": "Escribe un giro de trama de ciencia ficción en 1 oración."}]},
    context={"generation_config": creative_profile} # Inyectando el perfil
)
print(f"IA 🤖: {creative_response['messages'][-1].content}\n")

# 5. EJECUCIÓN: PERFIL 2 (Preciso/Estricto)
precise_profile = {"temperature": 0.1, "max_output_tokens": 50}

print("🎯 Ejecutando con Perfil Preciso (Temperatura 0.1)...")
precise_response = agent.invoke(
    {"messages": [{"role": "user", "content": "Escribe un giro de trama de ciencia ficción en 1 oración."}]},
    context={"generation_config": precise_profile} # Inyectando un perfil diferente
)
print(f"IA 🤖: {precise_response['messages'][-1].content}")