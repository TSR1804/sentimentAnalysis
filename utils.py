# utils.py
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load tokenizer
with open('model/tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

MAX_LEN = 200  # should match training

def preprocess_text(text):
    sequence = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequence, maxlen=MAX_LEN)
    return padded
