import streamlit as st
import pickle
import json
import numpy as np
import pandas as pd
import time
import plotly.express as px
import os

# Load model and column info
with open("bangalore_home_prices_model.pickle", "rb") as f:
    model = pickle.load(f)

with open("columns.json", "r") as f:
    data_columns = json.load(f)["data_columns"]
    locations = data_columns[3:]

# Page settings
st.set_page_config(page_title="Bangalore Price Predictor", layout="centered")

# Sidebar Info
st.sidebar.title("📊 Project Info")
st.sidebar.markdown("""
This app predicts **house prices in Bangalore** using:
- Linear Regression model
- One-hot encoded location
- Trained on housing dataset

👨‍💻 **By:** Shubham Kumar Jha  
📂 **Dataset:** Bengaluru_House_Data.csv
""")

# Main Title
st.markdown("""
# 🏠 Bangalore Home Price Predictor
Estimate the value of your dream home instantly!
---
""")

# Inputs
st.markdown("### 📝 Enter Home Details")

col1, col2 = st.columns(2)

with col1:
    sqft = st.number_input("📏 Total Area (sqft)", min_value=500, max_value=10000, step=50)

with col2:
    bhk = st.slider("🛏️ BHK (Bedrooms)", 1, 5, 2)

bath = st.slider("🛁 Number of Bathrooms", 1, 5, 2)
location = st.selectbox("📍 Location", sorted(locations))

# Prediction
if st.button("🔮 Predict Price"):
    with st.spinner("Predicting..."):
        try:
            loc_index = data_columns.index(location.lower())
        except:
            loc_index = -1

        x = np.zeros(len(data_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        if loc_index >= 0:
            x[loc_index] = 1

        prediction = model.predict([x])[0]
        time.sleep(1)  # for effect

    st.success("Prediction complete! 🎉")
    st.markdown(f"## 💰 Estimated Price: ₹ `{prediction:.2f} Lakhs`")

    # Download Button
    result_text = f"""Prediction Result:
Location: {location}
Area: {sqft} sqft
BHK: {bhk}
Bathrooms: {bath}

Predicted Price: ₹ {prediction:.2f} Lakhs
"""
    st.download_button("📥 Download Prediction", result_text, "prediction_result.txt", "text/plain")

    # Plotly Chart - Price vs Sqft
    st.markdown("### 📈 Price vs Area (Demo Visualization)")
    sqft_range = np.array([500, 1000, 1500, 2000, 2500, 3000])
    pred_prices = [
        model.predict([[s, bath, bhk] + [1 if loc == location.lower() else 0 for loc in data_columns[3:]]])[0]
        for s in sqft_range
    ]
    df_chart = pd.DataFrame({'Square Feet': sqft_range, 'Predicted Price (Lakhs)': pred_prices})
    fig = px.line(df_chart, x="Square Feet", y="Predicted Price (Lakhs)", markers=True, title="Price vs Area")
    st.plotly_chart(fig)

# Location-wise average bar chart
# ⬇️ BHK Distribution Chart Toggle
st.markdown("### 🏘️ BHK Distribution in the Dataset")

show_chart = st.checkbox("📊 Show BHK Distribution Chart")

if show_chart:
    data_path = "Bengaluru_House_Data.csv"

    if os.path.exists(data_path):
        df_data = pd.read_csv(data_path)

        # Extract BHK info from 'size' column
        if 'size' in df_data.columns:
            df_data['bhk'] = df_data['size'].str.extract('(\d+)').astype(float)

        bhk_counts = df_data['bhk'].value_counts().sort_index()

        fig = px.pie(
            names=[f"{int(bhk)} BHK" for bhk in bhk_counts.index],
            values=bhk_counts.values,
            title="Distribution of BHK Types in Dataset",
            hole=0.4
        )
        st.plotly_chart(fig)
    else:
        st.warning("⚠️ 'Client/Bengaluru_House_Data.csv' not found.")



# Custom CSS
st.markdown("""
<style>
    .main { background-color: #f9f9f9; }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .stButton>button {
        background-color: #2980b9;
        color: white;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #1abc9c;
        color: black;
    }
    .subtitle {
        font-size: 16px;
        color: gray;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)
