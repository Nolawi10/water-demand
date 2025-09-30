import streamlit as st
import pandas as pd
import pickle
import os

# Set up the page
st.set_page_config(layout="wide")

# Define paths (MODIFY THESE TO MATCH YOUR ACTUAL PATHS)
MODEL_PATH = r"C:\Users\itzno\Desktop\water-demand-api\water_demand_model.pkl"
DATA_PATH = r"C:\Users\itzno\Desktop\water-demand-api\synthetic_water_data.csv"

# Load the trained model with error handling
@st.cache_resource
def load_model():
    try:
        if os.path.exists(MODEL_PATH):
            with open(MODEL_PATH, 'rb') as f:
                return pickle.load(f)
        else:
            st.error(f"Model file not found at: {MODEL_PATH}")
            return None
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

model = load_model()

# Function to load feature data with error handling
def load_feature_data():
    try:
        if os.path.exists(DATA_PATH):
            return pd.read_csv(DATA_PATH)
        else:
            st.error(f"Data file not found at: {DATA_PATH}")
            return None
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

# Load the data
df = load_feature_data()

# Only show the UI if we have the model and data
if model is not None and df is not None:
    # Sidebar controls
    st.sidebar.header("Water Demand Prediction Parameters")
    
    population = st.sidebar.slider("Population", 0, 1000000, 500000)
    temperature = st.sidebar.slider("Temperature (°C)", 0, 100, 20)
    precipitation = st.sidebar.slider("Precipitation (mm)", 0, 100, 50)
    evaporation = st.sidebar.slider("Evaporation (mm)", 0, 100, 50)

    if st.sidebar.button("Predict Water Demand"):
        try:
            input_features = [[population, temperature, precipitation, evaporation]]
            prediction = model.predict(input_features)
            st.success(f"Predicted Water Demand: {prediction[0]:.2f} units")
            
            # Show feature importance if data is available
            if 'water_demand' in df.columns:
                st.subheader("Feature Importance")
                st.bar_chart(df.corr()['water_demand'].drop('water_demand'))
        except Exception as e:
            st.error(f"Prediction failed: {str(e)}")