# CV Tailor Pro

**CV Tailor Pro** is a lightweight and intelligent web application that automatically rewrites your CV to match a specific job description. It supports both a traditional web interface and a RESTful API for programmatic access.

---

## Main Features

- **CV rewriting** using a transformer-based language model (`Flan-T5`).
- **Interactive chatbot** to answer CV improvement questions.
- **Conversation history** stored locally in JSON.
- **Web interface** built with Flask and HTML/CSS.
- **REST API** for backend integrations (POST, GET, DELETE).
- **Testable from Python** using real endpoints.

---

## Key Technologies & Skills

| Category           | Tools & Skills                                     |
|--------------------|----------------------------------------------------|
| Programming      | Python (Flask, requests), HTML, CSS                |
| AI/ML            | Hugging Face Transformers, Flan-T5                 |
| API Design       | RESTful endpoints (`GET`, `POST`, `DELETE`)        |
| Dev Tools        | Git, Virtual Environments, JSON handling           |
| Testing          | Python scripts, Postman, curl                      |
| File Handling    | Uploads, parsing `.txt` files, JSON logging        |

---

## Web Interface Usage

1. Upload your CV as a plain `.txt` file.
2. Paste the job description you're targeting.
3. The app rewrites your CV to better align with the job.
4. Use the AI chatbot to ask specific CV improvement questions.

---

## 🔌 REST API Endpoints

| Method | Route                  | Description                          |
|--------|------------------------|--------------------------------------|
| POST   | `/api/rewrite`         | Rewrite CV lines to match job        |
| POST   | `/api/chat`            | Ask the chatbot a career-related question |
| GET    | `/api/chat/history`    | Retrieve the chat history            |
| DELETE | `/api/chat/history`    | Clear the chat history               |

### Sample Request (POST /api/rewrite)

```json
{
  "cv_lines": [
    "Managed social media campaigns",
    "Created presentations for internal reviews"
  ],
  "job_description": "Looking for a creative marketing specialist with analytics experience"
}
````

---

## Project Structure

```
cv_tailor_pro/
│
├── app/
│   ├── __init__.py
│   ├── routes.py          # Flask web + API routes
│   ├── rewriting.py       # Rewriting logic with LLM
│   ├── chat.py            # Chatbot engine + history logging
│   ├── utils.py           # CV file parsing helpers
│
├── static/
│   ├── style.css
│   └── chat_log.json      # Chat history (JSON)
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── chat.html
│
├── run.py
├── test_api.py            # Python test script for API
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Locally

```bash
# Activate virtual environment
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# Start server
flask run
```

---

## API Testing Tools
* Python script (`test_api.py`)
* curl from terminal

---

## Project Status

* Fully functional web app
* LLM-powered rewriting & chatbot
* API endpoints tested and working
* Planned: PDF export, user sessions, internationalization

---

## Author

**Miguel Ángel Carrillo Cobián**
Montreal, Canada
📧 [ma.carrillo.cobian@gmail.com](mailto:ma.carrillo.cobian@gmail.com)
🔗 [LinkedIn](https://linkedin.com/in/macarrillocobian/)
💻 [GitHub](https://github.com/ma-carrillo)

---
