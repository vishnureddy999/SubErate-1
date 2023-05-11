import streamlit as st
import pysrt
from translate import Translator
import os

def translate_subtitle(subtitle_path, target_lang):
    # Load subtitle file
    subs = pysrt.open(subtitle_path)
    # Initialize translator
    translator = Translator(to_lang=target_lang)
    # Translate each subtitle and update the text
    for sub in subs:
        sub.text = translator.translate(sub.text)
    # Save the translated subtitle as a new file
    output_path = f"{subtitle_path.split('.')[0]}_{target_lang}.srt"
    subs.save(output_path, encoding='utf-8')
    return output_path

# Streamlit app
st.title("Subtitle Translator")

# Upload subtitle file
subtitle_path = st.file_uploader("Upload subtitle file (.srt)", type="srt")
if subtitle_path:
    # Create a temporary file path
    temp_file_path = os.path.join("/tmp", subtitle_path.name)

    # Save the uploaded file data to the temporary file
    with open(temp_file_path, "wb") as f:
        f.write(subtitle_path.getbuffer())
    # Get target language from user input
    target_lang = st.selectbox("Select target language", options=["en", "hi", "te"])
    # Translate subtitle and download output file
    if st.button("Translate"):
        output_path = translate_subtitle(temp_file_path, target_lang)
        st.success(f"Subtitle has been translated and saved as {output_path}")
