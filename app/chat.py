from transformers import pipeline
import json
import os

if os.getenv("CI") != "true": chatbot = pipeline("text2text-generation", model="google/flan-t5-small")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHAT_LOG_PATH = os.path.join(BASE_DIR, "static", "chat_log.json")

def get_response(prompt):
    # Build the full prompt
    full_prompt = (
        "You are a professional Hiring Specialist. Answer the following question or provide guidance:" + prompt
    )

    # Get response from the model
    if os.getenv("CI") == "true":
        response = "Testing..."
    else:
        response = chatbot(full_prompt, max_new_tokens=80)[0]["generated_text"].strip()

    # Log conversation in JSON file
    entry = {"user": prompt, "ai": response}

    # Read existing history (or start new list)
    if os.path.exists(CHAT_LOG_PATH):
        with open(CHAT_LOG_PATH, "r", encoding="utf-8") as f:
            history = json.load(f)
    else:
        history = []

    # Append new entry
    history.append(entry)

    # Save updated history
    with open(CHAT_LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

    return response
