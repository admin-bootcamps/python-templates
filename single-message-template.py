# This library is used for the Text Generation API.
import requests

# Set up the API and constants...
# Enter your API Key
API_KEY = "sk-or-v1-apiKeyHere"


# Set your model
MODEL_NAME = "gpt-4o-mini"

# Define the API info
API_URL = "https://openrouter.ai/api/v1/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# We will set the first part of the prompt and allow the user to choose what topic to use.
start_message = "Tell me a funny and unique joke about:  "


while True:
    user_input = input("Joke topic: ")

    # Construct the prompt
    message_send = start_message + user_input
    
    # Construct the message
    user_message = {
        "model": MODEL_NAME,
        "prompt": message_send,
        "temperature": 0.7
    }

    # Call the API
    response = requests.post(API_URL, json=user_message, headers=HEADERS)
    # Get the data we need from the API response
    data = response.json()
    # Get the text content of the message to show the user
    assistant_reply = data['choices'][0]['text']
    print(f"Joke-Bot: {assistant_reply}")
    
