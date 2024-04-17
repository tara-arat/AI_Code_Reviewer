import streamlit as st
from openai import OpenAI

# Set up the OpenAI API with your API key
OPEN_API_KEY = "Your_API"
client = OpenAI(api_key=OPEN_API_KEY)

def review_code(code):
    # Call OpenAI API to generate response
    response = client.Completions.create(
        engine="davinci",
        prompt=f"Review this Python code and provide feedback and fixed snippets:\n\n{code}",
        max_tokens=200,
        temperature=0.7,
        top_p=1,
        n=1,
        stop=None
    )
    # Return the response
    return response.choices[0].text.strip() if response and response.choices else None

def main():
    st.title("GenAI App - AI Code Reviewer")

    # Get the user's Python code
    code = st.text_area("Enter your Python code here:")

    if st.button("Review Code"):
        if code:
            with st.spinner('Generating...'):
                feedback = review_code(code)
            if feedback:
                st.subheader("Feedback:")
                st.write(feedback)
            else:
                st.error("Oops! Something went wrong. Please check your code and try again.")
        else:
            st.warning("Please enter your Python code for review.")

if __name__ == "__main__":
    main()
