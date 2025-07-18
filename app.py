import streamlit as st
import pandas as pd

# App Title
st.title("PubMed Abstract Summarizer")
st.write("🔍 Search and summarize biomedical abstracts by PubMed ID")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your summaries.csv file", type=["csv"])

if uploaded_file:
    # Load the data
    df = pd.read_csv(uploaded_file)

    # User input for PubMed ID search
    pubmed_id = st.text_input("Enter PubMed ID")

    if pubmed_id:
        result = df[df['ID'].astype(str).str.strip() == pubmed_id.strip()]
        
        if not result.empty:
            for _, row in result.iterrows():
                st.subheader("🧾 Original Abstract")
                st.write(row['BG'])

                st.subheader("🧠 AI Summary")
                st.success(row['Summary'])
        else:
            st.warning("❌ No abstract found for this PubMed ID.")

    # Optional: display the full dataset
    if st.checkbox("Show full dataset"):
        st.dataframe(df)

# Footer
st.markdown("---")
st.markdown("Built by Samuel Johnson | 3MTT Kaduna | Data Analytics Track")
