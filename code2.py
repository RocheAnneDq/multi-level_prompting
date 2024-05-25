import streamlit as st
import google.generativeai as genai
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Function to generate content
def generate_content(prompts, api_client):
    # Combine prompts into a single prompt
    combined_prompt = " ".join(prompts)

    # Generate Content
    response = api_client.generate_content(prompt=combined_prompt)
    return response['text']

# Authenticate with Google API
def authenticate():
    # Load service account credentials
    credentials = service_account.Credentials.from_service_account_file(
        'path/to/service-account-file.json',
        scopes=['https://www.googleapis.com/auth/generative_language_api_scope']
    )

    # Build Google API client
    api_client = build('generativelanguage', 'v1beta', credentials=credentials)
    return api_client

# Streamlit UI
def main():
    # Set page title and favicon
    st.set_page_config(page_title="College Course Suggestion", page_icon=":mortar_board:")

    # Header
    st.title("College Course Suggestion")
    st.markdown("---")

    # Additional Information
    text = """
    **ROCHELLE ANNE DINAQUE**  
    *BSCS 3B*  
    CCS 229 - Intelligent Systems  
    Computer Science Department  
    College of Information and Communications Technology  
    West Visayas State University
    """
    st.markdown(text)
    st.write("Final Project in CCS 229 - Intelligent Systems")
    st.markdown("---")

    # About
    st.subheader("About")
    st.write("""
    This application allows you to generate text content using the Generative AI model. 
    Prompting is the process of providing a starting point or context to the Generative AI Model. 
    You can enter a sentence, phrase, or keywords into the text input below to prompt the model. 
    The model will then use this prompt to generate text content from the provided input.
    \nTo get started, enter your details in the fields below. Once you've entered your details, click the 'Get Course Suggestions' button to generate text based on your input. You can experiment with different inputs to see how the generated content changes.
    """)
    st.markdown("---")

    # Input prompts from the user
    hobby = st.text_input("What is your hobby?")
    favorite_subject = st.text_input("What is your favorite subject?")
    financial_budget = st.select_slider("Select your financial budget", options=["Low", "Medium", "High"])
    course_complexity = st.radio("Select the desired course complexity", options=["Beginner", "Intermediate", "Advanced"])
    country = st.text_input("Enter the country you want to study in:")
    university = st.text_input("Enter the prefer university (if any):")

    # Generate prompt based on user inputs
    prompts = [
        f"Hobby: {hobby}",
        f"Favorite subject: {favorite_subject}",
        f"Financial budget: {financial_budget}",
        f"Course complexity: {course_complexity}",
        f"Country: {country}",
        f"University: {university}"
    ]

    # Button to generate content
    if st.button("Get Course Suggestions"):
        if hobby and favorite_subject and country and university:
            api_client = authenticate()
            generated_text = generate_content(prompts, api_client)
            st.subheader("College Course Suggestions:")
            st.write(generated_text)
        else:
            st.warning("Please provide your hobby, favorite subject, desired country, and university.")

if __name__ == "__main__":
    main()
