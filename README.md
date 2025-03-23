📧 Email Classifier App

This is a web-based application built with Streamlit that classifies emails as Spam or Not Spam using a trained Support Vector Machine (SVM) model. The app takes user input, processes the text, and instantly predicts the email category.

📌 Table of Contents

Overview
Installation
Usage
Features
Technologies Used
Contributing
License
🌟 Overview

The Email Classifier App uses Natural Language Processing (NLP) techniques with a trained SVM model to classify emails as either Spam or Not Spam. The model leverages a Count Vectorizer to transform text data into numerical form before making predictions.

⚙️ Installation

Clone the repository:
git clone https://github.com/Nonny-123/Spam-Email-Classifier.git
cd Spam-Email-Classifier
Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Ensure the model and vectorizer files are in place:
SVM_model.pkl – Pre-trained Support Vector Machine model for classification.
vectorizer.pkl – Count Vectorizer used for text preprocessing.
🚀 Usage

Run the app:
streamlit run app.py
Classifying Emails:
Enter the email content into the text area.
Click the Predict button to determine whether the email is classified as Spam or Not Spam.
🌐 Features

✅ Simple, clean, and intuitive user interface.
✅ Real-time prediction of spam or non-spam emails.
✅ Error handling for missing models and vectorizers.
✅ Instant feedback upon classification.

🏗️ Technologies Used

Python 🐍
Streamlit ⚡
Joblib 🔧
Scikit-Learn 🤖
🤝 Contributing

Contributions are welcome! Here’s how you can help:

Fork the repository.
Create a new branch.
Commit your changes and push to the branch.
Open a pull request.
📄 License

This project is licensed under the MIT License.

👨‍💻 Developed by Okonji Chukwunonyelim Gabriel.

Would you like to include performance metrics, sample predictions, or data source details? Let me know, and I’ll add them! 🚀
