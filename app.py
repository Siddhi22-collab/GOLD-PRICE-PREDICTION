import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('gold_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app title
st.title("Gold Price Prediction (GLD)")

# Input fields for the four features
st.header("Enter Financial Indicators:")

SPX = st.number_input("S&P 500 Index (spx)")
USO = st.number_input("United States Oil Fund (uso)")
SLV = st.number_input("Silver Price (slv)")
EUR_USD = st.number_input("EUR/USD Exchange Rate (eur/usd)")

# Predict when the button is clicked
if st.button("Predict Gold Price"):
    input_data = np.array([[SPX,USO,SLV,EUR_USD]])  # Keep as 2D array
    prediction = model.predict(input_data)
    st.success(f"Predicted Gold Price (GLD): ${prediction[0]:.2f}")
