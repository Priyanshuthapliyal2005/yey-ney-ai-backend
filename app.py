from flask import Flask, request, jsonify
import firebase_setup as fb

app = Flask(__name__)

# Initialize Firebase
fb.initialize_firebase()

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    username = data.get('username')
    dob = data.get('dob')
    contact_number = data.get('contact_number')
    
    # Construct user data
    user_data = fb.user_data_structure(email, username, dob, contact_number)
    
    # Create user
    result = fb.create_user(email, password, user_data)
    
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
