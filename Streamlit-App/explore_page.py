import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def show_explore_page():
    # Load the dataset
    dataset = pd.read_csv("../Resources/cleaned_dataset.csv")

    # Count the frequency of each state
    state_counts = dataset['State'].value_counts()

    # Create a pie chart using matplotlib with adjustments
    fig, ax = plt.subplots(figsize=(5, 5))

    # Adjust explode to separate smaller slices
    explode = tuple(0.1 if count < max(state_counts) * 0.01 else 0 for count in state_counts)

    # Set a minimum percentage to display labels
    min_percentage = 2.0
    wedges, texts, autotexts = ax.pie(state_counts, labels=state_counts.index, autopct=lambda p: f'{p:.1f}%' if p > min_percentage else '',
                                      startangle=90, textprops={'fontsize': 8, 'va': 'center'}, explode=explode)

    # Adjust the layout to avoid overlapping text
    plt.setp(autotexts, size=6)
    plt.setp(texts, size=6)

    # Configure the layout of the Streamlit app
    st.title('Distribution of vehicles by state')
    st.pyplot(fig)

    # Bar Chart
    # Configure the layout of the Streamlit app
    st.title('Mean Price Based On State')

    # Group by state and calculate the mean price
    data = dataset.groupby(["State"])["Price"].mean().sort_values(ascending=True)

    st.bar_chart(data)

    # Line chart
    # Configure the layout of the Streamlit app
    st.title('Mean Price Based On Year of Manufacture')
    data = dataset.groupby(["Year"])["Price"].mean().sort_values(ascending=True)

    # Display the Altair chart using Streamlit
    st.line_chart(data, width=50)
