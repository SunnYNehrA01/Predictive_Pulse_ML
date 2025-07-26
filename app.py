from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flashing messages

# Create models directory
os.makedirs('models', exist_ok=True)

# Load the model and label encoder
try:
    model_path = 'models/bp_model.joblib'
    encoder_path = 'models/label_encoder.joblib'
    
    if not os.path.exists(model_path) or not os.path.exists(encoder_path):
        raise FileNotFoundError("Model files not found. Please train the model first.")
    
    model = joblib.load(model_path)
    label_encoder = joblib.load(encoder_path)
    print("Model and encoder loaded successfully!")
except Exception as e:
    print(f"Error loading models: {e}")
    model = None
    label_encoder = None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict-page')
def predict_page():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or label_encoder is None:
        return render_template('index.html', 
                             error="Model not loaded. Please ensure the model is trained and saved.")
    
    try:
        # ✅ Use the same 11 features used during training
        input_data = [
            int(request.form.get('C')),
            int(request.form.get('Age')),
            int(request.form.get('History')),
            int(request.form.get('Patient')),
            int(request.form.get('TakeMedication')),
            int(request.form.get('Severity')),
            int(request.form.get('BreathShortness')),
            int(request.form.get('VisualChanges')),
            int(request.form.get('NoseBleeding')),
            int(request.form.get('Whendiagnoused')),
            int(request.form.get('Systolic_Num')),
            int(request.form.get('Diastolic_Num')),
            int(request.form.get('ControlledDiet'))
        ]
        name = request.form.get('Name')  # Captures name from HTML form


        prediction = model.predict([input_data])[0]
        decoded_prediction = label_encoder.inverse_transform([prediction])[0]
        # Advice based on prediction
        advice_map = {
            "NORMAL": "Your blood pressure is normal. Maintain a healthy lifestyle!",
            "HYPERTENSION (Stage-1)": "Monitor your BP regularly and reduce salt intake.",
            "HYPERTENSION (Stage-2)": "Consult a doctor and follow medication strictly.",
            "HYPERTENSIVE CRISIS": "Immediate medical attention is required!"
        }
        advice = advice_map.get(decoded_prediction, "Please consult a healthcare provider.")
        return render_template(
            'index.html',
            prediction_text=f"Predicted Hypertension Stage: {decoded_prediction}",
            advice=advice,
            systolic=input_data[-3],  # Systolic_Num
            diastolic=input_data[-2],  # Diastolic_Num
            name=name 
        )
    except Exception as e:
        return render_template('index.html', error=f"Prediction error: {str(e)}")
if __name__ == '__main__':
    app.run(debug=True)
