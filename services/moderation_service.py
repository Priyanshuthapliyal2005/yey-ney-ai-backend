# services/moderation_service.py
import requests

def check_content_moderation(media_url):
    api_url = "https://vision-api-example.com/check"
    data = {
        "media": {
            "type": "image",
            "url": media_url
        },
        "options": {
            "detect_violence": True,
            "detect_sexual_content": True
        }
    }
    response = requests.post(api_url, json=data)
    return response.json()
