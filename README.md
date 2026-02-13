# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using Python and Streamlit that recommends similar movies based on user selection. The system uses a precomputed similarity matrix and dynamically fetches movie posters using the TMDB API for an interactive experience.

---

## ✨ Features

- Content-based movie recommendations  
- Fuzzy matching for similar movie titles  
- Interactive Streamlit web application  
- Real-time movie posters using TMDB API  
- Fast recommendations using saved similarity data  

---

## 🛠️ Technologies Used

- Python  
- Streamlit  
- Pandas  
- Pickle  
- Requests  
- TMDB API  

---

## 📁 Project Structure

```bash
  RECOMMENDATION_SYSTEM/
  │
  ├── .ipynb_checkpoints/
  │   ├── dataset1-checkpoint.csv
  │   └── Untitled-checkpoint.ipynb
  │
  ├── data.xls
  ├── dataset.csv
  ├── dataset1.csv
  │
  ├── main.py
  ├── movies_list.pkl
  ├── similarity.pkl
  │
  └── Untitled.ipynb
```


## 🚀 How to Run the Project

### 1️⃣ Install required libraries

```bash
pip install streamlit pandas numpy scikit-learn requests

```
## 📊 Dataset Acknowledgment

The movie data used in this project is sourced from the TMDB Movies Dataset provided by The Movie Database (TMDB).  
This dataset includes comprehensive movie metadata and is commonly used for educational and research purposes.

All poster images are fetched in real time using the TMDB API.

Credits go to TMDB for maintaining and providing this valuable resource.
