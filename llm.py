import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_guidance(user_input, career, missing_skills):
    prompt = f"""
You are an expert career advisor.

User Skills:
{user_input}

Target Career:
{career}

Missing Skills:
{", ".join(missing_skills)}

Provide response in structured format...
"""

    response = model.generate_content(prompt)
    return response.text