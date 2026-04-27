import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from azure_nlp import analyze_texts
 
st.set_page_config(page_title="Social Media Sentiment Analyzer")
 
st.title("Social Media Sentiment Analyzer (Azure AI)")
 
option = st.radio("Choose input type:", ["Manual Text", "CSV Upload"])
 
texts = []
 
if option == "Manual Text":
    user_input = st.text_area("Enter posts (one per line)")
    if user_input:
        texts = user_input.split("\n")
else:
    file = st.file_uploader("Upload CSV with 'text' column", type=["csv"])
    if file:
        df = pd.read_csv(file)
        texts = df["text"].tolist()
 
if st.button("Analyze Sentiment") and texts:
    results = analyze_texts(texts)
    df = pd.DataFrame(results)
 
    st.subheader("Results")
    st.dataframe(df)
 
    st.subheader("Sentiment Distribution")
    sentiment_counts = df["sentiment"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%")
    st.pyplot(fig)
 
    st.subheader("Language Distribution")
    lang_counts = df["language"].value_counts()
    fig2, ax2 = plt.subplots()
    ax2.bar(lang_counts.index, lang_counts.values)
    st.pyplot(fig2)
