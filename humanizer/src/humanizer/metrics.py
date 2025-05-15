import nltk
from nltk.tokenize import sent_tokenize
import re

# Download NLTK resources
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

class HumanizationMetrics:
    def __init__(self):
        pass
    
    def calculate_humanization_score(self, text):
        """Calculate a humanization score based on various text features"""
        scores = {}
        
        # 1. Sentence length variation (higher variation is more human-like)
        sentences = sent_tokenize(text)
        if not sentences:
            return {"total_score": 0}
            
        sent_lengths = [len(s.split()) for s in sentences]
        avg_length = sum(sent_lengths) / len(sent_lengths)
        length_variance = sum((l - avg_length) ** 2 for l in sent_lengths) / len(sent_lengths)
        
        # Normalize variance to a 0-1 score (higher is better)
        # Typical human writing has good variance, but not extreme
        variance_score = min(length_variance / 25, 1.0)
        scores["sentence_variety"] = variance_score * 100
        
        # 2. Contraction usage (more contractions are typically more human-like)
        contraction_pattern = r"(\w+'(?:ve|re|s|d|ll|t|m))\b"
        contraction_count = len(re.findall(contraction_pattern, text))
        word_count = len(text.split())
        
        # Normalize to a score (0-1)
        contraction_ratio = contraction_count / max(word_count, 1) * 20  # Scaling factor
        contraction_score = min(contraction_ratio, 1.0)
        scores["contraction_usage"] = contraction_score * 100
        
        # 3. Personal pronouns (more first-person pronouns often indicate human writing)
        personal_pronouns = ["I", "me", "my", "mine", "we", "us", "our", "ours"]
        pronoun_count = sum(1 for word in text.split() if word.lower() in 
                          [p.lower() for p in personal_pronouns])
        
        # Normalize to a score (0-1)
        pronoun_ratio = pronoun_count / max(word_count, 1) * 30  # Scaling factor
        pronoun_score = min(pronoun_ratio, 1.0)
        scores["personal_voice"] = pronoun_score * 100
        
        # Calculate total score (weighted average)
        weights = {
            "sentence_variety": 0.4,
            "contraction_usage": 0.3,
            "personal_voice": 0.3
        }
        
        total_score = sum(scores[key] * weights[key] for key in weights)
        scores["total_score"] = round(total_score, 1)
        
        return scores