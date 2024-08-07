from flask import Flask, request, jsonify, redirect, flash, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
from datetime import datetime, timezone
from flask_login import current_user

app= Flask(__name__)  #Creates a Flask application instance
cors = CORS(app)  #Allows interaction between different domains
bcrypt = Bcrypt(app) #Initializes Bcrypt object for password hashing
load_dotenv()

server_email = os.getenv('SERVER_EMAIL')
server_password = os.getenv('SERVER_PASSWORD')


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:Dor!ta0822@localhost/user_login" #Specifies the location of the local sql database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['SECRET_KEY'] = 'Racecar' #Used for various security purposes
app.config['JWT_SECRET_KEY'] = 'GOT24' #Used for signing and veryfing JWTs
app.config['JWT_TOKEN_LOCATION'] = ['headers'] #Specifies where JWT will be located

db = SQLAlchemy(app)  #Creates a db instance
jwt = JWTManager(app) #Initializes a JWTManager instance and binds it to the Flask application
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable = False)
    last_name = db.Column(db.String(45), nullable = False)
    email = db.Column(db.String(45), nullable = False, unique= True)
    username = db.Column(db.String(45), nullable = False)
    password = db.Column(db.String(150), nullable=False) 
    is_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True, default=None)

class Config(object):
    MAIL_DEFAULT_SENDER = os.getenv('SERVER_EMAIL')
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('SERVER_EMAIL')
    MAIL_PASSWORD = os.getenv('SERVER_PASSWORD')
    MAIL_DEBUG = True
 
app.config.from_object(Config())
mail = Mail(app)
    
def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=os.getenv('SERVER_EMAIL'),
    )
    mail.send(msg)

def generate_token(email):
    serializer = URLSafeTimedSerializer("Hod2024")
    return serializer.dumps(email)

def confirm_token(token, expiration=7200):
    serializer = URLSafeTimedSerializer("Hod2024")
    try:
        email = serializer.loads( token, max_age=expiration)
        return email
    except Exception:
        return False
    
@app.route('/register', methods=['GET','POST'])
def register():
    user_data = request.get_json()
    print(user_data)
    first_name = user_data.get('first_name')
    last_name = user_data.get('last_name')
    email = user_data.get('email')
    username = user_data.get('username')
    password = user_data['password']
    is_confirmed = user_data.get('is_confirmed', False)
    confirmed_on = None

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8') #Hashing password before storing it

    new_user = User(first_name=first_name, last_name=last_name, email=email, username=username, password=hashed_password, is_confirmed=is_confirmed, confirmed_on=datetime.now(timezone.utc)) #Adding new user to db
    db.session.add(new_user)
    db.session.commit()

    token = generate_token(new_user.email)
    confirm_url = url_for("confirm_email", token=token, _external=True)
    html = render_template("confirm_email.html", confirm_url=confirm_url)
    subject = "Please confirm your email"
    send_email(new_user.email, subject, html)

    # login_user(user_data)
    return jsonify({ 'message' : 'User created successfully and confirmation email sent', 'user': {
        'first_name': first_name,
        'last_name' : last_name,
        'email' : email,
        'username' : username,
        'is_confirmed': is_confirmed,
        'confirmed_on' : confirmed_on
    }}), 201
   

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    print('Received data:', username, password)

    user = User.query.filter_by(username=username).first()  #User verification

    if user and bcrypt.check_password_hash(user.password, password):  #Authentication check
        access_token = create_access_token(identity=user.id)
        print(access_token)
        return jsonify({'message' : 'Login Success', 'access_token' : access_token})
    else:
        return jsonify({'message' : 'Login Failed'}), 401
    
    
@app.route('/get_name', methods=['GET'])
@jwt_required()
def get_name():
    # Extract the user ID from the JWT
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()

    if user:
        return jsonify({'message' : 'User found', 'First_name': user.first_name, 'Last_name': user.last_name, 'Username': user.username })
    else:
        return jsonify({'message' : 'User not found'}), 404
    
@app.route('/api/confirm', methods=['GET'])
def confirm_email():
    token = request.args.get('token')
    email = confirm_token(token)
    user = User.query.filter_by(email = email).first_or_404()
    user.is_confirmed = True
    user.confirmed_on = datetime.now()
    db.session.add(user)
    db.session.commit()
    return jsonify({'success' : True, 'redirect_url' : '/dashboard'})


if __name__ == "__main__": 
    with app.app_context():   #Creates a db if it does not exist
        db.create_all()
    app.run(debug=True)

