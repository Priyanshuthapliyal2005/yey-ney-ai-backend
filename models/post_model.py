# models/post_model.py
from datetime import datetime
from typing import Optional, Dict, List, Any

class PostModel:
    def __init__(self, post_id: str, user_id: str, title: str, url: str, share_url: str,
                 thumbnail_image: str, main_image: str, video_link: Optional[str],
                 main_sentence: str, allow_reactions: bool, language: str,
                 location: Dict[str, Any], music_link: Optional[str],
                 filter_style: str, yey: int, ney: int, comments: Dict[str, Any],
                 created_at: str, updated_at: str):
        
        self.post_id = post_id
        self.user_id = user_id
        self.title = title
        self.url = url
        self.share_url = share_url
        self.thumbnail_image = thumbnail_image
        self.main_image = main_image
        self.video_link = video_link
        self.main_sentence = main_sentence
        self.allow_reactions = allow_reactions
        self.language = language
        self.location = location  # Dictionary
        self.music_link = music_link
        self.filter_style = filter_style
        self.yey = yey
        self.ney = ney
        self.comments = comments  # Dictionary with count and content
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'PostModel':
        return PostModel(
            post_id=data.get('_id', ""),
            user_id=data.get('user_id', ""),
            title=data.get('title', ""),
            url=data.get('url', ""),
            share_url=data.get('share_url', ""),
            thumbnail_image=data.get('thumbnail_image', ""),
            main_image=data.get('main_image', ""),
            video_link=data.get('video_link', None),
            main_sentence=data.get('main_sentence', ""),
            allow_reactions=data.get('allow_reactions', True),
            language=data.get('language', "en-US"),
            location=data.get('location', {}),
            music_link=data.get('music_link', None),
            filter_style=data.get('filter_style', "default"),
            yey=data.get('yey', 0),
            ney=data.get('ney', 0),
            comments=data.get('comments', {"count": 0, "content": []}),
            created_at=data.get('created_at', datetime.utcnow().isoformat() + "Z"),
            updated_at=data.get('updated_at', datetime.utcnow().isoformat() + "Z")
        )
