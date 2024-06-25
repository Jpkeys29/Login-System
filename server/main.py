from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route('/')
def home():
    return {
        "First_name":"first_name",
        "Last_name": "last_name",
        "Email" : "email",
    }

if __name__ == '__main__':
    app.run(debug=True)