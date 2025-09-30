import streamlit as st
import pandas as pd
import pickle
import os
import numpy as np
import warnings
from sklearn.exceptions import InconsistentVersionWarning

# ========== CONFIGURATION ==========
warnings.filterwarnings("ignore", message="missing ScriptRunContext")
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

st.set_page_config(
    page_title="Water Demand Predictor",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== CUSTOM CSS ==========
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
            padding: 2rem;
        }
        .sidebar .sidebar-content {
            background-color: #ffffff;
            box-shadow: 2px 0 10px rgba(0,0,0,0.1);
            padding: 1.5rem;
        }
        h1 {
            color: #1f77b4;
            border-bottom: 2px solid #1f77b4;
            padding-bottom: 0.5rem;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            border-radius: 8px;
            padding: 10px 24px;
            font-weight: bold;
            transition: all 0.3s;
        }
        .stButton>button:hover {
            background-color: #1668a8;
            transform: scale(1.02);
        }
        .prediction-card {
            background-color: white;
            border-radius: 10px;
            padding: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin: 1rem 0;
        }
        .metric-value {
            font-size: 2.5rem !important;
            color: #1f77b4 !important;
        }
    </style>
""", unsafe_allow_html=True)

# ========== HEADER SECTION ==========
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/305/305098.png", width=100)
with col2:
    st.title("Smart Water Demand Prediction System")
    st.markdown("""
    <div style='color:#666; margin-bottom:1.5rem;'>
        Predict future water requirements based on environmental and demographic factors
    </div>
    """, unsafe_allow_html=True)

# ========== MODEL LOADING ==========
@st.cache_resource
def load_model():
    MODEL_PATH = r"C:\Users\itzno\Desktop\water-demand-api\water_demand_model.pkl"
    try:
        if os.path.exists(MODEL_PATH):
            with open(MODEL_PATH, 'rb') as f:
                model = pickle.load(f)
                return model if hasattr(model, 'predict') else None
        st.error(f"Model file not found at: {MODEL_PATH}")
        return None
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def load_feature_data():
    DATA_PATH = r"C:\Users\itzno\Desktop\water-demand-api\synthetic_water_data.csv"
    try:
        if os.path.exists(DATA_PATH):
            df = pd.read_csv(DATA_PATH)
            return df if not df.empty else None
        st.error(f"Data file not found at: {DATA_PATH}")
        return None
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

model = load_model()
df = load_feature_data()

# ========== MAIN APP LOGIC ==========
model_loaded = model is not None and hasattr(model, 'predict')
data_loaded = df is not None and not df.empty

if model_loaded and data_loaded:
    # ========== SIDEBAR CONTROLS ==========
    with st.sidebar:
        st.header("⚙️ Prediction Parameters")
        
        with st.expander("Demographic Factors", expanded=True):
            population = st.slider(
                "Population", 
                0, 1000000, 500000,
                help="Total population in the area"
            )
        
        with st.expander("Environmental Factors", expanded=True):
            temperature = st.slider(
                "Temperature (°C)", 
                -20, 50, 20,
                help="Average daily temperature"
            )
            precipitation = st.slider(
                "Precipitation (mm)", 
                0, 500, 50,
                help="Monthly precipitation level"
            )
            evaporation = st.slider(
                "Evaporation (mm)", 
                0, 200, 50,
                help="Daily evaporation rate"
            )
        
        predict_button = st.button(
            "🚀 Predict Water Demand", 
            use_container_width=True,
            type="primary"
        )

    # ========== PREDICTION RESULTS ==========
    if predict_button:
        try:
            # Make prediction
            input_data = [[population, temperature, precipitation, evaporation]]
            prediction = model.predict(input_data)
            
            # Handle array output
            if isinstance(prediction, np.ndarray):
                prediction = prediction[0]
            
            # Display results in card
            with st.container():
                st.markdown("""<div class='prediction-card'>""", unsafe_allow_html=True)
                
                col_a, col_b = st.columns([1, 2])
                with col_a:
                    st.markdown("### 📊 Prediction Results")
                    st.metric(
                        label="Water Demand", 
                        value=f"{prediction:,.0f} units",
                        delta="Normal" if 50000 <= prediction <= 150000 else "High"
                    )
                    
                    # Visual indicator
                    demand_percent = min(100, int(prediction/5000))
                    st.progress(
                        demand_percent, 
                        text=f"Capacity: {demand_percent}%"
                    )
                
                with col_b:
                    if 'water_demand' in df.columns:
                        st.markdown("### 📈 Feature Importance")
                        importance = df.corr()['water_demand'].drop('water_demand')
                        st.bar_chart(importance)
                
                st.markdown("""</div>""", unsafe_allow_html=True)
                
                # Additional insights
                with st.expander("💡 Water Management Recommendations", expanded=True):
                    tab1, tab2, tab3 = st.tabs(["Conservation", "Infrastructure", "Monitoring"])
                    
                    with tab1:
                        st.markdown("""
                        - **Fix leaks** promptly (saves up to 20 gallons/day)
                        - Install **low-flow fixtures**
                        - Implement **rainwater harvesting**
                        - Promote **water-efficient landscaping**
                        """)
                    
                    with tab2:
                        st.markdown("""
                        - Upgrade **distribution systems**
                        - Implement **smart metering**
                        - Build **storage reservoirs**
                        - Develop **water recycling systems**
                        """)
                    
                    with tab3:
                        st.markdown("""
                        - Install **IoT sensors** for real-time monitoring
                        - Implement **predictive maintenance**
                        - Regular **water quality testing**
                        - **Demand forecasting** analytics
                        """)

            # Data exploration section
            with st.expander("🔍 Explore Historical Data", expanded=False):
                st.dataframe(df.head(10)), 
                st.line_chart(df[['temperature', 'precipitation', 'evaporation']].head(50))

        except Exception as e:
            st.error(f"⚠️ Prediction failed: {str(e)}")

else:
    st.warning("Please ensure both model and data files are available to use the predictor")
    st.image("https://cdn-icons-png.flaticon.com/512/3767/3767084.png", width=200)