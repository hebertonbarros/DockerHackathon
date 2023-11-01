from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import pandas as pd


app = Flask(__name__)
CORS(app)  # Initialize CORS with the app


sample_data = [
    { "log": "Email sent to SpaceExplorer65 with subject: Exclusive Offer: Upgrade Now!!!", "sentiment": "info" },
    { "log": "API request failed: DELETE /api/delete - 401 Unauthorized", "sentiment": "error" },
    { "log": "Failed login attempt for user DEBUG from IP MidnightHawk", "sentiment": "warning" },
    { "log": "API request failed: PUT /api/resource - 500 Internal Server Error", "sentiment": "error" },
]

model = joblib.load('model_logs.joblib')
tfidf_vectorizer = joblib.load('tfidf_vectorizer.joblib')

@app.route('/')
def hello_world():
    return 'Hello, World!'    

@app.route('/api/analyzeLogs', methods=['POST'])
def analyze_logs():
    if request.method == 'POST':
        data = request.get_json()

        # Assuming 'log_data' is passed as a list in the JSON request
        log_data = data.get('log_data', None)
        # print(type(log_data))

        log_df = pd.DataFrame(log_data)

        if log_data is not None:
            # Call your prediction function
            result = model.predict(tfidf_vectorizer.transform(log_df['Log'])) #.tolist())

            log_df['predicted_sentiment'] = result
            # print(log_df)
            json_data = log_df.to_json(orient='records')
            # Create a JSON response with the prediction result
            response = {'result': json_data}
            return jsonify(response)
        else:
            return jsonify({'error': 'Invalid input data'}), 400  # Bad Request
    else:
        return jsonify({'error': 'Invalid request method'}), 405  # Method Not Allowed


if __name__ == '__main__':
    app.run(port=3010, debug=True)
