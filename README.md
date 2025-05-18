# 🎬 Movie Recommendation System

This is a content-based Movie Recommendation System built using Python. It suggests movies similar to the ones you like based on their features such as genres, overview, cast, crew, and keywords.

## 🚀 Features

- Recommend similar movies based on user input
- Uses NLP techniques to process and match movie metadata
- Clean UI using Streamlit for easy interaction
- Efficient similarity computation using cosine similarity

## 🧰 Tech Stack

- **Python 3**
- **Pandas, NumPy** – for data processing
- **Scikit-learn** – for feature extraction and similarity computation
- **NLTK** – for text preprocessing
- **Streamlit** – for web interface


## 🧠 How It Works

1. Combines key features like genres, cast, crew, and keywords into a single string ("tags").
2. Transforms the text data using **CountVectorizer** to get feature vectors.
3. Computes cosine similarity between these vectors.
4. When a user inputs a movie title, the app recommends the top 5 similar movies.

## ▶️ Getting Started

### Prerequisites

- Python 3.x
- Install required libraries:

