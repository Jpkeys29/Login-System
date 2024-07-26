from flask import Flask, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt

app= Flask(__name__)  #Creates a Flask application instance
cors = CORS(app)  #Allows interaction between different domains
bcrypt = Bcrypt(app) #Initializes Bcrypt object for password hashing

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

@app.route('/register', methods=['POST'])
def register():
    user_data = request.get_json()
    print(user_data)

    first_name = user_data.get('first_name')
    last_name = user_data.get('last_name')
    email = user_data.get('email')
    username = user_data.get('username')
    password = user_data['password']

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8') #Hashing password before storing it

    new_user = User(first_name=first_name, last_name=last_name, email=email, username=username, password=hashed_password) #Adding new user to db
    db.session.add(new_user)
    db.session.commit()

    return jsonify({ 'message' : 'User created successfully', 'user': {
        'first_name': first_name,
        'last_name' : last_name,
        'email' : email,
        'username' : username
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
        return jsonify({'message' : 'User found', 'First name' : user.first_name, 'Last Name' : user.last_name, 'Username' : user.username })
    else:
        return jsonify({'message' : 'User not found'}), 404
    


if __name__ == "__main__": 
    with app.app_context():   #Creates a db if it does not exist
        db.create_all()
    app.run(debug=True)

