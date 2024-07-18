from flask import Flask, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt

app= Flask(__name__)
cors = CORS(app)

@app.route('/register', methods=['POST'])
def register():
    user_data = request.get_json()
    print(user_data)
    return user_data

if __name__ == "__main__":
    app.run(debug=True)

