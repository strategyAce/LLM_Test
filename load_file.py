import padas as pd

def load_election_data(file_path):
    """Load and display election results from a CSV file"""

    print(f"Loading election data from {file_path}...")

    # Load the CSV file
    df = pd.read_csv(file_path)

    # Display the first few rows to understand the data
    print("\nPreview of election data:")
    display(df.head())

    # Display basic information about the dataset
    print("\nDataset information:")
    print(f"Number of rows: {len(df)}")
    print(f"Columns: {', '.join(df.columns)}")

    return df
