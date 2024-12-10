import streamlit as st
import pandas as pd

@st.cache
def load_data():
    data_2016 = pd.read_csv('2016-HIC-Counts-by-CoC.csv', header=1)
    data_2023 = pd.read_csv('2023-HIC-Counts-by-CoC.csv', header=1)
    return data_2016, data_2023

def main():
    st.title("Homelessness Data for 2016 and 2023")

    st.write("""
    ## Data Overview

    This page provides **raw data** for **2016** and **2023** for the **Homelessness in the US** analysis. 
    The dataset includes the number of beds available across different types of housing for homeless individuals 
    in **Emergency Shelters (ES)**, **Transitional Housing (TH)**, and **Safe Havens (SH)**.

    The dataset is grouped by **CoC Number** (Continuum of Care), which represents regions in the US and their 
    services for homeless populations.

    ### What You Can Explore:
    - **Total Year-Round Beds**: The total number of beds available in **Emergency Shelters (ES)**, 
      **Transitional Housing (TH)**, and **Safe Havens (SH)** for each year (2016 and 2023).
    - **Comparison Between Years**: Understand how the bed availability changed from **2016** to **2023**.
    - **Insights by CoC Number**: Explore bed availability data across different **CoC Numbers** (regions).

    This page is crucial for those who want to dive deep into the underlying data to gain insights into 
    homelessness trends in the US over time. Use the data tables to see specific values for different regions 
    and compare how things have changed.
    """)

    # Load the data
    data_2016, data_2023 = load_data()

    # Bed columns we are interested in
    bed_columns = [
        'Total Year-Round Beds (ES)', 
        'Total Year-Round Beds (TH)', 
        'Total Year-Round Beds (SH)'
    ]

    st.subheader("Total Beds by Housing Type in 2016")
    st.write(data_2016[bed_columns].sum())

    st.subheader("Total Beds by Housing Type in 2023")
    st.write(data_2023[bed_columns].sum())
