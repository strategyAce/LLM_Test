from transformers import AutoTokenizer, AutoModelForCausalLM

def setup_hugging_face_model(model_name="HuggingFaceH4/tiny-random-LlamaForCausalLM"):
    """Setup a model from Hugging Face (using a small test model by default)"""

    print(f"\nSetting up Hugging Face model: {model_name}")

    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    print(f"Model and tokenizer loaded successfully")

    return tokenizer, model
