import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure the API key
genai.configure(api_key=GOOGLE_API_KEY)

# Create Gemini Pro model
model = genai.GenerativeModel('gemini-pro')

def chat_with_gemini(query: str) -> str:
    """
    Send a query to Gemini and get a response
    
    Args:
        query (str): The question or prompt to send to Gemini
        
    Returns:
        str: Gemini's response text
    """
    # Start a new chat
    chat = model.start_chat(history=[])
    
    try:
        # Send the query to Gemini and get response
        response = chat.send_message(query)
        return response.text
    
    except Exception as e:
        return f"Error communicating with Gemini: {str(e)}"

if __name__ == "__main__":
    if not GOOGLE_API_KEY:
        print("Error: GOOGLE_API_KEY must be set in .env file")
        print("Create a .env file and add the following line:")
        print("GOOGLE_API_KEY=your-api-key-here")
    else:
        # Example usage
        question = "What is the capital of France?"
        answer = chat_with_gemini(question)
        print(f"Question: {question}")
        print(f"Answer: {answer}")
