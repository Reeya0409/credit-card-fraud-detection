💳 AI-Powered Credit Card Fraud Detection System

🔗 Live Demo: https://credit-card-fraud-detection-1-thwy.onrender.com

---

📌 Overview

This project is a machine learning-based web application that detects fraudulent credit card transactions. It classifies transactions as fraudulent or normal and provides real-time predictions through an interactive user interface.

---

🚨 Problem Statement   

Credit card fraud is a major issue due to the rapid growth of online transactions. Detecting fraud is challenging because:   

Fraud cases are very rare (imbalanced dataset)   
Patterns are complex and hidden   

The goal is to build a system that can accurately detect fraudulent transactions and reduce financial risk.   

---

⚙️ Features   

🔍 Real-time fraud detection   
⚡ Quick Test (instant demo scenarios)   
🔬 Advanced Input for transaction simulation   
🎲 Auto-fill sample data   
📊 Fraud probability visualization   

---

🧠 Technologies Used   

Python   
Scikit-learn   
Pandas, NumPy   
Streamlit   
SMOTE (Imbalanced Data Handling)   

---

🤖 Machine Learning Approach   

🔹 Data Preprocessing   
Feature scaling using StandardScaler   
Handling imbalanced dataset using SMOTE     

🔹 Model Used   
Random Forest Classifier   
Handles complex patterns   
Reduces overfitting   
Provides high accuracy   

🔹 Evaluation Metrics   
Accuracy   
Confusion Matrix   
Classification Report   

---

🖥️ Application Interface   

🏠 Overview   
Information about fraud and prevention   

⚡ Quick Test   
Test predefined normal and fraud scenarios   

🔬 Advanced Input   
Simulate full transaction data   
Predict fraud probability   

---

📊 How It Works   

User inputs transaction data   
Data is scaled using trained scaler   
Model predicts fraud or normal   
Probability score is displayed   

---

🚀 Future Improvements   
Integration with real-time banking systems   
Use of deep learning models   
Explainable AI for better interpretation   
Deployment as API   

---

📂 Project Structure   
├── app.py   
├── fraud_model.pkl   
├── scaler.pkl   
├── creditcard.ipynb   
├── requirements.txt   
├── screeshot1   
├── screenshot2   
├── demo   
├── confusion_matrix   
└── README.md   

---

📎 Installation (Run Locally)   
git clone https://github.com/Reeya0409/credit-card-fraud-detection.git   
cd credit-card-fraud-detection   
pip install -r requirements.txt   
streamlit run app.py   

---

📚 References   
Kaggle Credit Card Fraud Dataset   
Scikit-learn Documentation   

---

👨‍💻 Author   
Reeya Sharma   

⭐ If you like this project, give it a star!
