# Placement Predictor

A Flask-based placement prediction web application that estimates whether a student is likely to get placed based on CGPA, skill score, projects, and internships.

## Features

- Student placement prediction form
- Resume skill detection from PDF upload
- Result page with probability and graph
- Simple UI with CSS styling

## Tech Stack

- Python
- Flask
- scikit-learn
- pandas
- matplotlib
- pdfplumber

## Run locally

1. Create a virtual environment and activate it.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the app:
   ```bash
   python app.py
   ```
4. Open the browser at:
   ```text
   http://127.0.0.1:5000
   ```

## Project files

- `app.py` – Flask app with routes
- `model.py` – model training script
- `students.csv` – training data
- `model.pkl` – saved trained model
- `templates/` – HTML pages
- `static/` – CSS assets
- `uploads/` – uploaded PDF resumes

## Notes

The resume analysis checks common skills like Python, Java, SQL, HTML, CSS, and machine learning keywords.
