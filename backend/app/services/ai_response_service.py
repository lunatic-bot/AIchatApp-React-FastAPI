from transformers import pipeline

# Load a small, efficient chatbot model from Hugging Face
chat_model = pipeline("text-generation", model="distilgpt2")

async def get_ai_response(user_message: str) -> str:
    """Generate AI response using a local Hugging Face model."""
    response = chat_model(user_message, max_length=50, do_sample=True)
    return response[0]["generated_text"]
