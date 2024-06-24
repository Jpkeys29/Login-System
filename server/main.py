from flask import Flask;
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route('/')
def home():
    return "Login System"

if __name__ == '__main__':
    app.run(debug=True)