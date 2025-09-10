# app.py
# Streamlit + Google Generative AI (Gemini) SQL Query Generator

import streamlit as st
import google.generativeai as genai

# ------------------ CONFIGURE GEMINI ------------------
GOOGLE_API_KEY = "AIzaSyCyaR50hZ36zqZVz4bdm0CGx9z3Zx6j7ls"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Gemini model (use supported model)
model = genai.GenerativeModel("gemini-2.5-pro")

# ------------------ STREAMLIT LAYOUT ------------------
st.set_page_config(page_title="SQL Query Generator", page_icon=":robot_face:")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png",
        width=280,
    )

st.markdown(
    """
    <div style='text-align: center'>
    <h1> SQL QUERY GENERATOR</h1>
    <h3>I can generate SQL queries for you</h3>
    <h4>with explanation as well</h4>
    <p>This tool allows you to generate SQL queries based on plain English input.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ------------------ USER INPUT ------------------
text_input = st.text_input("Enter your text here in plain English")
submit_button = st.button("Generate SQL Query")

# ------------------ PROCESSING ------------------
if submit_button and text_input:
    with st.spinner("Generating SQL query..."):

        # Build prompt
        template = f"""
        You are a helpful assistant.
        Convert the following request into a valid SQL query.
        Also provide a short explanation of the query.

        Request:
        '''{text_input}'''
        """

        try:
            response = model.generate_content(template)
            result = response.text

            # Extract SQL query
            if "```sql" in result:
                sql_query = result.split("```sql")[1].split("```")[0].strip()
            else:
                sql_query = result.strip()

            # Extract explanation (everything else)
            explanation = result.replace(sql_query, "").strip()

            # Show results
            with st.container():
                st.success("SQL query generated successfully!")
                st.code(sql_query, language="sql")

                st.success("Explanation of this SQL query")
                st.markdown(explanation)

        except Exception as e:
            st.error(f"Error generating SQL: {e}")
