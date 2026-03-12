# 🎬 Movie Recommendation System

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Latest-150458?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Latest-013243?style=flat&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Latest-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-Latest-2CA5E0?style=flat&logo=python&logoColor=white)
![TMDB](https://img.shields.io/badge/TMDB-API-01B4E4?style=flat&logo=themoviedatabase&logoColor=white)
![ML](https://img.shields.io/badge/ML-Content--Based%20Filtering-blueviolet?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)


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
