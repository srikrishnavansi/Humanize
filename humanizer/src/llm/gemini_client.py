import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiClient:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config={
                "temperature": 0.9,  # Higher temperature for more creative/varied outputs
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 8192,
            }
        )
    
    def generate_text(self, prompt):
        """Generate text using Gemini model"""
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error generating text: {e}")
            return None