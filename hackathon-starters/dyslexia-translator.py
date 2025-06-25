
# Accessibility Tool for Dyslexia


import requests

API_KEY = "sk-or-v1-apiKeyHere"

MODEL_NAME = "gpt-4o-mini"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

SYSTEM_PROMPT = "You simplify text for students with dyslexia. Use shorter words, clearer structure, and break content into short, readable chunks. You do NOT use fancy formatting or advanced vocabulary."

message_history = [{"role": "system", "content": SYSTEM_PROMPT}]

def format_message(role, text):
    return {"role": role, "content": text}

while True:
    user_input = input("Enter text to simplify for dyslexia: ")
    message_history.append(format_message("user", user_input))
    
    user_message = {
        "model": MODEL_NAME,
        "messages": message_history,
        "temperature": 0.4
    }

    response = requests.post(API_URL, json=user_message, headers=HEADERS)
    reply = response.json()['choices'][0]['message']['content']
    
    print(f"Readable version:\n{reply}")
    message_history.append(format_message("assistant", reply))
