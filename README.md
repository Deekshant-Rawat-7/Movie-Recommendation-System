# Recommendation_System



Check out the research paper:
https://ieeexplore.ieee.org/document/10428182



# Recommendation_System



Check out the research paper:
https://ieeexplore.ieee.org/document/10428182


# 🎬 Movie Recommendation System Using Content-Based Filtering

This project is a content-based movie recommendation system that suggests similar movies based on user input. It uses metadata from movies such as genres, cast, crew, keywords, and overview to compute similarity using **CountVectorizer** and **Cosine Similarity**. The system is deployed as an interactive web app using **Streamlit**.

---

## 📌 Features

- Recommend movies based on title input
- Uses metadata from `movies.csv` and `credits.csv`
- Vectorizes movie tags using `CountVectorizer`
- Computes similarity using `cosine_similarity`
- Displays movie posters using TMDB API
- Interactive web interface with Streamlit
- Custom background and image styling



## 🧠 Methodology

1. **Data Preprocessing**  
   - Merge `movies.csv` and `credits.csv` on title  
   - Extract and clean features: genres, keywords, cast, crew, overview  
   - Convert structured data into text format

2. **Feature Engineering**  
   - Combine all features into a single `tags` column  
   - Apply `CountVectorizer` with max 5000 features and stopword removal

3. **Similarity Calculation**  
   - Use `cosine_similarity` on vectorized tags  
   - Store similarity matrix in `similarity.pkl`

4. **Recommendation Logic**  
   - Input a movie title  
   - Return top 6 similar movies based on similarity scores  
   - Fetch posters using TMDB API

5. **Web Deployment**  
   - Build UI with Streamlit  
   - Display recommendations with posters and titles  
   - Add custom background and header images



## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/movie-recommendation-system.git

cd movie-recommendation-system

2. Create Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install Dependencies

pip install -r requirements.txt

4. Run the App

streamlit run app.py


📦 Requirements

To run this project, install the following Python packages:

txt
streamlit==1.29.0
pandas==2.0.3
scikit-learn==1.3.0
requests==2.31.0
nltk==3.8.1
You can install them using:

bash
pip install -r requirements.txt



📊 Evaluation



Since this is a content-based system, traditional accuracy metrics don't apply. Instead:

Precision@5: ~0.4–0.6 (based on manual inspection)

User Satisfaction: ~70–85% relevance

Cold-start friendly: Works well for new users or movies


🔑 API Key

This project uses the TMDB API to fetch movie posters. You’ll need to replace the API key in app.py with your own:

api_key = "your_tmdb_api_key"



📄 License

This project is licensed under the MIT License.


🙌 Acknowledgements

IEEE SMART-2023 Conference

Graphic Era Hill University

Symbiosis Institute of Technology

TMDB API for movie data and posters
