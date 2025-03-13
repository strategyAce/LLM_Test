import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


def query_election_data(df, query, tokenizer, model):
    """Query the model with a specific question about the election data"""

    print(f"\nProcessing query: '{query}'")

    # Format the data into a context the model can use
    context = "Election Results Data:\n"
    context += df.to_string()

    # Prepare the prompt
    prompt = f"""
    {context}

    Question: {query}
    Answer:
    """

    # Generate a response from the model
    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        output_sequences = model.generate(
            input_ids=inputs["input_ids"],
            max_length=512,
            temperature=0.7,
            top_p=0.9,
            do_sample=True
        )

    response = tokenizer.decode(output_sequences[0], skip_special_tokens=True)

    # Extract just the answer part
    answer = response.split("Answer:")[1].strip() if "Answer:" in response else response

    return answer
