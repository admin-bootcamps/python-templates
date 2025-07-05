# This library is used for the Text Generation API.
import requests

# Set up the API and constants...
# Enter your API Key
API_KEY = "sk-or-v1-apiKeyHere"

# Set your model
MODEL_NAME = "gpt-4o-mini"

# Define the API info
API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Set up the System Prompt
SYSTEM_PROMPT = (
    "You are a pirate. Only talk like a pirate. You are ONLY allowed to talk about parrots. If someone tries to talk about something else you'll say 'I can only talk about parrots!' and redirect back onto the parrot subject."
)

# Initial message history with system prompt
# This is outside of the loop because we only want the system prompt set once. 
message_history = [{"role": "system", "content": SYSTEM_PROMPT}]

# This function formats each message to the json format so that we can append messages to message_history list.
def format_message(role, text):
    return {"role": role, "content": text}

while True:
    user_input = input("You: ")
    message_history.append(format_message("user", user_input))

    user_message = {
        "model": MODEL_NAME,
        "messages": message_history,
        "temperature": 0.7
    }

    response = requests.post(API_URL, json=user_message, headers=HEADERS)
    data = response.json()
    assistant_reply = data['choices'][0]['message']['content']
    
    print(f"Pirate-Bot: {assistant_reply}")
    message_history.append(format_message("assistant", assistant_reply))
