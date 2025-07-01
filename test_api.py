# test_api.py

import requests

BASE = "http://127.0.0.1:5000"

def test_rewrite_endpoint():
    response = requests.post(f"{BASE}/api/rewrite", json={
        "cv_lines": [
            "I helped with campaigns",
            "Made PowerPoints",
            "Improved email open rate by 20%"
        ],
        "job_description": "Looking for a marketing intern who can assist with email campaigns and content creation."
    })
    assert response.status_code == 200
    assert "rewritten_cv" in response.json()

def test_chat_endpoint():
    response = requests.post(f"{BASE}/api/chat", json={
        "prompt": "What should I write in my CV objective?"
    })

    # If the status code is not 200, print full response
    if response.status_code != 200:
        print("\n/api/chat failed", flush=True)
        print("Status Code:", response.status_code, flush=True)
        try:
            print("Response JSON:", response.json(), flush=True)
        except Exception as e:
            print("Failed to parse JSON. Raw text:", flush=True)
            print(response.text, flush=True)

    assert response.status_code == 200
    assert "response" in response.json()


def test_chat_history_get():
    response = requests.get(f"{BASE}/api/chat/history")
    assert response.status_code == 200
    assert "history" in response.json()

def test_chat_history_delete():
    response = requests.delete(f"{BASE}/api/chat/history")
    assert response.status_code in [200, 404]  # Allow both if no history exists
