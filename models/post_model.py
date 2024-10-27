# models/post_model.py
from datetime import datetime

def post_data_structure(user_id, title, main_sentence, media_url, location):
    return {
        "_id": f"{user_id}-{datetime.utcnow().timestamp()}",
        "status": "live",
        "user_id": user_id,
        "title": title,
        "url": f"https://yeyney.com/{user_id}/{title.replace(' ', '-')}",
        "media": {
            "type": "image",  # or "video"
            "url": media_url,
        },
        "main_sentence": main_sentence,
        "location": location,
        "allow_reactions": True,
        "yey": 0,
        "ney": 0,
        "created_at": datetime.utcnow().isoformat()
    }
