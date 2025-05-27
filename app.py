from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure Gemini with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini response function

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")  # Correct model name
    response = model.generate_content([prompt[0], question])
    return response.text
# SQL execution function
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        return f"Error executing SQL: {e}"

# Static prompt
prompt = ["""
You are a helpful assistant that answers questions about a SQLite database.
ONLY return a valid SQL query as your response.
Do not include explanations or natural language text.
Do not use triple backticks (```).
Start your response directly with the SQL command.
"""]

# Streamlit UI
st.set_page_config(page_title="Database Assistant", page_icon=":computer:")
st.header("🧠 Database Assistant using Gemini and SQLite")

# User input
question = st.text_input("Enter your question:", key="input")
submit = st.button("Ask the question")

# On submit
if submit and question:
    with st.spinner("Generating SQL and fetching results..."):
        response = get_gemini_response(question, prompt)
        st.subheader("Generated SQL Query:")
        st.code(response, language="sql")
        
        data = read_sql_query(response, "student.db")

        st.subheader("Query Result:")
        if isinstance(data, str) and data.startswith("Error"):
            st.error(data)
        elif data:
            st.table(data)
        else:
            st.info("No data returned for this query.")
