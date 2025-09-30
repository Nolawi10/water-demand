from flask import Flask, request, jsonify
import joblib
import numpy as np

import os
import joblib

model_path = os.path.join(os.path.dirname(__file__), "water_demand_model.pkl")
print("Loading model from:", model_path)  # Debugging print
model = joblib.load(model_path)


app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array([data["Temperature_C"], data["Humidity_%"], data["Rainfall_mm"],
                             data["Soil_Moisture_%"], data["Water_Level_m"]]).reshape(1, -1)
        prediction = model.predict(features)[0]
        return jsonify({"Water_Demand_L/ha": prediction})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
