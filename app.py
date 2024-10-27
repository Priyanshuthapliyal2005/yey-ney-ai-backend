# app.py
from flask import Flask
from routes.user_routes import user_routes
from routes.post_routes import post_routes
from routes.reaction_routes import reaction_routes
from routes.moderation_routes import moderation_routes

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(user_routes)
app.register_blueprint(post_routes)
app.register_blueprint(reaction_routes)
app.register_blueprint(moderation_routes)

if __name__ == "__main__":
    app.run(debug=True)
