import streamlit as st
from rag_chain import load_qa_chain

# --- Page Config ---
st.set_page_config(page_title="Alltius RAG Bot", layout="wide")
st.markdown("<h1 style='text-align: center;'>🤖 Alltius.ai Support Chatbot</h1>", unsafe_allow_html=True)

# --- Load QA Chain ---
qa = load_qa_chain()

# --- Category Dropdown ---
st.markdown("### 📂 Choose a Help Category:")
categories = [
    "General",
    "Trading & Investment",
    "Account & KYC",
    "Payments & Withdrawals",
    "IPO & Mutual Funds",
    "Insurance"
]
selected_category = st.selectbox("", categories, index=0)

# --- Question Input ---
st.markdown("### 💬 Ask Your Question:")
query = st.text_input("", placeholder="Type your support question here...")

# --- Submit Button ---
submit = st.button("🔍 Submit")

if submit and query:
    full_query = f"Category: {selected_category}\nQuestion: {query}"

    with st.spinner("Thinking..."):
        result = qa.run(full_query)

    if "I don't know" in result or len(result.strip()) == 0:
        st.warning("🤔 Sorry, I don't know the answer based on the documents.")
    else:
        st.success(result)
elif submit and not query:
    st.warning("❗ Please enter a question before clicking Submit.")
