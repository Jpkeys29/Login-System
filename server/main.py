from flask import Flask, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt

app= Flask(__name__)  #Initializes the Flask application
cors = CORS(app)
bcrypt = Bcrypt(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:Dor!ta0822@localhost/user_login" #Specifying the location of the local sql database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# app.config['SECRET_KEY'] = 'Racecar'
# app.config['JWT_SECRET_KEY'] = 'GOT24'
# app.config['JWT_TOKEN_LOCATION'] = ['headers']

db = SQLAlchemy(app)  #Creates a db instance
# jwt = JWTManager(app)
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

# @app.route('/get_name', methods=['GET'])
# @jwt_required()
# def get_name():
#     # Extract the user ID from the JWT
#     user_id = get_jwt_identity()
#     user = User.query.filter_by(id=user_id).first()

#     if user:
#         return jsonify({'message' : 'User found', 'name' : user.name})
#     else:
#         return jsonify({'message' : 'User not found'}), 404
    
# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data['username']
#     password = data['password']
#     print('Received data:', username, password)

#     user = User.query.filter_by(username=username).first()

#     if user and bcrypt.check_password_hash(user.password, password):
#         access_token = create_access_token(identify=user.id)
#         return jsonify({'message' : 'Login Success', 'access_token' : access_token})
#     else:
#         return jsonify({'message' : 'Login Failed'}), 401
    


if __name__ == "__main__": 
    with app.app_context():   #Creates a db if it does not exist
        db.create_all()
    app.run(debug=True)

