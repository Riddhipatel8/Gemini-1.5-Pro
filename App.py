import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load the API key from the .env file
load_dotenv()
api_key = os.getenv('API_KEY')

# Configure the generative AI model
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Streamlit app
st.title('Generative AI Content Generator')

# User input for the content description
user_input = st.text_area('Write a Prompt:', height=100)

if st.button('Generate Content'):
    if user_input:
        response = model.generate_content(user_input)
        st.write('Generated Content:')
        st.write(response.text)
    else:
        st.warning('Please write a Prompt:')

