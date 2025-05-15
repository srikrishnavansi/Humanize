# app.py
import streamlit as st
from src.humanizer.humanizer import TextHumanizer
from src.utils.text_processing import count_words, estimate_reading_time
import time

# Initialize the humanizer
humanizer = TextHumanizer()

# Set page configuration
st.set_page_config(
    page_title="AI Text Humanizer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with improved colors for better visibility
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
    }
    .subheader {
        font-size: 1.5rem;
        color: #424242;
    }
    .score-container {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f0f2f6;
        margin-bottom: 1rem;
    }
    .humanized {
        background-color: #e3f2fd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #1976d2;
        color: #000000;
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: black;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .stTabs [aria-selected="true"] {
        background-color: black !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='main-header'>AI Text Humanizer</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Transform AI-generated content into natural, human-like writing</p>", unsafe_allow_html=True)

# Sidebar
st.sidebar.image("https://img.icons8.com/fluency/96/000000/brain.png", width=80)
st.sidebar.title("Options")

# Tabs for different functionalities
tab1, tab2 = st.tabs(["Humanize Text", "Generate Content"])

# Tab 1: Humanize existing text
with tab1:
    st.header("Humanize Your Text")
    st.write("Paste your text below to make it sound more human-written.")
    
    input_text = st.text_area("Text to humanize:", height=200)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Humanize", key="humanize_btn", use_container_width=True):
            if input_text:
                with st.spinner("Humanizing your text..."):
                    # Add a slight delay to make the processing feel more substantial
                    time.sleep(1)
                    result = humanizer.humanize_text(input_text)
                    
                    # Store the result in session state for download button
                    st.session_state.humanized_result = result
                    
                    # Display results
                    st.markdown("### Humanized Text:")
                    st.markdown(f"<div class='humanized'>{result['humanized_text']}</div>", unsafe_allow_html=True)
                    
                    # Display metrics
                    st.markdown("### Humanization Metrics")
                    col_a, col_b, col_c = st.columns(3)
                    
                    with col_a:
                        st.metric("Overall Score", f"{result['humanization_score']['total_score']}%")
                    with col_b:
                        st.metric("Sentence Variety", f"{result['humanization_score']['sentence_variety']:.1f}%")
                    with col_c:
                        st.metric("Personal Voice", f"{result['humanization_score']['personal_voice']:.1f}%")
                    
                    # Display word counts
                    original_count = count_words(input_text)
                    humanized_count = count_words(result['humanized_text'])
                    reading_time = estimate_reading_time(result['humanized_text'])
                    
                    st.markdown(f"**Word count:** {humanized_count} words (original: {original_count})")
                    st.markdown(f"**Estimated reading time:** {reading_time} min")
            else:
                st.error("Please enter some text to humanize.")
    
    with col2:
        # Use session state to maintain the download button state
        if 'humanized_result' in st.session_state:
            st.download_button(
                label="Download Humanized Text",
                data=st.session_state.humanized_result['humanized_text'],
                file_name="humanized_text.txt",
                mime="text/plain",
                use_container_width=True
            )

# Tab 2: Generate content
with tab2:
    st.header("Generate Human-Like Content")
    st.write("Generate original content on any topic that sounds naturally human-written.")
    
    topic = st.text_input("Topic or subject:", placeholder="E.g., Benefits of meditation for productivity")
    
    col1, col2 = st.columns(2)
    with col1:
        tone = st.selectbox(
            "Tone:",
            options=["casual", "professional", "academic"],
            format_func=lambda x: {
                "casual": "Casual & Conversational",
                "professional": "Professional & Informative",
                "academic": "Academic & Thoughtful"
            }[x]
        )
    
    with col2:
        length = st.selectbox(
            "Length:",
            options=["short", "medium", "long"],
            format_func=lambda x: {
                "short": "Short (300-500 words)",
                "medium": "Medium (700-1000 words)",
                "long": "Long (1500-2000 words)"
            }[x]
        )
    
    if st.button("Generate Content", key="generate_btn", use_container_width=True):
        if topic:
            with st.spinner(f"Generating human-like content about '{topic}'..."):
                # Add a slight delay to make the processing feel more substantial
                time.sleep(1)
                result = humanizer.generate_content(topic, tone, length)
                
                # Store the result in session state for download button
                st.session_state.generated_result = result
                
                # Display results
                st.markdown("### Generated Content:")
                st.markdown(f"<div class='humanized'>{result['content']}</div>", unsafe_allow_html=True)
                
                # Display metrics
                st.markdown("### Humanization Metrics")
                col_a, col_b, col_c = st.columns(3)
                
                with col_a:
                    st.metric("Overall Score", f"{result['humanization_score']['total_score']}%")
                with col_b:
                    st.metric("Sentence Variety", f"{result['humanization_score']['sentence_variety']:.1f}%")
                with col_c:
                    st.metric("Personal Voice", f"{result['humanization_score']['personal_voice']:.1f}%")
                
                # Display word counts
                word_count = count_words(result['content'])
                reading_time = estimate_reading_time(result['content'])
                
                st.markdown(f"**Word count:** {word_count} words")
                st.markdown(f"**Estimated reading time:** {reading_time} min")
                
                # Download button
                st.download_button(
                    label="Download Generated Content",
                    data=result['content'],
                    file_name=f"{topic.lower().replace(' ', '_')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
        else:
            st.error("Please enter a topic for content generation.")

# Footer
st.markdown("---")
st.markdown("Use this tool ethically and responsibly. Not intended for academic dishonesty.")