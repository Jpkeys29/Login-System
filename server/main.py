from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
from sqlalchemy import create_engine  # Import create_engine
from flask_bcrypt import Bcrypt

app = Flask(__name__)
cors = CORS(app, origins='*')
bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:Dor!ta0822@localhost/user_login'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
   useID = db.Column(db.Integer, primary_key = True)
   first_name = db.Column(db.String(45), nullable = False)
   last_name = db.Column(db.String(45), nullable = False)
   email = db.Column(db.String(45), nullable = False, unique= True)
   password = db.Column(db.String(150), nullable=False)  

try:
  # Update connection URI for PostgreSQL
  engine = create_engine('postgresql://root:Dor!ta0822@localhost/user_login')
  print("Connection to PostgreSQL database successful!")
except OperationalError as err:
  print("Error connecting to PostgreSQL database:", err)

@app.route('/', methods=['POST'])
def home():
    data = request.get_json()
    print(type(data))

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')

    # Hash the password using bcrypt before storing it
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create a new user and add to the database
    new_user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully', 'user': {
        'first_name': first_name,
        'last_name': last_name,
        'email': email
    }}), 201

@app.route('/dashboard')
def dashboard():
    return 'Hola'

if __name__ == '__main__':
    app.run(debug=True)