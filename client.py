import requests

response = requests.post(
    "http://localhost:8000/chat",  # Changed from /essay/invoke to /chat/invoke
    json={'input': "Tell me about Promtior"}  # Changed input format to match input_type=str
)

print(response.json())