from flask import Flask, request, jsonify
import numpy as np
from sklearn.preprocessing import StandardScaler
import tensorflow as tf 
from tensorflow.python.keras.models import load_model
import joblib
import os

scaler = StandardScaler()

app = Flask(__name__)

tf_model = load_model('./saved_models')

@app.route('/')
def home():
    return "Welcome to the Diabetes Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    
    # Extract features from the JSON data
    bmi = data['bmi']
    hba1c = data['hba1c']
    blood_glucose = data['blood_glucose']
    
    # Create a feature array
    features = np.array([[bmi, hba1c, blood_glucose]])
    features_scaled = scaler.transform(features)
    output = tf_model.predict(features_scaled)
    output = tf.math.sigmoid(output)
    output = np.where(output >= 0.5, 1, 0) 
    final = ','.join(str(item) for innerlist in output for item in innerlist)
    
    return jsonify({
        'prediction': final
    })

if __name__ == '__main__':
    app.run(debug=True)
