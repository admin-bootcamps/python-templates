# This library is used for the Image Generation API.
import requests

# These libraries are for managing the image processing.
from PIL import Image
from io import BytesIO

# Set up the API and constants...
# Enter your API Key
API_KEY = "hf_apiKeyHere"

# Set your model
MODEL = "fal-ai/hidream-i1-fast"

# Define the API info
API_URL = f"https://router.huggingface.co/fal-ai/{MODEL}"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

while True:
    # Ask the User for input and format it in the way we need for the API
    prompt = input("Generate an image of: ")
    user_message = {"prompt": prompt}

    # Call the API
    response = requests.post(API_URL, json=user_message, headers=HEADERS)
    # Get the data we need from the API response and process it.
    image_url = response.json()['images'][0]['url']

    # Display the image URL.
    print(f"Image URL: {image_url}")

    # Get the image from the URL
    image_data = requests.get(image_url).content

    # Save the image to a file
    with open("output.jpg", "wb") as f:
        f.write(image_data)

    # Show the image
    Image.open(BytesIO(image_data)).show()
