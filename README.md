# 🎬 Movie Recommendation System

A Content-Based Movie Recommendation System built using Machine Learning and Streamlit.  
It recommends movies based on similarity of tags using NLP techniques like TF-IDF and Cosine Similarity.

## 📌 Project Overview

This project recommends movies based on the content similarity of:
- Genres
- Keywords
- Cast
- Crew (Director)
- Overview

It uses **Natural Language Processing (NLP)** and **Cosine Similarity** to find movies similar to the selected one.

## 🧠 Machine Learning Concept

- Data Preprocessing
- Feature Engineering (tags creation)
- TF-IDF / Count Vectorization
- Cosine Similarity

---

## 📂 Dataset

- TMDB 5000 Movies Dataset
- TMDB Credits Dataset

---

## ⚙️ Tech Stack

- Python 🐍
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Requests (for API)
- TMDB API (for movie posters)

---

## 🔥 Features

- Select a movie from dropdown
- Get top 5 similar movies
- Display movie posters
- Fast and interactive UI
- Clean Streamlit web app

---

## 🏗️ Project Workflow

1. Data Cleaning & Merging
2. Feature Extraction (genres, keywords, cast, crew)
3. Tag creation (NLP processing)
4. Vectorization using TF-IDF / CountVectorizer
5. Cosine Similarity calculation
6. Recommendation function
7. Streamlit web app

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Anup-Dhungel/movie-recommendation-system.git
cd movie-recommendation-system
