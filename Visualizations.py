import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache
def load_data():
    data_2016 = pd.read_csv('2016-HIC-Counts-by-CoC.csv', header=1)
    data_2023 = pd.read_csv('2023-HIC-Counts-by-CoC.csv', header=1)
    return data_2016, data_2023

def plot_histogram(data_2016, data_2023):
    bed_columns = [
        'Total Beds for Households with only Children (ES)', 
        'Total Beds for Households with only Children (TH)', 
        'Total Beds for Households with only Children (SH)'
    ]
    
    bed_data_2016 = data_2016[bed_columns].apply(pd.to_numeric, errors='coerce').sum()
    bed_data_2023 = data_2023[bed_columns].apply(pd.to_numeric, errors='coerce').sum()

    plt.figure(figsize=(10, 6))

    sns.histplot(bed_data_2016, kde=True, color='blue', label='2016', bins=15)
    sns.histplot(bed_data_2023, kde=True, color='orange', label='2023', bins=15)
    
    plt.title('Distribution of Total Beds for Households with Only Children (2016 vs 2023)')
    plt.xlabel('Total Beds')
    plt.ylabel('Frequency')
    plt.legend(title="Year")
    st.pyplot(plt)

    st.write("""
    ### Histogram of Total Beds for Households with Only Children
    This histogram displays the **distribution** of available beds for households with only children, 
    across **Emergency Shelters (ES)**, **Transitional Housing (TH)**, and **Safe Havens (SH)** for 
    the years **2016** and **2023**. The plot compares the frequency of different bed ranges, helping 
    to understand how available beds for households with only children have changed between the two years.
    """)

def plot_line_chart(data_2016, data_2023):
    bed_columns = [
        'Total Year-Round Beds (ES)', 
        'Total Year-Round Beds (TH)', 
        'Total Year-Round Beds (SH)'
    ]
    
    bed_data_2016 = data_2016[bed_columns].apply(pd.to_numeric, errors='coerce').groupby(data_2016['CoC Number']).sum()
    bed_data_2023 = data_2023[bed_columns].apply(pd.to_numeric, errors='coerce').groupby(data_2023['CoC Number']).sum()

    bed_data_2016 = bed_data_2016.reset_index().melt(id_vars='CoC Number', var_name='Housing Type', value_name='Total Beds')
    bed_data_2023 = bed_data_2023.reset_index().melt(id_vars='CoC Number', var_name='Housing Type', value_name='Total Beds')

    bed_data_2016['Year'] = 2016
    bed_data_2023['Year'] = 2023

    combined_data = pd.concat([bed_data_2016, bed_data_2023])

    plt.figure(figsize=(15, 7))
    sns.lineplot(data=combined_data, x='Housing Type', y='Total Beds', hue='Year', style='Year', markers='o', palette='viridis')
    
    plt.title('Comparison of Bed Counts per Housing Type (2016 vs 2023) by CoC Number')
    plt.xlabel('Housing Type')
    plt.ylabel('Total Beds')
    plt.legend(title="Year")
    plt.xticks(rotation=45)
    st.pyplot(plt)

    st.write("""
    ### Line Chart: Bed Counts per Housing Type (2016 vs 2023)
    This line chart compares the **total bed counts** for different housing types 
    (**Emergency Shelters (ES)**, **Transitional Housing (TH)**, **Safe Havens (SH)**) between 
    **2016** and **2023**. The chart shows trends in bed availability for each housing type, 
    making it easier to compare how the number of available beds for each housing type has changed 
    over time, and whether some housing types have seen growth or decline.
    """)

def plot_scatterplot(data_2016, data_2023):
    bed_columns = [
        'Total Year-Round Beds (ES)', 
        'Total Year-Round Beds (TH)', 
        'Total Year-Round Beds (SH)'
    ]
    
    combined_data_2016 = data_2016[bed_columns].apply(pd.to_numeric, errors='coerce')
    combined_data_2023 = data_2023[bed_columns].apply(pd.to_numeric, errors='coerce')

    plt.figure(figsize=(10, 6))

    sns.scatterplot(data=combined_data_2016, x='Total Year-Round Beds (ES)', y='Total Year-Round Beds (TH)', color='blue', label='2016', s=100)
    sns.scatterplot(data=combined_data_2016, x='Total Year-Round Beds (ES)', y='Total Year-Round Beds (SH)', color='blue', marker='x', s=100)

    sns.scatterplot(data=combined_data_2023, x='Total Year-Round Beds (ES)', y='Total Year-Round Beds (TH)', color='orange', label='2023', s=100)
    sns.scatterplot(data=combined_data_2023, x='Total Year-Round Beds (ES)', y='Total Year-Round Beds (SH)', color='orange', marker='x', s=100)

    plt.title('Scatter Plot of Total Beds in Housing Types (ES, TH, SH) for 2016 vs 2023')
    plt.xlabel('Emergency Shelters (ES) Beds')
    plt.ylabel('Transitional Housing (TH) and Safe Havens (SH) Beds')
    plt.legend(title="Year")
    st.pyplot(plt)

    st.write("""
    ### Scatter Plot of Total Beds in Housing Types (ES, TH, SH)
    This scatter plot compares the **total beds** in **Emergency Shelters (ES)** to **Transitional Housing (TH)** 
    and **Safe Havens (SH)** for both **2016** and **2023**. Each point represents the bed count for a 
    specific housing type. The plot allows you to visually compare how different housing types (ES, TH, SH) 
    are related and whether the availability of beds in one type has a correlation with the availability 
    in another, across both years.
    """)

def main():
    st.title("Visualizations for Homelessness Analysis")

    data_2016, data_2023 = load_data()

    # Plot the histogram of total beds for households with only children by housing type
    plot_histogram(data_2016, data_2023)

    # Plot the line chart of data by CoC Number
    plot_line_chart(data_2016, data_2023)

    # Plot the scatter plot of total beds by housing type and year
    plot_scatterplot(data_2016, data_2023)

if __name__ == "__main__":
    main()
