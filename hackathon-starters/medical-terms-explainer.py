### Medical Info Explainer

import requests

API_KEY = "sk-or-v1-apiKeyHere"

MODEL_NAME = "gpt-4o-mini"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

SYSTEM_PROMPT = "You explain medical words in simple, calm, friendly language. You do not diagnose or treat. You just explain what the term means so someone can understand it better."

message_history = [{"role": "system", "content": SYSTEM_PROMPT}]

def format_message(role, text):
    return {"role": role, "content": text}

while True:
    user_input = input("Medical term or phrase: ")
    message_history.append(format_message("user", user_input))
    
    user_message = {
        "model": MODEL_NAME,
        "messages": message_history,
        "temperature": 0.5
    }

    response = requests.post(API_URL, json=user_message, headers=HEADERS)
    reply = response.json()['choices'][0]['message']['content']
    
    print(f"Explanation: {reply}")
    message_history.append(format_message("assistant", reply))
