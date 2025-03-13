import streamlit as st
from src.initializeshared import initialize_shared

def main():
  st.title("Testing LLM Model App")
  
  #load csv file
  election_df = load_election_data(CSVPATH)
  
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
