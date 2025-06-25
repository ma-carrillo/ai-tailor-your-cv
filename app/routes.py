from flask import render_template, request
from app import app
from app.utils import parse_cv_file, extract_job_text
from app.rewriting import rewrite_lines
from app.chat import get_response
import os
import json


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHAT_LOG_PATH = os.path.join(BASE_DIR, "static", "chat_log.json")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():

    # Process CV
    cv_file = request.files["cv_file"]
    cv_lines = parse_cv_file(cv_file)

    # Process job text
    job_text = request.form["job_description"]

    # Rewrite the CV based on the job description
    output_text = rewrite_lines(cv_lines, job_text)

    return render_template("result.html", tailored_cv=output_text)

@app.route("/chat", methods=["POST"])
def chat():

    # Get Prompt
    ai_prompt = request.form["ai_prompt"]

    # Receive response from AI
    response = get_response(ai_prompt)

    return render_template("chat.html", ai_prompt=ai_prompt, response=response)

@app.route("/chat/history", methods=["GET"])
def get_chat_history():
    if os.path.exists(CHAT_LOG_PATH):
        with open(CHAT_LOG_PATH, "r", encoding="utf-8") as f:
            history = json.load(f)
    else:
        history = []

    return render_template("chat_history.html", history=history)


@app.route("/chat/history", methods=["DELETE"])
def delete_chat_history():
    if os.path.exists(CHAT_LOG_PATH):
        os.remove(CHAT_LOG_PATH)
        return {"message": "Chat history deleted."}, 200
    else:
        return {"message": "No chat history to delete."}, 404
