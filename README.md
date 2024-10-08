
# Content-Based Movie Recommendation System

## Overview![Screenshot 2024-08-03 213838](https://github.com/user-attachments/assets/38b877f7-0bcc-4db7-98ae-3e9bcd23ba5d)


This repository contains a content-based movie recommendation system that suggests movies to users based on their preferences. By leveraging movie metadata such as genres, cast, crew, and plot descriptions, the system can recommend movies that are similar to the ones users have enjoyed in the past.

## Features

- **Personalized Recommendations**: Provides movie suggestions tailored to individual user preferences.
- **Interactive Interface**: Built using Streamlit to display recommended movies and detailed information.
- **Data Cleaning and Preprocessing**: Utilizes the TMDB dataset from Kaggle for comprehensive movie metadata.
- **Advanced Similarity Calculations**: Implements TF-IDF Vectorizer and Cosine Similarity to compare and recommend movies.
![Screenshot 2024-08-03 213916](https://github.com/user-attachments/assets/2a56d14c-04c4-4fcb-b1b7-b1d8883bc93d)
![Screenshot 2024-08-03 214032](https://github.com/user-attachments/assets/a7a7e7a4-e06b-4e20-b67b-e901ab77ba36)

## Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Streamlit**
- **Scikit-learn**

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/movie-recommendation-system.git
    cd movie-recommendation-system
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

## Usage

1. Start the Streamlit app by following the installation steps above.
2. The main interface will allow users to input their movie preferences.
3. The system will display a list of recommended movies based on the input preferences.
4. Users can view detailed information about each recommended movie.

## Dataset

The recommendation system uses the TMDB dataset from Kaggle, which includes detailed metadata for movies such as genres, cast, crew, and descriptions.

## How It Works

1. **Data Collection**: Collects detailed information about movies from the TMDB dataset.
2. **Feature Extraction**: Extracts relevant features (e.g., genres, keywords, descriptions) from the dataset.
3. **Profile Building**: Creates a user profile based on the features of movies the user has rated or liked.
4. **Similarity Calculation**: Uses TF-IDF Vectorizer and Cosine Similarity to calculate the similarity between movies.
5. **Recommendation Generation**: Suggests movies that are most similar to the user's profile.
6. **Interactive Interface**: Displays the recommended movies using Streamlit.

## Example Workflow
![Uploading Screenshot 2024-08-03 213936.png…]()

1. **User Rates Movies**: A user rates several movies.
2. **System Updates Profile**: The system updates the user’s profile based on these ratings.
3. **Generates Recommendations**: The system calculates similarity scores between the user's profile and other movies in the database.
4. **Displays Recommendations**: The system presents a list of recommended movies through the Streamlit interface.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or new features to add.


