import streamlit as st

def Homelessness_Overview():
    st.title("Homelessness Overview")
    st.write("""
    ## Overview of Homelessness Data

    This page provides a general overview of the **Homelessness in the United States** data, 
    focusing on two important years: **2016** and **2023**.

    The data explores the number of available **beds** for homeless individuals across different 
    **housing types** such as:
    - **Emergency Shelters (ES)**: Temporary housing provided to homeless individuals and families.
    - **Transitional Housing (TH)**: Housing designed to assist individuals or families in transitioning 
      from homelessness to permanent housing.
    - **Safe Havens (SH)**: Specialized shelters for individuals with more complex needs, such as those 
      with mental health issues.

    This app allows you to:
    - Explore total bed availability across **Emergency Shelters (ES)**, **Transitional Housing (TH)**, and 
      **Safe Havens (SH)** for the years **2016** and **2023**.
    - Compare changes in the availability of beds over time through **data visualizations** like scatter plots, 
      histograms, and line charts.
    - Understand how **CoC Number** (Continuum of Care) regions are impacted by changes in the number of available beds.

    The purpose of this page is to give you context for the visualizations and deeper insights available in the 
    following pages. Use this overview to get a clearer picture of how homelessness data is structured and what 
    trends are worth examining.
    """)
