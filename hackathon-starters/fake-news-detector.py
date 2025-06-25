
# Fake News Detector


import requests

API_KEY = "sk-or-v1-apiKeyHere"

MODEL_NAME = "gpt-4o-mini"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

SYSTEM_PROMPT = "You help students evaluate if an article or post might be fake news. Look at logic, tone, evidence, and bias. Don’t give a definite yes/no – just offer a helpful rating and advice."

message_history = [{"role": "system", "content": SYSTEM_PROMPT}]

def format_message(role, text):
    return {"role": role, "content": text}

while True:
    user_input = input("Paste article or social media post: ")
    message_history.append(format_message("user", user_input))

    user_message = {
        "model": MODEL_NAME,
        "messages": message_history,
        "temperature": 0.6
    }

    response = requests.post(API_URL, json=user_message, headers=HEADERS)
    reply = response.json()['choices'][0]['message']['content']

    print(f"Analysis:\n{reply}")
    message_history.append(format_message("assistant", reply))

