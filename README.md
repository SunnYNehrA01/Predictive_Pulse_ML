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
<hr>
<br>
<p align="center">
<!-- 🔷 Header Banner -->
<p align="center">
  <div style="border: 2px solid #ddd; padding: 8px; display: inline-block;">
    <img src="https://github.com/user-attachments/assets/7eb43d4d-8b73-4b86-a5d8-d2f119f2ffa2" width="1000" alt="Header Banner"/>
  </div>
</p>

<br>

<!-- 🧠 Dashboard View -->
<h3>🧠 Dashboard View</h3>

<p align="center">
  <div style="border: 2px solid #ddd; padding: 8px; display: inline-block;">
    <img src="https://github.com/user-attachments/assets/f24dfa5c-f666-4692-bbaf-2fd09cbb65e2" width="850" alt="Dashboard View"/>
  </div>
</p>

<br>

<!-- 📈 Pulse Prediction Result -->
<h3>📈 Pulse Prediction Result</h3>

<p align="center">
  <div style="border: 2px solid #ddd; padding: 8px; display: inline-block;">
    <img src="https://github.com/user-attachments/assets/ac657222-1124-4f36-8793-368ed03768b8" width="850" alt="Prediction Result"/>
  </div>
</p>

<br>

<!-- 💻 Home Screen & Login -->
<h3>🖼️ Screens: Pulse Prediction Tool</h3>

<table align="center">
  <tr>
    <td align="center">
      <div style="border: 2px solid #ddd; padding: 8px;">
        <img src="https://github.com/user-attachments/assets/f907c12e-4031-4f99-a62f-2260a0c3d6c9" width="400" alt="Home Screen"/>
      </div><br>
    </td>
    <td align="center">
      <div style="border: 2px solid #ddd; padding: 8px;">
        <img src="https://github.com/user-attachments/assets/d42f994b-dd62-425b-999f-14a755a79401" width="400" alt="Login Screen"/>
      </div><br>
    </td>
  </tr>
</table>

<br>

<!-- ⚙️ Model Prediction Output -->
<h3>⚙️ Model Prediction Output PDF</h3>

<p align="center">
  <div style="border: 2px solid #ddd; padding: 8px; display: inline-block;">
    <img src="https://github.com/user-attachments/assets/9f866887-7a08-4be6-86bd-a4a9cef4530a" width="600" alt="Terminal Output"/>
  </div>
</p>

<br>

<!-- 📘 Architecture Flow -->
<h3>📘 Prediction Result Report</h3>

<p align="center">
  <div style="border: 2px solid #ddd; padding: 8px; display: inline-block;">
    <img src="https://github.com/user-attachments/assets/55e53fdd-ae93-43b7-ba64-2192c63f5c0f" width="950" alt="Architecture or Summary"/>
  </div>
</p>

















