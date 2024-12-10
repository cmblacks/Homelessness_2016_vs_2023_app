import streamlit as st
from Home import Home
from Data import main as Data
from Visualizations import main as Visualizations
from Homelessness_Overview import Homelessness_Overview

# Sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Homelessness Overview", "Data", "Visualizations"])

# Load the appropriate page based on selection
if selection == "Home":
    Home()
elif selection == "Homelessness Overview":
    Homelessness_Overview()
elif selection == "Data":
    Data()
elif selection == "Visualizations":
    Visualizations()