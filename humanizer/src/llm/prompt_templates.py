# src/llm/prompt_templates.py
class PromptTemplates:
    @staticmethod
    def humanize_text(text):
        """Prompt template for humanizing text"""
        return f"""
        # TASK: HUMANIZE THE FOLLOWING TEXT
        
        I need you to rewrite the following text to make it sound completely human-written. 
        
        ## IMPORTANT INSTRUCTIONS:
        1. Maintain the same meaning and key information
        2. Introduce natural human elements:
           - Vary sentence structures and lengths (mix short and long sentences)
           - Add occasional informal language, contractions, or filler words
           - Include subjective expressions or personal opinions where appropriate
           - Use analogies, metaphors, or examples that a human might use
           - Add mild imperfections (thoughtful pauses, slight conversational tangents)
        3. Avoid overly formal or perfect structure
        4. Make the tone conversational and authentic
        5. Reduce repetitive sentence structures
        
        ## TEXT TO HUMANIZE:
        {text}
        
        ## OUTPUT FORMAT:
        Return ONLY the humanized text without explanations, prefixes, or notes.
        """
    
    @staticmethod
    def generate_content_on_topic(topic, tone="casual", length="medium"):
        """Prompt template for generating content on a topic"""
        length_guide = {
            "short": "300-500 words",
            "medium": "700-1000 words",
            "long": "1500-2000 words"
        }
        
        tone_guide = {
            "casual": "conversational, friendly, using contractions and occasional slang",
            "professional": "knowledgeable but approachable, like a blog written by an industry expert",
            "academic": "thoughtful and nuanced, but still accessible to non-experts"
        }
        
        return f"""
        # TASK: WRITE HUMAN-LIKE CONTENT ON A TOPIC
        
        Write a {length_guide[length]} piece about "{topic}" in a {tone_guide[tone]} tone.
        
        ## IMPORTANT INSTRUCTIONS:
        1. Write as a human would, with:
           - Personal anecdotes or opinions where appropriate
           - Varied sentence structures (mix of simple and complex)
           - Occasional use of questions or rhetorical questions
           - Natural flow with transitions between ideas
           - Some paragraph breaks for readability
           - Contractions and conversational language
        2. Include imperfections that make writing human:
           - Occasional parenthetical thoughts
           - Some informal expressions
           - Varied paragraph lengths
        3. Avoid overly structured writing with perfectly balanced points
        4. Write in first person where appropriate
        
        ## OUTPUT FORMAT:
        Return ONLY the human-like content without explanations, prefixes, or notes.
        """