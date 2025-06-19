# app.py
from flask import Flask, request, jsonify
import tensorflow as tf
from utils import preprocess_text

app = Flask(__name__)

# Load model
model = tf.keras.models.load_model('model/sentiment_model.h5')

@app.route('/')
def index():
    return "Welcome to the Sentiment Analysis API!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    review = data['text']
    processed = preprocess_text(review)
    prediction = model.predict(processed)[0][0]

    sentiment = 'Positive' if prediction > 0.5 else 'Negative'

    return jsonify({
        'review': review,
        'sentiment': sentiment,
        'confidence': float(prediction)
    })

if __name__ == '__main__':
    app.run(debug=True)
