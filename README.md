# 🩺 Predictive Pulse: Harnessing Machine Learning for Blood Pressure Analysis

> A Flask-based web application that predicts a person's blood pressure stage (e.g., Normal, Hypertension Stage 1/2, Crisis) based on basic health inputs, using a trained ML model. The app also allows users to download the results as a PDF report.

---

## 🔍 Project Overview

Predictive Pulse is a machine learning project that helps estimate a user's blood pressure category from clinical features like age group, gender, systolic & diastolic BP, and other symptoms.

Key Features:
- Interactive web UI using Flask + HTML/CSS (Bootstrap)
- Trained SVM-based ML model for BP classification
- Client-side PDF generation using jsPDF
- Clean and responsive design
- Lightweight and easy to deploy

---

## 🧠 How It Works

1. **User visits the homepage** and enters basic medical inputs through a form.
2. **Model predicts** the blood pressure stage (e.g., Normal, Crisis).
3. **Advice is shown** based on the prediction.
4. **Download button** allows saving the result as a PDF report.

---

## 🚀 Tech Stack

- **Frontend**: HTML, CSS (Bootstrap), JavaScript (jsPDF)
- **Backend**: Python, Flask
- **ML Model**: Scikit-learn (SVM pipeline)
- **Data Processing**: Pandas, NumPy
- **PDF Generator**: jsPDF (client-side)

---

## 📁 Project Structure
predictive_pulse/
│
├── app.py # Main Flask application
├── /templates/ # HTML files
│ ├── home.html
│ └── index.html
├── /static/ # Static assets like images & CSS
│ ├── bg.jpg
│ └── style.css # Optional: custom styles
├── /models/ # Trained model files
│ ├── bp_model.joblib
│ └── label_encoder.joblib
├── requirements.txt # Python dependencies
└── README.md # Project overview


---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/predictive-pulse.git
   cd predictive-pulse


2. **(Optional but Recommended) Create a virtual environment**
    python -m venv venv
    source venv/bin/activate        # On Windows: venv\Scripts\activate


3. **Install dependencies**
    pip install -r requirements.txt

4. **Run the app**
    python app.py

5. **Open the app in your browser**
    Navigate to: http://127.0.0.1:5000


