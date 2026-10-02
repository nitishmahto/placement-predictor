from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import base64
import io
import os
import pickle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pdfplumber


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {".pdf"}
KNOWN_SKILLS = [
    "python",
    "java",
    "machine learning",
    "data analysis",
    "sql",
    "html",
    "css",
]

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)


def extract_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            text += page_text + "\n"
    return text


def detect_skills(text):
    found_skills = []
    lowered_text = text.lower()

    for skill in KNOWN_SKILLS:
        if skill in lowered_text:
            found_skills.append(skill)

    return found_skills


def create_graph():
    data = pd.read_csv("students.csv")

    plt.figure(figsize=(5, 3))
    plt.scatter(data["cgpa"], data["placed"])
    plt.xlabel("CGPA")
    plt.ylabel("Placement")

    img = io.BytesIO()
    plt.savefig(img, format="png", bbox_inches="tight")
    img.seek(0)

    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return graph_url


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return {"status": "ok", "app": "placement-predictor"}


@app.route("/predict", methods=["POST"])
def predict():
    cgpa = float(request.form.get("cgpa", 0))
    skills = float(request.form.get("skills", 0))
    projects = float(request.form.get("projects", 0))
    internships = float(request.form.get("internships", 0))

    data = np.array([[cgpa, skills, projects, internships]])

    prediction = model.predict(data)
    probability = model.predict_proba(data)[0][1] * 100
    graph = create_graph()

    if prediction[0] == 1:
        result = "Student will get placement"
    else:
        result = "Student may not get placement"

    return render_template(
        "result.html",
        prediction_text=result,
        probability=round(probability, 2),
        graph=graph,
    )


@app.route("/analyze_resume", methods=["POST"])
def analyze_resume():
    if "resume" not in request.files:
        return "No file uploaded"

    file = request.files["resume"]

    if file.filename == "":
        return "No file uploaded"

    filename = secure_filename(file.filename)
    _, extension = os.path.splitext(filename)
    if extension.lower() not in ALLOWED_EXTENSIONS:
        return "Please upload a PDF resume"

    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    text = extract_text(file_path)
    found_skills = detect_skills(text)
    missing_skills = [skill for skill in KNOWN_SKILLS if skill not in found_skills]

    return render_template(
        "result.html",
        skills=found_skills,
        missing=missing_skills,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
