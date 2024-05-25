import streamlit as st
import google.generativeai as genai
import os

# Function to generate content
def generate_content(prompts):
    # Configuration
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048
    }

    # Initialize Model
    model = genai.GenerativeModel("gemini-pro", generation_config=generation_config)

    # Combine prompts into a single prompt
    combined_prompt = " ".join(prompts)

    # Generate Content
    response = model.generate_content([combined_prompt])
    return response.text

# Streamlit UI
def main():
    st.title("College Course Suggestion")
    
    text = """\n\nROCHELLE ANNE DINAQUE BSCS 3B
    \nCCS 229 - Intelligent Systems
    Computer Science Department
    College of Information and Communications Technology
    West Visayas State University"""
    st.text(text)
    st.write("Final Project in CCS 229 - Intelligent Systems")
    st.write("This application allows you to generate text content using the Generative AI model. Prompting is the process of providing a starting point or context to the Generative AI Model. You can enter a sentence, phrase, or keywords into the text input below to prompt the model. The model will then use this prompt to generate text content from the provided input.")
    st.write("To get started, enter your details in the fields below. Once you've entered your details, click the 'Get Course Suggestions' button to generate text based on your input. You can experiment with different inputs to see how the generated content changes.\n\n\n")

    # Input prompts from the user
    hobby = st.text_input("What is your hobby?")
    favorite_subject = st.text_input("What is your favorite subject?")
    financial_budget = st.select_slider("Select your financial budget", options=["Low", "Medium", "High"])
    course_complexity = st.radio("Select the desired course complexity", options=["Beginner", "Intermediate", "Advanced"])
    country = st.text_input("Enter the country you want to study in:")
    university = st.text_input("Enter the specific university (if any):")

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
            generated_text = generate_content(prompts)
            st.subheader("College Course Suggestions:")
            st.write(generated_text)
        else:
            st.warning("Please provide your current place, hobby, favorite subject, desired country, and university.")

if __name__ == "__main__":
    main()
