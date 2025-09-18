import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(page_title="PCOSNet Demo", page_icon="🩺", layout="centered")

st.title("PCOSNet Demo 🩺")
st.write("AI-based fusion model (ultrasound + tabular) for PCOS diagnostics.")

# Tabular inputs
st.subheader("Enter Patient Data")
age = st.number_input("Age (years)", min_value=15, max_value=45, value=25)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.5)
insulin = st.number_input("Insulin Level (µIU/mL)", min_value=1.0, max_value=300.0, value=80.0)

# Ultrasound upload
st.subheader("Upload Ultrasound Image")
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Ultrasound", use_column_width=True)

# Fake prediction logic (replace later with trained model)
if st.button("Predict"):
    features = np.array([age, bmi, insulin])
    # Simulated model: random choice
    pred = np.random.choice(["PCOS Likely", "PCOS Unlikely"])
    st.success(f"Prediction: {pred}")
