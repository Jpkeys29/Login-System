from flask import Flask, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
import pymysql

app= Flask(__name__)  #Initializes the Flask application
cors = CORS(app)
bcrypt = Bcrypt(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:Dor!ta0822@localhost/user_login" #Specifying the location of the local sql database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)  #Creates a db instance

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable = False)
    last_name = db.Column(db.String(45), nullable = False)
    email = db.Column(db.String(45), nullable = False, unique= True)
    password = db.Column(db.String(150), nullable=False) 

@app.route('/register', methods=['POST'])
def register():
    user_data = request.get_json()
    print(user_data)

    first_name = user_data.get('first_name')
    last_name = user_data.get('last_name')
    email = user_data.get('email')
    password = user_data['password']

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8') #Hashing password before storing it

    new_user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password) #Adding new user to db
    db.session.add(new_user)
    db.session.commit()

    return jsonify({ 'message' : 'User created successfully', 'user': {
        'first_name': first_name,
        'last_name' : last_name,
        'email' : email
    }}), 201

if __name__ == "__main__": 
    with app.app_context():
        db.create_all()
    app.run(debug=True)

