import streamlit as st
import tensorflow as tf
import numpy as np
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the model
model = tf.keras.models.load_model('model/sentiment_model.h5')

# Load the tokenizer
with open('model/tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

# Define max length for padding
max_len = 200  

# Streamlit app
st.title("🎬 Movie Review Sentiment Classifier")
st.write("This app classifies movie reviews as **Positive** or **Negative** using an LSTM model trained on IMDB data.")

# Input from user
user_input = st.text_area("Enter a movie review:", height=150)

if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a review to classify.")
    else:
        # Preprocess the text
        sequences = tokenizer.texts_to_sequences([user_input])
        padded = pad_sequences(sequences, maxlen=max_len)

        # Make prediction
        prediction = model.predict(padded)[0][0]
        sentiment = "Positive 😊" if prediction >= 0.5 else "Negative 😞"

        # Display result
        st.subheader("Prediction:")
        st.write(f"**{sentiment}** (Score: {prediction:.4f})")
