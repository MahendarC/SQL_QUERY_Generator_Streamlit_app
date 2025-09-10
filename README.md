# SQL_QUERY_Generator_Streamlit_app

#  SQL Query Generator with Streamlit + Google Gemini AI

This project is a **Streamlit web application** that generates **SQL queries from plain English text** using **Google Generative AI (Gemini)**.  
It also provides explanations of the generated queries to help you understand them better. 🚀

---

## Features
-  Convert plain English text into SQL queries  
-  Get explanation of the generated SQL query  
-  Interactive **Streamlit UI**  
-  Powered by **Google Gemini 2.5 Pro model**  
-  Simple and lightweight  

---

##  Installation

Clone this repository:

bash
git clone https://github.com/<your-username>/sql-query-generator.git
cd sql-query-generator










Install Python 3.8 or higher.
Check version with: python --version

Create and activate a virtual environment inside your project folder (D:\mahendar practice).
Command: python -m venv venv
Activate (Windows): venv\Scripts\activate

Install the required packages:
pip install streamlit
pip install google-generativeai
pip install python-dotenv

Create a file named .env in your project folder and put this inside it:
GOOGLE_API_KEY=AIzaSyCyaR50hZ36zqZVz4bdm0CGx9z3Zx6j7ls

Create a file named app.py in your project folder and paste this code:
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

st.title("SQL Generator with Google Gemini")

user_input = st.text_area("Enter your plain English query:", "")

if st.button("Generate SQL"):
if user_input.strip() == "":
st.warning("Please enter some text!")
else:
try:
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(
f"Convert this request into an SQL query: {user_input}"
)
st.subheader("Generated SQL Query:")
st.code(response.text, language="sql")
except Exception as e:
st.error(f"Error generating SQL: {str(e)}")

Run the app from your project folder:
streamlit run app.py

App will open in browser at http://localhost:8501
