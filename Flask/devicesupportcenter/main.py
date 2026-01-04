from flask import Flask, jsonify
from db import repair_center

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"message": "Welcome to Service Center API"}), 200

@app.route('/devices')
def get_all_devices():
    return jsonify({})
if __name__ == "__main__":
    app.run()