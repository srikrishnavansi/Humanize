# src/humanizer/humanizer.py
from src.llm.gemini_client import GeminiClient
from src.llm.prompt_templates import PromptTemplates
from src.humanizer.metrics import HumanizationMetrics

class TextHumanizer:
    def __init__(self):
        self.llm = GeminiClient()
        self.prompts = PromptTemplates()
        self.metrics = HumanizationMetrics()
    
    def humanize_text(self, text):
        """Transform AI-generated text to appear more human-written"""
        prompt = self.prompts.humanize_text(text)
        humanized_text = self.llm.generate_text(prompt)
        
        # Calculate humanization score
        score = self.metrics.calculate_humanization_score(humanized_text)
        
        return {
            "original_text": text,
            "humanized_text": humanized_text,
            "humanization_score": score
        }
    
    def generate_content(self, topic, tone="casual", length="medium"):
        """Generate human-like content on a given topic"""
        prompt = self.prompts.generate_content_on_topic(topic, tone, length)
        content = self.llm.generate_text(prompt)
        
        # Calculate humanization score
        score = self.metrics.calculate_humanization_score(content)
        
        return {
            "topic": topic,
            "content": content,
            "humanization_score": score
        }