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
    """)
    st.markdown("---")

    # User Input Section
    st.subheader("User Inputs")
    hobby = st.text_input("What is your hobby?")
    favorite_subject = st.text_input("What is your favorite subject?")
    financial_budget = st.select_slider("Select your financial budget", options=["Low", "Medium", "High"])
    course_complexity = st.radio("Select the desired course complexity", options=["Beginner", "Intermediate", "Advanced"])
    country = st.text_input("Enter the country you want to study in:")
    university = st.text_input("Enter the specific university (if any):")

    st.markdown("---")

    # Generate Button
    if st.button("Get Course Suggestions"):
        if hobby and favorite_subject and country and university:
            # Generate suggestions
            generated_text = generate_content([hobby, favorite_subject, financial_budget, course_complexity, country, university])

            # Display suggestions
            st.subheader("College Course Suggestions:")
            st.write(generated_text)
        else:
            st.warning("Please provide your hobby, favorite subject, financial budget, desired course complexity, country, and university.")

if __name__ == "__main__":
    main()
