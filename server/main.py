from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route('/', methods=['POST'])

def home():
    data = request.get_json()

    print(type(data))
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')

    return (data)

if __name__ == '__main__':
    app.run(debug=True)