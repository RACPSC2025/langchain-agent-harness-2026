
import os
import json

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from dotenv import load_dotenv

# 1. LLM API KEY
load_dotenv()

if not os.getenv("GEMINI_API_KEY"):
    raise ValueError("❌ ERROR: 'GEMINI_API_KEY' no found or empty.")

print("✅ API Key detectada correctamente. Conectando al LLM...")


# 2. Creating your First Tool
@tool
def get_current_weather(city: str) -> str:
    """
    Get the current weather conditions for a specific city.

    Use this tool when the user asks about:
    - Current weather conditions
    - Temperature, humidity, or wind speed
    - Whether it's raining, sunny, or cloudy

    Args:
        city: The name of the city to check weather for (e.g., "New York", "Tokyo")

    Returns:
        A string with current weather information including temperature, conditions, and humidity.
    """
    # Simulated weather data (in production, this would call a real API)
    weather_data = {
        "new york": "New York: 22°C (72°F), Partly Cloudy, Humidity: 65%",
        "london": "London: 15°C (59°F), Overcast, Humidity: 80%",
        "tokyo": "Tokyo: 28°C (82°F), Sunny, Humidity: 55%",
        "paris": "Paris: 18°C (64°F), Light Rain, Humidity: 75%",
        "sydney": "Sydney: 25°C (77°F), Clear Sky, Humidity: 60%"
    }

    # Normalize input and return weather data
    city_lower = city.lower()
    if city_lower in weather_data:
        return weather_data[city_lower]
    else:
        return f"Weather data not available for {city}. Please try another city."

# Let's inspect the tool's schema (what the LLM sees, what the decorator created)
print("Tool Name:", get_current_weather.name)
print("\nTool Description:")
print(get_current_weather.description)
print("\nTool Schema (JSON):")
print(json.dumps(get_current_weather.args_schema.model_json_schema(), indent=2))


# 3. Model (the motor)
model = init_chat_model(
    "google_genai:gemini-3.6-flash",
    # temperature=0.2,          # Lower temperature → more deterministic tool use
)

# 4. Agent Harness with the tool
agent = create_agent(
    model=model,
    tools=[get_current_weather],      # ← This is the key line
        system_prompt="""You are a helpful weather assistant.
        When users ask about weather, use the get_current_weather tool to provide accurate information.
        Always respond in a friendly and concise manner.""",
)

# 5. Invoke
result = agent.invoke({
    "messages": [
        {"role": "user", "content": "What is the weather in New York?"}
    ]
})

# 6. Clean output
"""last_message = result["messages"][-1]
print("AI 🤖:", last_message.content[0].get('text', ''))

print("--- AGENT EXECUTION TRACE ---\n")

for msg in result["messages"]:
    msg_type = type(msg).__name__

    if msg_type == "HumanMessage":
        print(f"👤 USER: {msg.content}")

    elif msg_type == "AIMessage" and msg.tool_calls:
        # The LLM decided to use a tool
        tool_call = msg.tool_calls[0]
        print(f"🧠 AI DECISION: Called tool '{tool_call['name']}' with args {tool_call['args']}")

    elif msg_type == "ToolMessage":
        # The Harness executed the tool and returned this
        print(f"🛠️ SYSTEM (Tool Result): {msg.content}")

    elif msg_type == "AIMessage" and msg.content:
        # The final answer generated after seeing the tool result
        print(f"🤖 AI FINAL ANSWER: {msg.content[0].get('text', '')}")

    print("-" * 40)"""