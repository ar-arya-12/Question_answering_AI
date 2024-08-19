import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# Function to return the response
def load_answer(question):
    # Initialize the LLM with the Google Generative AI model
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    
    # Generate the answer using the LLM
    answer = llm.invoke(question)
    return answer

# App UI starts here
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")

# Gets the user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text

user_input = get_text()

# Only call load_answer if there is user input
if user_input:
    response = load_answer(user_input)
else:
    response = "Please enter a question"

submit = st.button('Generate')

# If generate button is clicked
if submit:
    st.subheader("Answer:")
    st.write(response)
