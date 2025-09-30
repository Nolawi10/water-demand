from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics import r2_score

app = Flask(__name__)

# Load the model and data
MODEL_PATH = 'water_demand_model.pkl'
DATA_PATH = 'synthetic_water_data.csv'

try:
    # Try loading the model
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    
    # Verify it's a valid scikit-learn model
    if not hasattr(model, 'predict'):
        raise ValueError('Loaded object is not a valid scikit-learn model')
    
    # Load the data
    df = pd.read_csv(DATA_PATH)
    
    # Calculate model accuracy
    X = df.drop('Water_Demand_L/ha', axis=1)
    y = df['Water_Demand_L/ha']
    predictions = model.predict(X)
    accuracy = r2_score(y, predictions) * 100
    
    print(f"Model loaded successfully. Accuracy: {accuracy:.2f}%")
except Exception as e:
    print(f"Error loading model: {str(e)}")
    # Create a simple linear regression model as a fallback
    from sklearn.linear_model import LinearRegression
    df = pd.read_csv(DATA_PATH)
    X = df.drop('Water_Demand_L/ha', axis=1)
    y = df['Water_Demand_L/ha']
    model = LinearRegression()
    model.fit(X, y)
    predictions = model.predict(X)
    accuracy = r2_score(y, predictions) * 100
    print(f"Created fallback model. Accuracy: {accuracy:.2f}%")

@app.route('/')
def home():
    return render_template('index.html', accuracy=accuracy)

@app.route('/predict', methods=['POST'])
def predict():

    try:
        data = request.get_json()
        
        # Prepare input data
        input_data = [
            data['temperature'],
            data['humidity'],
            data['rainfall'],
            data['soilMoisture']
        ]

        # Make prediction
        prediction = model.predict([input_data])[0]
        
        return jsonify({
            'prediction': float(prediction),
            'status': 'success'
        })
    except Exception as e:
        print(f"Prediction error: {str(e)}")
        return jsonify({
            'error': 'Failed to make prediction',
            'status': 'error'
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
