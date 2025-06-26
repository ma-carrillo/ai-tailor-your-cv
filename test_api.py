import requests

BASE = "http://127.0.0.1:5000"

# ✅ Test /api/chat
print("=== /api/chat ===")
chat = requests.post(f"{BASE}/api/chat", json={
    "prompt": "What should I write in my CV objective?"
})
print(chat.status_code)
print(chat.json())
print()

# ✅ Test /api/rewrite
print("=== /api/rewrite ===")
rewrite = requests.post(f"{BASE}/api/rewrite", json={
    "cv_lines": [
        "I helped with campaigns",
        "Made PowerPoints",
        "Improved email open rate by 20%"
    ],
    "job_description": "Looking for a marketing intern who can assist with email campaigns and content creation."
})
print(rewrite.status_code)
print(rewrite.json())
print()

# ✅ Test /api/chat/history (GET)
print("=== GET /api/chat/history ===")
history = requests.get(f"{BASE}/api/chat/history")
print(history.status_code)
print(history.json())
print()

# ✅ Test /api/chat/history (DELETE)
print("=== DELETE /api/chat/history ===")
delete = requests.delete(f"{BASE}/api/chat/history")
print(delete.status_code)
print(delete.json())
