from datetime import datetime
from models.post_model import PostModel  # Import PostModel instead of Post

class PostService:

    @staticmethod
    def create_post(media, place, friend_group, sentence, music_id, is_private, user_id):
        # Logic to save the post goes here
        post_id = "new_post_id"  # Replace with a generated ID from your database
        
        new_post = PostModel(  # Use PostModel
            post_id=post_id,
            user_id=user_id,
            title=sentence,
            url=f"https://example.com/post/{post_id}",
            share_url=f"https://g.example.com/{post_id}",
            thumbnail_image="https://example.com/thumbnails/image.jpg",
            main_image="https://example.com/images/image.jpg",
            video_link=None,
            main_sentence=sentence,
            allow_reactions=True,
            language="en-US",
            location=place,
            music_link=music_id,
            filter_style="default",
            yey=0,
            ney=0,
            comments={"count": 0, "content": []},
            created_at=datetime.utcnow().isoformat() + "Z",
            updated_at=datetime.utcnow().isoformat() + "Z"
        )

        # Return a success message
        return {
            "success": True,
            "post_id": new_post.post_id,
            "message": "Post created successfully.",
            "post": new_post  # Optionally include the post data
        }

    @staticmethod
    def get_all_posts(limit=10, offset=0, sort="newest"):
        # Placeholder for getting all posts with pagination and sorting
        mock_posts = [
            PostModel(  # Use PostModel
                post_id=f"post_{i}",
                user_id="user_id_placeholder",
                title=f"Post {i}",
                url=f"https://example.com/post/{i}",
                share_url=f"https://g.example.com/{i}",
                thumbnail_image="https://example.com/thumbnails/image.jpg",
                main_image="https://example.com/images/image.jpg",
                video_link=None,
                main_sentence=f"Sample sentence for post {i}",
                allow_reactions=True,
                language="en-US",
                location="Sample location",
                music_link="sample_music_id",
                filter_style="default",
                yey=0,
                ney=0,
                comments={"count": 0, "content": []},
                created_at=datetime.utcnow().isoformat() + "Z",
                updated_at=datetime.utcnow().isoformat() + "Z"
            ) for i in range(offset, offset + limit)
        ]

        return {"success": True, "posts": mock_posts, "total": len(mock_posts)}

    @staticmethod
    def get_post_by_id(post_id):
        # Logic to retrieve a post by ID goes here
        mock_post = PostModel(  # Use PostModel
            post_id=post_id,
            user_id="user_id_placeholder",
            title="Sample Post",
            url=f"https://example.com/post/{post_id}",
            share_url=f"https://g.example.com/{post_id}",
            thumbnail_image="https://example.com/thumbnails/image.jpg",
            main_image="https://example.com/images/image.jpg",
            video_link=None,
            main_sentence="This is a sample post",
            allow_reactions=True,
            language="en-US",
            location="Sample location",
            music_link="sample_music_id",
            filter_style="default",
            yey=0,
            ney=0,
            comments={"count": 0, "content": []},
            created_at=datetime.utcnow().isoformat() + "Z",
            updated_at=datetime.utcnow().isoformat() + "Z"
        )

        return {"success": True, "post": mock_post}

    @staticmethod
    def update_post(post_id, post_data, user_id):
        # Logic to update a post by ID
        updated_post = PostModel(  # Use PostModel
            post_id=post_id,
            user_id=post_data.get("user_id", "user_id_placeholder"),  # Get user_id from post_data
            title=post_data.get("title", ""),
            url=post_data.get("url", ""),
            share_url=post_data.get("share_url", ""),
            thumbnail_image=post_data.get("thumbnail_image", ""),
            main_image=post_data.get("main_image", ""),
            video_link=post_data.get("video_link", None),
            main_sentence=post_data.get("main_sentence", ""),
            allow_reactions=post_data.get("allow_reactions", True),
            language=post_data.get("language", "en-US"),
            location=post_data.get("location", {}),
            music_link=post_data.get("music_link", None),
            filter_style=post_data.get("filter_style", "default"),
            yey=post_data.get("yey", 0),
            ney=post_data.get("ney", 0),
            comments=post_data.get("comments", {"count": 0, "content": []}),
            created_at=post_data.get("created_at", datetime.utcnow().isoformat() + "Z"),
            updated_at=datetime.utcnow().isoformat() + "Z"
        )

        # Return a success message with updated data
        return {
            "success": True,
            "post_id": post_id,
            "message": "Post updated successfully.",
            "post": updated_post
        }

    @staticmethod
    def delete_post(post_id, user_id):
        # Logic to delete a post by ID
        return {
            "success": True,
            "post_id": post_id,
            "message": "Post deleted successfully."
        }
