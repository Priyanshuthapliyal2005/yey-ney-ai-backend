from flask import Flask
from routes.user_routes import user_routes

app = Flask(__name__)
app.register_blueprint(user_routes)

@app.route('/')
def home():
    return "Welcome to the Yey Ney AI Backend!"

if __name__ == '__main__':
    app.run(debug=True)
