
# Mood Art Generator (Text > Image)


import requests
from PIL import Image
from io import BytesIO
import os



# Set up the Image API Params...

IMAGE_API_KEY = "hf_yourImageKeyHere"

IMAGE_MODEL = "fal-ai/hidream-i1-fast"
IMAGE_API_URL = f"https://router.huggingface.co/fal-ai/{IMAGE_MODEL}"
IMAGE_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {IMAGE_API_KEY}"
}

# Set up the Text API Params...

TEXT_API_KEY = "sk-or-v1-yourTextKeyHere"



TEXT_MODEL_NAME = "gpt-4o-mini"
TEXT_API_URL = "https://openrouter.ai/api/v1/chat/completions"
TEXT_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TEXT_API_KEY}"
}

TEXT_SYSTEM_PROMPT = """You are a prompt generator. You'll generate a prompt that can be directly fed into an image generation model. You will be given a mood. Give an image prompt that would generate a visualisation of the mood(s) you're given. The mood should be represented by colours, motion, flows and patterns in the image, rather than having a subject or scene. Here are some examples of descriptions you might use:

happy: bright yellows, soft curves, sunny light;
joyful: radiant oranges, playful shapes, sparkles and confetti;
excited: vivid oranges and pinks, dynamic lines, bursts of light;
calm: cool greens and blues, smooth waves, peaceful balance;
relaxed: pale blues, horizontal lines, slow movement, open space;
sad: muted blues, slow flowing water, soft shadows."""


IDENTIFY_SYSTEM_PROMPT= """ You are a mood identifier. You help identify labels for the user's emotions or feelings when they can't articulate it themselves. You'll be given a description of a mood, emotion or feeling. This might be in colours, shapes, physical experience, or other descriptors. Your job is to identify what emotion might apply to the user's feelings. output one or two emotions that might apply to the given description.  
"""



    


# Run our script ...
while True:
    mood_description = input("Describe your emotion or feelings in words, shapes, colours, or however you want.\n->  ")

    # Construct the message
    user_message = {
        "model": TEXT_MODEL_NAME,
        "messages": [{"role": "system", "content": IDENTIFY_SYSTEM_PROMPT},{"role": "user", "content": mood_description}],
        "temperature": 0.7
    }

    # Call the Text API which will write a detailed Prompt
    response = requests.post(TEXT_API_URL, json=user_message, headers=TEXT_HEADERS)

     # Get the emotion that was identified
    emotion_label = response.json()['choices'][0]['message']['content']
    print(f"Sounds like you might be feeling: {emotion_label}")


# Now, construct the Image Prompt


  # Construct the message
    user_message = {
        "model": TEXT_MODEL_NAME,
        "messages": [{"role": "system", "content": TEXT_SYSTEM_PROMPT},{"role": "user", "content": emotion_label}],
        "temperature": 0.7
    }

    # Call the Text API which will write a detailed Prompt
    response = requests.post(TEXT_API_URL, json=user_message, headers=TEXT_HEADERS)

    # Get the data we need from the API response
    image_prompt = response.json()['choices'][0]['message']['content']
    # print(f"Generated Image Prompt: {image_prompt}")

    # Construct the Image API input with the prompt we just generated
    image_input = {"prompt": image_prompt}

    # Call the API
    response = requests.post(IMAGE_API_URL, json=image_input, headers=IMAGE_HEADERS)

    # Get the data we need from the API response and process it.
    image_url = response.json()['images'][0]['url']

    # Display the image URL.
    print(f"Mood Art Image URL: {image_url}")

    # Get the image from the URL
    image_data = requests.get(image_url).content

    # Make a file name from the emotion labels
    filename = emotion_label.replace(" ", "_").replace(",", "").lower()
    
    # Save the image under the created file name
    with open(f"images/{filename}.jpg", "wb") as f:
        f.write(image_data)

    # Show the image
    Image.open(BytesIO(image_data)).show()





# EXAMPLE OUTPUTS

#################################################

# example_angry.jpeg

    # Describe your emotion or feeling in words: angry and emotional

    # Generated Image Prompt: Intense reds and dark maroons, sharp jagged lines, chaotic swirls, contrasting shadows, and erratic bursts of energy, all combined to create a sense of turbulence and heat, reflecting the rawness of anger and deep emotional turmoil.

    # Mood Art Image URL: https://v3.fal.media/files/kangaroo/ievnQh6nUAjsahi8gqST7.jpeg

#################################################

# example_nostalgic.jpeg

    # Describe your emotion or feeling in words: happy, nostalgic, calm

    # Generated Image Prompt: A harmonious blend of soft pastel yellows and gentle corals, featuring smooth, flowing curves that evoke a sense of warmth and comfort. Subtle hints of light greens and sky blues create a serene backdrop, while delicate sparkles and wispy textures add a nostalgic touch of whimsy. The overall composition should embody a peaceful balance, with soft gradients and flowing patterns that encourage a sense of tranquility and fond memories.

    # Mood Art Image URL: https://v3.fal.media/files/penguin/cddqM-Rtkw9wrBcqRTemJ.jpeg

#################################################

# example_frustrated.jpeg

    # Describe your emotion or feeling in words: frustrated but i know i'm just hungry

    # Generated Image Prompt: deep, muted reds and browns, sharp jagged lines, chaotic patterns, swirling textures, intermittent bursts of brightness representing fleeting hope, and a sense of tension in the composition.

    # Mood Art Image URL: https://v3.fal.media/files/kangaroo/4I_lO_3_wttllJEAV1Hag.jpeg

#################################################

# example_happy_sad.jpeg

    # Describe your emotion or feeling in words: happy and a bit sad

    # Generated Image Prompt: Create an abstract image that blends warm, vibrant yellows and soft oranges to evoke happiness, flowing seamlessly into cooler shades of blue and gentle purples to represent a hint of sadness. Incorporate swirling patterns that mix energetic brush strokes with softer, more delicate lines, creating a sense of motion that captures the complexity of these emotions. The overall composition should have a harmonious balance, with light radiating from the center, gradually fading into darker hues at the edges, symbolizing the interplay between joy and melancholy.

    # Mood Art Image URL: https://v3.fal.media/files/elephant/2Z-ogjyh8ubZSa1B6d0FX.jpeg