import streamlit as st
import pandas as pd

def load_election_data(file_path):
    """Load and display election results from a CSV file"""

    print(f"Loading election data from {file_path}...")

    # Load the CSV file
    df = pd.read_csv(file_path)

    # Display the first few rows to understand the data
    st.print("Preview of election data:")
    #display(df.head())

    # Display basic information about the dataset
    st.print("\nDataset information:")
    st.print(f"Number of rows: {len(df)}")
    st.print(f"Columns: {', '.join(df.columns)}")

    return df
