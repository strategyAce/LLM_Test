import streamlit as st
from src.initializeshared import initialize_shared

def main():
  st.title("Testing LLM Model App")

  with st.container(border=True):
    # Data source selection
    uploaded_file = None
    drive_path = None
    if data_source == "Local file upload":
        uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
      
  
  #load csv file
  election_df = load_election_data(uploaded_file)
  
  # Note: Replace with a more capable model if needed
  tokenizer, model = setup_hugging_face_model("HuggingFaceH4/zephyr-7b-beta")
  
  # Ask the model about Precinct 99
  query = "Which Presidential candidate received more votes in Precinct 208?"
  answer = query_election_data(election_df, query, tokenizer, model)
  st.write(f"Query: {query}")
  st.write("")
  st.write(f"Model's answer: {answer}")
  
if __name__ == "__main__":
    main()
