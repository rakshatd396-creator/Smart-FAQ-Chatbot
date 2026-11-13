import streamlit as st
import ollama

# Read syllabus
with open("syllabus.txt", "r") as file:
    syllabus = file.read()

# Prompt template
prompt_template = """
You are a helpful College FAQ Chatbot.

Answer questions using the syllabus below.
Give simple and clear answers.

If information is not available,
say that it is not available in the syllabus.

Syllabus:
{syllabus}

Question:
{question}

Answer:
"""

# Chatbot interface
st.title("Smart FAQ Chatbot")
st.write("Ask questions about your course syllabus.")

question = st.text_input("Enter your question")

if st.button("Ask"):

    if question:
        prompt = prompt_template.format(
            syllabus=syllabus,
            question=question
        )

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        st.subheader("Answer")
        st.write(response["message"]["content"])

    else:
        st.warning("Please enter a question.")