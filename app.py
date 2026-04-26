import streamlit as st
import numpy as np
import pickle
scaler = pickle.load(open("scaler.pkl", "rb"))


# Load model
model = pickle.load(open("fraud_model.pkl", "rb"))

st.set_page_config(page_title="Fraud Detection", layout="wide")

# ---------- CUSTOM STYLE ----------
st.markdown("""
<style>
            
.block-container {
    padding-top: 0rem !important;
}
header {
    visibility: hidden;
}

            
/* FORCE TEXT COLOR FIX */
html, body, [class*="css"] {
    color: #f1f5f9 !important;
}

/* Markdown text */
[data-testid="stMarkdownContainer"] {
    color: #f1f5f9 !important;
}

/* Labels (sliders, inputs) */
label, .stSlider label {
    color: #e2e8f0 !important;
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: #f1f5f9 !important;
}

/* MAIN BACKGROUND */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: #020617;
}

/* TITLE */
.big-title {
    font-size: 48px;
    font-weight: bold;
    text-align: center;
    background: linear-gradient(90deg, #22c55e, #4ade80);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 20px;
}

/* CARD EFFECT */
.block-container {
    padding-top: 2rem;
}


/* BUTTONS */
.stButton>button {
    background: linear-gradient(90deg, #22c55e, #16a34a);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    font-weight: 600;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #16a34a, #22c55e);
}

/* METRICS */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.05);
    border-radius: 15px;
    padding: 15px;
    text-align: center;
}

/* SLIDERS */
.stSlider > div {
    padding: 10px;
}

/* PROGRESS BAR */
.stProgress > div > div {
    background-color: #22c55e;
}
            
/* SECTION HEADINGS */
h2, h3 {
    border-left: 4px solid #22c55e;
    padding-left: 10px;
    margin-top: 10px;
}

/* DIVIDER IMPROVEMENT */
hr {
    border: none;
    height: 1px;
    background: linear-gradient(to right, transparent, #22c55e, transparent);
    margin: 20px 0;
}

p {
    color: #cbd5f5;
    font-size: 15px;
}
            
h1, h2, h3 {
    color: #ffffff;
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="big-title">💳 AI-Powered Fraud Detection System</div>', unsafe_allow_html=True)
# st.divider()

# ---------- SIDEBAR ----------
menu = ["🏠 Overview", "⚡ Quick Test", "🔬 Advanced Input"]
choice = st.sidebar.radio("Navigation", menu)

# ---------- OVERVIEW ----------
if choice == "🏠 Overview":

    col1, col2, col3 = st.columns(3)

    col1.metric("Model", "Random Forest")
    col2.metric("Features", "30")
    col3.metric("Fraud Rate", "0.17%")

    col4, col5 = st.columns(2)

    col4.metric("Accuracy", "99.8%")  # replace with your actual value
    col5.metric("Model Type", "Supervised ML")

    st.markdown("---")
    st.markdown("### 📊 Model Performance")

    st.image("confusion_matrix.png", caption="Confusion Matrix")


    st.markdown("---")
    with st.container():
        st.markdown("### 💳 About Credit Card Fraud")
        st.write("""
        Credit card fraud occurs when unauthorized transactions are made using someone’s card details.
        With the growth of online payments, fraud has become more sophisticated and harder to detect.
        """)

        st.markdown("### 🚨 Common Types of Fraud")
        st.write("""
        - **Online Transaction Fraud** – stolen card details used for online purchases  
        - **Card Skimming** – data stolen via ATM or POS devices  
        - **Phishing Attacks** – users tricked into sharing card details  
        - **Identity Theft** – fraudster uses personal information to access accounts  
        """)

        st.markdown("### 🛡️ How to Prevent Fraud")
        col1, col2 = st.columns(2)

        with col1:
            st.success("""
            ✔ Never share OTP or CVV  
            ✔ Use secure websites (HTTPS)  
            ✔ Enable transaction alerts  
            ✔ Use strong passwords  
            """)

        with col2:
            st.warning("""
            ⚠ Avoid public Wi-Fi for payments  
            ⚠ Don’t save card details on unknown sites  
            ⚠ Regularly check bank statements  
            ⚠ Block card immediately if suspicious activity occurs  
            """)

        st.markdown("---")

    
        st.markdown("### 🎯 Objective")
        st.success("""
        Build a reliable system that can identify fraudulent transactions 
        with high recall while maintaining good precision.
        """)

    
# ---------- QUICK TEST ----------
elif choice == "⚡ Quick Test":

    st.markdown("## ⚡ Instant Fraud Testing")

    st.write("""
    This section allows you to quickly test the model using predefined scenarios.
    It helps demonstrate how the model behaves without manually entering all features.
    """)

    col1, col2 = st.columns(2)

    # NORMAL TEST
    if col1.button("🟢 Test Normal Transaction"):
        sample = np.zeros(30)
        prob = model.predict_proba(sample.reshape(1, -1))[0][1]

        st.success("Prediction: Normal Transaction")
        st.write(f"Fraud Probability: {round(prob*100,2)}%")
        st.progress(int(prob * 100))

    # FRAUD TEST
    if col2.button("🔴 Test Fraud Transaction"):
        sample = np.random.uniform(-5, 5, 30)
        prob = model.predict_proba(sample.reshape(1, -1))[0][1]

        st.error("Prediction: Fraud Transaction")
        st.write(f"Fraud Probability: {round(prob*100,2)}%")
        st.progress(int(prob * 100))

    st.markdown("---")

    st.markdown("### 🧪 What This Demonstrates")
    st.info("""
    - How the model reacts to different input patterns  
    - Difference between normal and suspicious transactions  
    - Real-time prediction capability  
    """)

    st.markdown("### 📊 Interpretation Tip")
    st.write("""
    - Higher fraud probability → more suspicious transaction  
    - Model decisions are based on learned patterns, not fixed rules  
    """)

# ---------- ADVANCED INPUT ----------
elif choice == "🔬 Advanced Input":

    st.markdown("## 🔬 Enter Full Transaction Data")
    st.info("These features are anonymized using PCA and represent hidden transaction patterns.")
    st.warning("⚠️ These values are not manually known. Use Quick Test for demo OR try random values to simulate transactions.")

    features = []

    col1, col2, col3 = st.columns(3)

    feature_names = [f"Transaction Pattern {i}" for i in range(1, 29)]

    # 🎲 Auto Fill
    if st.button("🎲 Auto Fill Sample Data"):
        st.session_state["auto_fill"] = list(np.random.uniform(-3, 3, 29)) + [np.random.uniform(0, 5000)]

    # TIME
    default_val = 0
    if "auto_fill" in st.session_state:
        default_val = int(st.session_state["auto_fill"][0])

    time = st.slider("Time", 0, 200000, default_val)
    features.append(time)

    idx = 1

    # Column 1
    with col1:
        for i in range(0, 10):
            default_val = 0.0
            if "auto_fill" in st.session_state:
                default_val = float(st.session_state["auto_fill"][idx])

            val = st.slider(feature_names[i], -10.0, 10.0, default_val)
            features.append(val)
            idx += 1

    # Column 2
    with col2:
        for i in range(10, 20):
            default_val = 0.0
            if "auto_fill" in st.session_state:
                default_val = float(st.session_state["auto_fill"][idx])

            val = st.slider(feature_names[i], -10.0, 10.0, default_val)
            features.append(val)
            idx += 1

    # Column 3
    with col3:
        for i in range(20, 28):
            default_val = 0.0
            if "auto_fill" in st.session_state:
                default_val = float(st.session_state["auto_fill"][idx])

            val = st.slider(feature_names[i], -10.0, 10.0, default_val)
            features.append(val)
            idx += 1

        default_val = 0.0
        if "auto_fill" in st.session_state:
            default_val = float(st.session_state["auto_fill"][idx])

        amount = st.slider("Transaction Amount (₹)", 0.0, 5000.0, default_val)
        features.append(amount)

    # ---------- PREDICT ----------
    if st.button("🚀 Analyze Transaction"):

        input_data = np.array(features).reshape(1, -1)

        input_data_scaled = scaler.transform(input_data)

        prediction = model.predict(input_data_scaled)
        prob = model.predict_proba(input_data_scaled)[0][1]

        st.markdown("## 📊 Result")

        if prediction[0] == 1:
            st.error("🚨 Fraud Detected")
        else:
            st.success("✅ Normal Transaction")

        st.progress(int(prob * 100))
        st.write(f"Fraud Probability: **{round(prob*100,2)}%**")
        if prob > 0.7:
            st.error("High Risk Transaction 🚨")
        elif prob > 0.4:
            st.warning("Medium Risk ⚠️")
        else:
            st.success("Low Risk ✅")
