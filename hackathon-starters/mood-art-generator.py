
# Mood Art Generator (Text > Image)


import requests
from PIL import Image
from io import BytesIO

API_KEY = "hf_apiKeyHere"

MODEL = "fal-ai/hidream-i1-fast"
API_URL = f"https://router.huggingface.co/fal-ai/{MODEL}"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

while True:
    mood_description = input("Describe your emotion or feeling in words: ")
    user_message = {"prompt": mood_description}

    response = requests.post(API_URL, json=user_message, headers=HEADERS)
    image_url = response.json()['images'][0]['url']

    print(f"Mood Art Image URL: {image_url}")

    image_data = requests.get(image_url).content
    with open("mood_art.jpg", "wb") as f:
        f.write(image_data)

    Image.open(BytesIO(image_data)).show()
