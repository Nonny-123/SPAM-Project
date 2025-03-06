import streamlit as st
import joblib

try:
    model = joblib.load("SVM_model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
except FileNotFoundError:
    st.error("Model or Vectorizer not found. Please ensure 'svc_model.pkl' and 'count_vectorizer.pkl' are in the same directory")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the model or vectorizer: {e}")
    st.stop()

def predict_email(email_text):
    vectorized_email = vectorizer.transform([email_text])
    prediction = model.predict(vectorized_email)[0]
    return prediction

st.title("Email Classifier App")
st.subheader("Enter an Email to determine if it is spam or not")

email_input = st.text_area("Enter Email text here")

if st.button("Predict"):
    if email_input:
        prediction = predict_email(email_input)
        if prediction == 1:
            st.info("Prediction: Spam")
        else:
            st.info('Prediction: Not Spam')
    else:
        st.warning("Please enter email text")

