# app.py

import streamlit as st
import pandas as pd

st.set_page_config(page_title="PubMed Abstract Summarizer", layout="wide")
st.title("🧠 PubMed Abstract Summarizer")

# Load the summaries file
df = pd.read_csv("summaries.csv")

search_term = st.sidebar.text_input("🔍 Search keyword in summaries")

if search_term:
    results = df[df["Summary"].str.contains(search_term, case=False)]
else:
    results = df

st.write(f"### Showing {len(results)} summaries")

for _, row in results.iterrows():
    with st.expander(f"PMID {row['PMID']}"):
        st.markdown(f"**🔬 Summary:** {row['Summary']}")
        if st.checkbox("Show original abstract", key=row['PMID']):
            st.text(row['Abstract'])
