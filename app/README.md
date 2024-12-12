# Video Recommendation System

A personalized video recommendation system that suggests relevant content to users based on their preferences, mood, and engagement history. This project addresses challenges like cold-start recommendations and evaluates model performance with metrics such as MAE and RMSE.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Evaluation Metrics](#evaluation-metrics)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Features

- **Personalized Recommendations:** Provides video recommendations based on user history and mood.
- **Cold-Start Problem Handling:** Suggests videos for new users without prior engagement data.
- **Performance Metrics:** Evaluates recommendation quality using MAE and RMSE.
- **APIs:** Exposes endpoints for integration with other platforms.

---

## Project Structure

```
Video-Recommendations-
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── recommender.py
│   └── utils.py
├── data
│   ├── sample_videos.csv
│   └── user_data.csv
├── tests
│   ├── test_models.py
│   ├── test_recommender.py
│   └── test_utils.py
├── run.py
├── requirements.txt
├── Video_recommendation_Alog.ipynb
└── README.md
```

- **app/**: Contains the core application code (models, logic, utilities).
- **data/**: Stores the sample datasets for users and videos.
- **tests/**: Includes unit tests for the core application functions.
- **run.py**: The entry point to start the application.
- **Video_recommendation_Alog.ipynb**: Jupyter notebook for experimentation and development.
- **requirements.txt**: Lists all dependencies required to run the project.

---

## Setup Instructions

### Prerequisites

1. Python 3.8 or higher
2. Git
3. Virtual Environment (recommended)

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/Ranjeeth11/Video-Recommendations-.git
   cd Video-Recommendations-
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/MacOS
   venv\Scripts\activate     # For Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python run.py
   ```

---

## Usage

### Run the Jupyter Notebook

Explore the recommendation algorithm in the `Video_recommendation_Alog.ipynb` notebook:

```bash
jupyter notebook Video_recommendation_Alog.ipynb
```

### Test the APIs

Use tools like Postman or `curl` to test the API endpoints.

---

## API Endpoints

1. **Get Recommendations**

   - **Endpoint**: `/recommend`
   - **Method**: POST
   - **Description**: Returns 10 recommended videos for a user based on username, category, and mood.
   - **Payload Example**:
     ```json
     {
         "username": "user123",
         "category_id": 2,
         "mood": "happy"
     }
     ```

2. **Get User Data**

   - **Endpoint**: `/user/<username>`
   - **Method**: GET
   - **Description**: Retrieves user data for a given username.

3. **Get Category Videos**

   - **Endpoint**: `/category/<category_id>`
   - **Method**: GET
   - **Description**: Fetches a list of videos in the specified category.

---

## Evaluation Metrics

The recommendation model's performance was evaluated using:

1. **Mean Absolute Error (MAE):** Measures average error magnitude.
   - **Result**: `MAE = 0.1750`

2. **Root Mean Square Error (RMSE):** Penalizes larger errors more than MAE.
   - **Result**: `RMSE = 0.1803`

---

## Future Enhancements

- Implement additional recommendation algorithms (e.g., collaborative filtering).
- Introduce real-time data updates.
- Add more comprehensive tests for edge cases.
- Optimize API response times.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to contribute to this repository by opening issues or submitting pull requests!
