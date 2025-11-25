import streamlit as st
import requests
from groq import Groq

# Lock 
st.title("🔐 Secure Currency Converter")

password = st.text_input("Enter Password:", type="password")

# Apna password yahan set karein
correct_password = st.secrets["APP_PASSWORD"]

if password != correct_password:
    st.warning("Please enter the correct password to access the converter.")
    st.stop()   # App yahan ruk jayegi agar password wrong ho

st.success("Password Correct! Access Granted ✔️")


# Start Currency Converter Here
st.title("💱 Live Currency Converter")

amount = st.number_input("Enter The Amount In PKR" , min_value = 1)

target_currency = st.selectbox("Convert To: " , ["USD" , "EUR" , "GBP" , "JPY" , "AED" , "AUD" , "CAD" , "CHF" , "CNY" , "NZD" , "SGD" ,   "INR" , "KRW" , "HKD" , "MXN" , "BRL" , "ZAR" , "RUB" , "TRY" , "SEK" , "NOK"])

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/PKR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][target_currency]
        converted_value = rate * amount
        st.success(f"{amount} PKR = {converted_value:.2f} {target_currency}")

    else: 
        st.error("Failed To Fetch Conversion Rate")

# AI ChatBot
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ==== Sidebar Chatbot ====
st.sidebar.subheader("🧠 AI Chatbot (Animated Robot)")

# User input
user_msg = st.sidebar.text_input("Ask something…")

if st.sidebar.button("Send"):
    if user_msg.strip():
        # Single-turn chat (no history)
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": user_msg}]
        )

        bot_reply = response.choices[0].message.content

        # Display user and bot messages
        st.sidebar.write("🧑‍💻 You: " + user_msg)
        st.sidebar.write("🤖 Bot: " + bot_reply)



