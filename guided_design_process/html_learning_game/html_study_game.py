# This library is used for the Text Generation API.
import requests

# -------------------------------
# Set up the API and constants
# -------------------------------
API_KEY = "sk-or-v1-yourApiKey"
MODEL_NAME = "gpt-5-mini"

API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# -------------------------------
# Set up the System Prompt
# -------------------------------
SYSTEM_PROMPT = (
    "You are an AI assistant that generates interactive HTML learning games. When given a topic and optional study material, you will output a complete HTML file containing a gamified learning experience (e.g., multiple-choice quiz, flashcards, or matching game). Include HTML, CSS, and JavaScript in one file. The game should track scores, provide feedback for correct/incorrect answers, and be ready to run in a browser. Do not include explanations outside of the HTML code. There should be interactivity, varied colours, and overall make the learning more fun."
)

# -------------------------------
# Initialize message history
# -------------------------------
message_history = [{"role": "system", "content": SYSTEM_PROMPT}]

# -------------------------------
# Function to format messages
# -------------------------------
def format_message(role, text):
    return {"role": role, "content": text}

# -------------------------------
# Main Loop
# -------------------------------
while True:
    
    print("\nEnter your study topic (or 'exit' to quit):")
    topic = input("Topic: ")
    if topic.lower() == "exit":
        break

    print("Optional: Enter study material or questions (press Enter to skip):")
    study_material = input("Study Material: ")

    # Construct prompt for AI
    user_prompt = f"Generate an HTML learning game for the topic: '{topic}'."
    if study_material.strip():
        user_prompt += f" Include the following study material/questions: {study_material}"

    message_history.append(format_message("user", user_prompt))
    print(f"\nAI is working on it...")
    # Call the API
    user_message = {
        "model": MODEL_NAME,
        "messages": message_history,
        "temperature": 0.7
    }
    
    response = requests.post(API_URL, json=user_message, headers=HEADERS)
    data = response.json()
    assistant_reply = data['choices'][0]['message']['content']

    if '```html' in assistant_reply:
        assistant_reply=assistant_reply.replace('```html','')
        assistant_reply=assistant_reply.replace('```','')
    print(f"\nSaving your file...")

    # Display message
    filename=topic.replace(" ","_")
    print(f"\nAI has generated the HTML game! Saving to '{filename}_learning_game.html'...")
    with open(f"guided_design_process/html_learning_game/generated_html/{filename}_learning_game.html", "w", encoding="utf-8") as file:
        file.write(assistant_reply)
        
    
    print(f"Saved! Open '{filename}_learning_game.html' in a browser to play the game.")

    # Append assistant reply to message history
    message_history.append(format_message("assistant", assistant_reply))
