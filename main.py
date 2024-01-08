from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/api/data')
def data():
    return jsonify({'message': 'Hello, World!', 'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True)