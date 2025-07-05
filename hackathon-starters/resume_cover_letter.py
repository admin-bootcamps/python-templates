
# AI Resume & Cover Letter Assistant


import requests

API_KEY = "sk-or-v1-apiKeyHere"

MODEL_NAME = "gpt-4o-mini"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

SYSTEM_PROMPT = "You help students write resumes and cover letters based on their experience and goals. Use clear, confident, and professional language."

message_history = [{"role": "system", "content": SYSTEM_PROMPT}]

def format_message(role, text):
    return {"role": role, "content": text}

while True:
    user_input = input("Enter your name, skills, experience, and the role you're applying for:\n")
    message_history.append(format_message("user", user_input))

    user_message = {
        "model": MODEL_NAME,
        "messages": message_history,
        "temperature": 0.6
    }

    response = requests.post(API_URL, json=user_message, headers=HEADERS)
    reply = response.json()['choices'][0]['message']['content']

    print("\nGenerated Resume & Cover Letter:\n")
    print(reply)
    message_history.append(format_message("assistant", reply))

