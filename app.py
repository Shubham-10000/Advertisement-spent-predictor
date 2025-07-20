import streamlit as st
import joblib
import numpy as np  


model1 = joblib.load('model1.pkl')


st.title("Seles Prediction Application")

st.write("Please enter the values below")

TV = st.number_input("TV Investment", min_value=0, max_value=1000,step = 10)

Radio = st.number_input("Radio Investment", min_value=0, max_value=1000,step = 10)\
    
Newspaper = st.number_input("Newspaper Investment", min_value=0, max_value=1000,step = 10)

if st.button("Predict Sales"):
    input_data = np.array([[TV, Radio, Newspaper]])
    prediction = model1.predict(input_data)
    st.success(f"Predicted Sales: {prediction[0]:.2f} units")
else:
    st.warning("Please click the 'Predict Sales' button to make a prediction.")