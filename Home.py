import streamlit as st

def Home():
    st.title("Homelessness in the US by Housing Type (2016 vs 2023)")

    st.write("""
    ## Welcome to the Homelessness Analysis App

    This app aims to provide insights into **homelessness data in the United States** by comparing the availability of beds 
    in various housing types for two important years: **2016** and **2023**.

    The goal of this analysis is to help visualize and understand how the availability of homeless shelter beds in 
    **Emergency Shelters (ES)**, **Transitional Housing (TH)**, and **Safe Havens (SH)** has changed over time and how 
    these changes may impact homeless individuals and families in different regions.

    ### Key Features of the App:
    - **Explore the Data**: View the total number of beds available across different housing types in **2016** and **2023**.
    - **Compare Trends**: Visualize how the availability of beds has changed between the two years with interactive plots.
    - **Detailed Visualizations**: Access charts such as **line charts**, **histograms**, and **scatter plots** to compare data by housing type and year.
    - **Understand Regional Impact**: The data is broken down by **CoC Number** (Continuum of Care), which represents specific regions across the country. This allows you to see how homelessness trends differ by location.

    ### Why This Matters:
    The availability of beds in shelters is an important metric for understanding how homelessness is addressed in different areas. By comparing **2016** and **2023**, we can see whether the resources for people experiencing homelessness have increased, decreased, or remained stable over time.

    ### How to Use the App:
    - Navigate to the **Data Page** to see the raw data for 2016 and 2023.
    - Check out the **Visualizations Page** for detailed charts that provide insights into how shelter bed availability has changed.
    - Visit the **Homelessness Overview** for a broad summary and context behind the data.

    This app is aimed at policymakers, researchers, and anyone interested in understanding the dynamics of homelessness in the U.S.
    """)

    st.write("""
    ## Purpose of the Project

    My project focuses on analyzing homelessness trends in the United States, with a particular emphasis on year-over-year changes in the availability of shelter beds and housing resources. The primary dataset includes variables such as the number of year-round shelter beds, types of housing (Emergency Shelters, Transitional Housing, Safe Haven, etc.), and bed availability over multiple years (e.g., 2016 and 2023). Using Tableau, my goal is to visualize the changes in bed capacity across different Contin...

    By breaking down the data by region or CoC, my analysis also explores geographic disparities in bed availability, offering a comprehensive view of how homelessness resources have evolved over time. My project aims to hopefully help inform decision-makers such as lawmakers, government agencies, and non-profits on the effectiveness of resource allocation and help guide future efforts in addressing homelessness in the U.S.
    """)

    st.write("""
    ## How the App Works

    This app allows you to interact with data and visualizations that demonstrate the availability and changes in shelter beds from **2016** to **2023**. You can explore detailed charts, compare bed availability by region, and gain valuable insights into the state of homelessness resources.

    Navigate through the **Data Page** to understand the raw data and see bed counts by housing type. Use the **Visualizations Page** to dive into interactive charts that provide a more in-depth look at the data.

    The **Homelessness Overview** page will give you context and background on the trends and key findings from the data.
    """)

