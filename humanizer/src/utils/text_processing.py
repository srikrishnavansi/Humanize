import re

def clean_text(text):
    """Clean and normalize text"""
    if not text:
        return ""
    
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Fix common formatting issues
    text = text.replace(" .", ".").replace(" ,", ",")
    
    return text

def count_words(text):
    """Count words in text"""
    if not text:
        return 0
    return len(text.split())

def estimate_reading_time(text, wpm=200):
    """Estimate reading time in minutes"""
    word_count = count_words(text)
    return max(1, round(word_count / wpm))