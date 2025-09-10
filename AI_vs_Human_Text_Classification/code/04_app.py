import streamlit as st
import joblib
import numpy as np

# Set page config
st.set_page_config(page_title="AI vs Human Text Detector", layout="centered")

# Load model and vectorizer
@st.cache_resource
def load_model_and_vectorizer():
    model = joblib.load("nb_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_model_and_vectorizer()

# Application Title
st.title("AI vs Human Text Detector")
st.write("Enter a paragraph or sentence below. The model will classify it as **AI-generated** or **Human-written**.")

# Input text
user_input = st.text_area("Enter text here:", height=200)

# Output Prediction
if st.button("🔍 Classify"):
    if not user_input.strip():
        st.warning("Please enter some text.")
    else:
        # Vectorize input
        input_vector = vectorizer.transform([user_input])

        # Predict
        predicted_label = model.predict(input_vector)[0]
        probabilities = model.predict_proba(input_vector)[0]

        # Mapping
        label_map = {1: "Human-Written", 0: "AI-Generated"}
        prediction_text = label_map.get(predicted_label, "Unknown")

        # Prediction Result
        st.subheader("Prediction")
        st.markdown(f"**{prediction_text}**")

        st.subheader("Confidence Scores")
        st.write("Confidence AI-Generated")
        st.progress(float(probabilities[0]))
        st.write("Confidence Human-Written")
        st.progress(float(probabilities[1]))

        st.json({
            "Human-Written (1)": f"{probabilities[1]:.2f}",
            "AI-Generated (0)": f"{probabilities[0]:.2f}"
        })
