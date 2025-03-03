import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit app title
st.title("AI Personalized Email Generator")

# User inputs
st.sidebar.header("Recipient Details")
recipient_name = st.sidebar.text_input("Recipient Name")
recipient_company = st.sidebar.text_input("Recipient Company")
email_purpose = st.sidebar.text_area("Purpose of the Email")
tone = st.sidebar.selectbox("Tone of the Email", ["Formal", "Friendly", "Professional", "Casual"])

# Generate email button
if st.sidebar.button("Generate Email"):
    if recipient_name and recipient_company and email_purpose:
        # Create a prompt for the AI
        prompt = f"Write a {tone.lower()} email to {recipient_name} from {recipient_company} about {email_purpose}."

        # Call OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the appropriate model
            prompt=prompt,
            max_tokens=200,  # Adjust based on email length
            temperature=0.7,  # Controls creativity
        )

        # Display the generated email
        generated_email = response.choices[0].text.strip()
        st.subheader("Generated Email")
        st.write(generated_email)
    else:
        st.error("Please fill in all the recipient details.")

# Instructions for the user
st.markdown("""
### How to Use:
1. Enter the recipient's name, company, and the purpose of the email in the sidebar.
2. Select the tone of the email (e.g., Formal, Friendly).
3. Click the "Generate Email" button.
4. The AI will generate a personalized email for you!
""")
