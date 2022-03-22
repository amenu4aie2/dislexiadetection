import streamlit as st
from predict_page import main
st.sidebar.selectbox("Explore or Predict",("Explore","Predict"))

main()