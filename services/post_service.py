# services/post_service.py
from firebase_setup import db
from models.post_model import post_data_structure

def create_post(user_id, title, main_sentence, media_url, location):
    post_data = post_data_structure(user_id, title, main_sentence, media_url, location)
    db.collection('posts').document(post_data["_id"]).set(post_data)
    print(f"Post created with ID: {post_data['_id']}")
