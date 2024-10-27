# services/reaction_service.py
from firebase_setup import db
from models.reaction_model import update_reaction

def add_reaction_to_post(post_id, reaction):
    try:
        post_ref = db.collection('posts').document(post_id)
        post = post_ref.get()
        
        if post.exists:
            post_data = post.to_dict()
            post_data = update_reaction(post_data, reaction)
            post_ref.update(post_data)
            print(f"Reaction added to post {post_id}.")
        else:
            print("Post not found.")
    except Exception as e:
        print(f"Error adding reaction: {e}")
