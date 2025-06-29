
# 🎬 Movie Review Sentiment Classifier

### Predict the Sentiment of Movie Reviews using Deep Learning  
A web application that analyzes the sentiment (Positive/Negative) of movie reviews using an LSTM-based neural network trained on the IMDB dataset. Built with TensorFlow and deployed via a user-friendly interface powered by Streamlit and Flask.

---

## 📑 Table of Contents
- [Introduction](#introduction)  
- [Features](#features)  
- [How It Works](#how-it-works)  
- [Technologies Used](#technologies-used)  
- [Screenshots](#screenshots)  
- [Installation](#installation)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [License](#license)  
- [Acknowledgements](#acknowledgements)  

---

## 📌 Introduction

The **Movie Review Sentiment Classifier** is a deep learning-based project that classifies user-input movie reviews as either **Positive** or **Negative**. The model uses **LSTM (Long Short-Term Memory)** layers for learning from sequential data and is trained on 50,000 movie reviews from the [IMDB dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews).

This project aims to simulate a real-world ML pipeline by including:
- Model training
- Saving/loading `.h5` and `tokenizer.pkl`
- Flask API serving predictions
- Streamlit UI for interactive review submission

---

## 🚀 Features

- 🎯 **Accurate Classification** — Achieves 89.02% accuracy on test data  
- 🧠 **Deep Learning Model** — Uses an LSTM layer for text sequence modeling  
- ⚙️ **Real-time Predictions** — Integrated Flask backend for API handling  
- 💡 **Streamlit UI** — Intuitive interface for sentiment prediction  
- 📦 **Pretrained Model Support** — Load and predict using `sentiment_model.h5` and `tokenizer.pkl`  
- 📝 **Confidence Score Output** — Displays sentiment with prediction confidence

---

## 🔎 How It Works

1. **User Input**: Enter any movie review in the Streamlit UI  
2. **Preprocessing**: Tokenized and padded to match model input  
3. **Prediction**: The LSTM model outputs a sentiment score  
4. **Output**: Displays **Positive** or **Negative** label with emoji and confidence

---

## 🛠️ Technologies Used

| Category       | Tools & Frameworks                      |
|----------------|-----------------------------------------|
| **Language**   | Python 3.10                             |
| **Model**      | TensorFlow, Keras                       |
| **UI**         | Streamlit                              |
| **API**        | Flask                                  |
| **Data**       | IMDB Movie Review Dataset (Kaggle)     |
| **Others**     | NumPy, Pandas, Scikit-learn, Matplotlib |

---

## 🖼️ Screenshots

### ✅ Positive Review  
![WhatsApp Image 2025-06-20 at 05 12 07_55b0150e](https://github.com/user-attachments/assets/afad0d4b-bbda-4672-88ed-ebefa3acef8e)

### ❌ Negative Review   
![Negative](![WhatsApp Image 2025-06-20 at 05 15 36_14f4911b](https://github.com/user-attachments/assets/8ee888f2-edca-44ef-894e-1713adee8e57)
)

### 😕 Negative Review   
![WhatsApp Image 2025-06-20 at 05 15 12_0ff61c0d](https://github.com/user-attachments/assets/53297d48-7b44-49e0-bed1-c5228fb0b2c1)


---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/sentimentAnalysis.git
cd sentimentAnalysis
```

### 2. Create a Virtual Environment
```bash
conda create -n sentiment_env python=3.10
conda activate sentiment_env
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Flask API
```bash
python app.py
```

### 5. Run Streamlit App (New Terminal)
```bash
streamlit run streamlit_app.py
```

---

## 🧱 Project Structure

```
.
├── model/
│   ├── sentiment_model.h5
│   └── tokenizer.pkl
├── app.py
├── utils.py
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

## 👩‍💻 Contributing

Feel free to fork this repository and open pull requests. Suggestions and improvements are always welcome!

---



## 🙏 Acknowledgements

- **Dataset**: [IMDB Dataset of 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
- **Frameworks**: TensorFlow, Keras, Streamlit, Flask  
- **Inspiration**: Real-world NLP use cases in production APIs  
