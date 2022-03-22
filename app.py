import imp
from operator import mod
import streamlit as st
from predict_page import main
from explore_page import modeltrain
st.sidebar.selectbox("Explore or Predict",("Explore","Predict"))
modeltrain()
main()
