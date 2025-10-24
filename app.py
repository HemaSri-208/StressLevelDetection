# Streamlit app code for Stress Detection Prediction
# Save this as a separate file, e.g., app.py
# Run with: streamlit run app.py
# Ensure 'trained_model.sav' is in the same directory or provide the correct path.

import streamlit as st
import pickle
import numpy as np
# ...existing code...
import streamlit as st
import pickle
import numpy as np
from pathlib import Path

# Resolve model path relative to this script, fallback to CWD
model_path = Path(__file__).resolve().parent / "trained_model.sav"
if not model_path.exists():
    model_path = Path.cwd() / "trained_model.sav"

if not model_path.exists():
    st.error(f"Model file not found. Expected at: {model_path}")
    st.stop()

# Load the saved model
with model_path.open("rb") as f:
    model = pickle.load(f)
# ...existing code...
# Load the saved model
filename = 'trained_model.sav'
model = pickle.load(open(filename, 'rb'))

# Define the labels
labels = {
    0: "Amused",
    1: "Neutral",
    2: "Stressed"
}

# Streamlit app title
st.title("Stress Detection Prediction")

# Input fields for the features
st.header("Input Physiological and Demographic Data")

bvp_mean = st.number_input("BVP_mean", value=0.0)
bvp_std = st.number_input("BVP_std", value=0.0)
eda_phasic_mean = st.number_input("EDA_phasic_mean", value=0.0)
eda_phasic_min = st.number_input("EDA_phasic_min", value=0.0)
eda_smna_min = st.number_input("EDA_smna_min", value=0.0)
eda_tonic_mean = st.number_input("EDA_tonic_mean", value=0.0)
resp_mean = st.number_input("Resp_mean", value=0.0)
resp_std = st.number_input("Resp_std", value=0.0)
temp_mean = st.number_input("TEMP_mean", value=0.0)
temp_std = st.number_input("TEMP_std", value=0.0)
temp_slope = st.number_input("TEMP_slope", value=0.0)
bvp_peak_freq = st.number_input("BVP_peak_freq", value=0.0)
age = st.number_input("age", min_value=0, max_value=120, value=30)
height = st.number_input("height (cm)", min_value=0, max_value=250, value=170)
weight = st.number_input("weight (kg)", min_value=0, max_value=200, value=70)

# Collect inputs into an array
input_data = np.array([
    bvp_mean, bvp_std, eda_phasic_mean, eda_phasic_min, eda_smna_min,
    eda_tonic_mean, resp_mean, resp_std, temp_mean, temp_std, temp_slope,
    bvp_peak_freq, age, height, weight
])

# Prediction button
if st.button("Predict"):
    # Predict
    prediction = model.predict(input_data.reshape(1, -1))[0]
    predicted_label = labels.get(prediction, "Unknown")
    
    st.success(f"Predicted State: {predicted_label}")