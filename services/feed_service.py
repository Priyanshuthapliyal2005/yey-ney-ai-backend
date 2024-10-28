# services/feed_service.py
from models.post_model import Post

def get_discovery_feed(user_id, language, location, interests):
    # This function would typically interact with the database
    # and return a list of posts based on the criteria.
    sample_post = {
        "_id": "unique_post_id",
        "user_id": "unique_user_id",
        "title": "Should I buy this Chanel bag?",
        "url": "https://yeyney.com/{user}/should-i-buy-this-chanel-bag",
        "share_url": "https://g.yeyney.cto/7fhdjhksdf",
        "thumbnail_image": "https://example.com/thumbnails/mountain.jpg",
        "main_image": "https://example.com/images/mountain.jpg",
        "video_link": "https://example.com/videos/mountain.mp4",
        "main_sentence": "An unforgettable hike through the breathtaking mountains.",
        "allow_reactions": True,
        "language": "en-US",
        "location": {
            "lat": 34.052235,
            "long": -118.243683,
            "friendly_name": "Griffith Park, Los Angeles",
            "country": "US"
        },
        "music_link": "https://example.com/music/hike_theme.mp3",
        "filter_style": "vintage",
        "yey": 0.2,
        "ney": 0.7,
        "comments": {
            "count": 20,
            "content": [
                {
                    "avatarUrl": "https://example.com/avatars/jane.jpg",
                    "username": "Jane Doe",
                    "comment_content": "I love this ❤️"
                }
            ]
        },
        "created_at": "2024-08-09T00:00:00Z",
        "updated_at": "2024-08-09T00:00:00Z"
    }

    posts = [Post.from_dict(sample_post)]
    return {"posts": [post.__dict__ for post in posts]}

def get_user_feed(user_id, post_id):
    # Similar logic can be implemented to retrieve user's specific posts
    return {"message": "User's feed retrieved successfully."}
