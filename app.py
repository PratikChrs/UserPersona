import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
import google.generativeai as genai

# Load Gemini API Key from .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")
# Set page config
st.set_page_config(page_title="Reddit Persona Viewer", layout="wide")

st.title("🧠 Reddit Persona Viewer")

# List HTML persona files
output_dir = "output"
html_files = [f for f in os.listdir(output_dir) if f.endswith(".html")]

if not html_files:
    st.warning("No HTML persona profiles found. Run main.py first to generate one.")
else:
    selected_file = st.selectbox("Select a Reddit persona profile to view:", html_files)

    html_path = os.path.join(output_dir, selected_file)

    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        html_prompt = f"""
You are a web content formatter. Convert the following text block into clean and readable HTML:

- Wrap all Reddit URLs inside clickable <a href="...">...</a> tags.
- Use <h2> for major sections (like Age, Location, Profession, etc.).
- Use <strong> or <b> for key labels (e.g. "Estimate:", "Quote:", "Source:").
- Use <ul> or <ol> and <li> for lists.
- Preserve paragraph breaks.
- Do not remove or alter quotes or content.

TEXT TO FORMAT:
{html_content}
"""
    response = model.generate_content(html_prompt)
    formatted_html = response.text

    # Display in an HTML container
    st.components.v1.html(formatted_html, height=800, scrolling=True)
