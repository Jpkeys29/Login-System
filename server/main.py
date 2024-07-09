from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
from sqlalchemy import create_engine  # Import create_engine

app = Flask(__name__)
cors = CORS(app, origins='*')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://@localhost/user_login'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

try:
  # Update connection URI for PostgreSQL
  engine = create_engine('postgresql://root:Dor!ta0822@localhost/user_login')
  print("Connection to PostgreSQL database successful!")
except OperationalError as err:
  print("Error connecting to PostgreSQL database:", err)


# class User(db.Model):


@app.route('/', methods=['POST'])
def home():
    data = request.get_json()
    print(type(data))

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')

    return (data)

@app.route('/dashboard')
def dashboard():
    return 'Hola'

if __name__ == '__main__':
    app.run(debug=True)