import requests

response = requests.post(
    "http://localhost:8000/chat/invoke", 
    json={'input': 
        
        ## change question in ""
        "Tell me about Promtior"
        }
)

print(response.json())