import flask
from flask import Flask, jsonify
from stock_info import stock_info

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    return 'Live Stock Data'

@app.route('/privacy')
def privacy():
    return 'Privacy Policy: We do not collect any information.'


@app.route('/api/data')
def data():
    return jsonify({'message': 'Hello, World!', 'status': 'success'})

@app.route('/api/stock/info/<string:ticker>', methods=['GET'])
def get_stock_info(ticker):
    try:
        info = stock_info(ticker)
        return jsonify(info)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)