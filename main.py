from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'Hello, World!'

    @app.route('/api/data')
    def data():
        return jsonify({'message': 'Hello, World!', 'status': 'success'})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)