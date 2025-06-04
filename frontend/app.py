import streamlit as st
import requests

# Title of the app
st.title("Sentiment Analyzer (Mistral)")

# Text input field
text_input = st.text_area("Enter your sentence here:")

# Button to trigger analysis
if st.button("Analyze"):
    # Send POST request to FastAPI backend
    res = requests.post("http://localhost:8000/analyze/", data={"text": text_input})

    # Get the sentiment from the response
    sentiment = res.json().get("sentiment", "Error")

    # Display the result
    st.subheader("Predicted Sentiment:")
    st.write(sentiment)
