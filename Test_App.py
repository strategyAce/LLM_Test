

def main():
  print("Testing LLM Model")
  #load csv file
  election_df = load_election_data(CSVPATH)
  # Note: Replace with a more capable model if needed
  tokenizer, model = setup_hugging_face_model("HuggingFaceH4/zephyr-7b-beta")
  # 3. Ask the model about Precinct 99
  query = "Which Presidential candidate received more votes in Precinct 208?"
  print(f"\nQuery: {query}")
  answer = query_election_data(election_df, query, tokenizer, model)
  print(f"\nModel's answer: {answer}")
