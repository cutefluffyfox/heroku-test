from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/')
def main_page():
    return jsonify({'ip': request.remote_addr})


app.run()
