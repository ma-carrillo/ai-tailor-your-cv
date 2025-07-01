
# CV Tailor Pro

**CV Tailor Pro** is a lightweight and intelligent web application that automatically rewrites your CV to match a specific job description. It supports both a traditional web interface and a RESTful API for programmatic access.

---

## Main Features

- **CV rewriting** using a transformer-based language model (`Flan-T5`).
- **Interactive chatbot** to answer CV improvement questions.
- **Conversation history** stored locally in JSON.
- **Web interface** built with Flask and HTML/CSS.
- **REST API** for backend integrations (POST, GET, DELETE).
- **Automated testing** with `pytest` using a custom script.
- **Container-ready** with `Dockerfile`.
- **CI/CD enabled** using GitHub Actions (`.yml` file in `.github/workflows`).

---

## Key Technologies & Skills

| Category        | Tools & Skills                                         |
|----------------|--------------------------------------------------------|
| Programming     | Python (Flask, requests), HTML, CSS                   |
| AI/ML           | Hugging Face Transformers, Flan-T5                    |
| API Design      | RESTful endpoints (`GET`, `POST`, `DELETE`)           |
| DevOps & CI/CD  | GitHub Actions, Docker                |
| Testing         | Pytest, automated test suite (`test_api.py`)          |
| Deployment      | Containerization-ready (Docker)                       |
| File Handling   | Uploads, parsing `.txt` files, JSON logging           |

---

## Web Interface Usage

1. Upload your CV as a plain `.txt` file.
2. Paste the job description you're targeting.
3. The app rewrites your CV to better align with the job.
4. Use the AI chatbot to ask specific CV improvement questions.

---

## 🔌 REST API Endpoints

| Method | Route                  | Description                               |
|--------|------------------------|-------------------------------------------|
| POST   | `/api/rewrite`         | Rewrite CV lines to match job             |
| POST   | `/api/chat`            | Ask the chatbot a career-related question |
| GET    | `/api/chat/history`    | Retrieve the chat history                 |
| DELETE | `/api/chat/history`    | Clear the chat history                    |

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

* Python script: `test_api.py` using `pytest`
* Python script: `test_api_manual.py` running it manually
* curl (command line)

---

## Docker Support

You can containerize the app using Docker:

```bash
docker build -t cv-tailor-pro .
docker run -p 5000:5000 cv-tailor-pro
```

---

## CI/CD with GitHub Actions

Every push triggers automated tests using `pytest` via GitHub Actions (`ci-cd.yml`).

This ensures API endpoints and functionality remain stable after changes.

---

## Author

**Miguel Ángel Carrillo Cobián**
Montreal, Canada
📧 [ma.carrillo.cobian@gmail.com](mailto:ma.carrillo.cobian@gmail.com)
🔗 [LinkedIn](https://linkedin.com/in/macarrillocobian/)
💻 [GitHub](https://github.com/ma-carrillo)

---