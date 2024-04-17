import streamlit as st
import openai


openai.api_key = "YOUR_KEY"

def review_code(code):
    try:
        
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=f"Review this Python code and provide feedback and fixed snippets:\n\n{code}",
            max_tokens=2000,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0.5
        )

        
        feedback = response.choices[0].text
        fixed_code = feedback.split("\n\n")[-1]

        return feedback, fixed_code
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")
        return None, None

def main():
    st.title("GenAI App - AI Code Reviewer")

    
    code = st.text_area("Enter your Python code here:")

    if st.button("Review Code"):
        if code:
            feedback, fixed_code = review_code(code)
            if feedback and fixed_code:
                st.subheader("Feedback:")
                st.write(feedback)

                st.subheader("Fixed Code:")
                st.code(fixed_code, language="python")
            else:
                st.error("Failed to get feedback and fixed code.")
        else:
            st.warning("Please enter your Python code for review.")

if __name__ == "__main__":
    main()
