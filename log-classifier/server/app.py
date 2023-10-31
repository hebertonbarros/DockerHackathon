from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Initialize CORS with the app


sample_data = [
    { "log": "Email sent to SpaceExplorer65 with subject: Exclusive Offer: Upgrade Now!!!", "sentiment": "info" },
    { "log": "API request failed: DELETE /api/delete - 401 Unauthorized", "sentiment": "error" },
    { "log": "Failed login attempt for user DEBUG from IP MidnightHawk", "sentiment": "warning" },
    { "log": "API request failed: PUT /api/resource - 500 Internal Server Error", "sentiment": "error" },
]

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/analyzeLogs', methods=['GET'])
def analyze_logs():
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(port=3010, debug=True)
