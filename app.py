import flask
from flask import Flask, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/api/data')
def data():
    return jsonify({'message': 'Hello, World!', 'status': 'success'})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)