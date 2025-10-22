import streamlit as st
import pandas as pd
import os
from typing import Any, Dict
from openai import OpenAI

st.set_page_config(page_title="Retail Insights Chatbot", layout="wide")
st.title("Retail Insights Chatbot (GPT)")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('retail_sales_small.csv', parse_dates=['InvoiceDate'])
    return df

df = load_data()

st.sidebar.header("Data Filters")
store = st.sidebar.selectbox("StoreID", options=sorted(df['StoreID'].unique()))
sku = st.sidebar.selectbox("SKU", options=sorted(df['SKU'].unique()))

st.write("Showing sample rows for selected Store & SKU")
st.dataframe(df[(df['StoreID']==store) & (df['SKU']==sku)].head(10))

st.markdown("---")
user_query = st.text_input("Ask a question about sales, e.g., 'Total sales last month for SKU_A'")

if st.button("Ask GPT") and user_query:
    openai_key = os.getenv('OPENAI_API_KEY')
    if not openai_key:
        st.error("Set OPENAI_API_KEY in environment to run GPT queries.")
    else:
        client = OpenAI(api_key=openai_key)
        # Build context from data - for safety keep a small stat summary
        subset = df[(df['StoreID']==store) & (df['SKU']==sku)]
        total_sales = int(subset['Sales'].sum())
        last_30 = int(subset[subset['InvoiceDate'] >= subset['InvoiceDate'].max() - pd.Timedelta(days=30)]['Sales'].sum())
        context = f"Store {store}, SKU {sku} total_sales={total_sales}, last_30_days_sales={last_30}."
        prompt = f"""You are an assistant for retail analytics. Use the context and answer query.
Context: {context}
Question: {user_query}
Provide a concise answer and if possible give a short pandas code snippet to compute it."""
        res = client.responses.create(model="gpt-4o-mini", input=prompt)
        st.markdown("**GPT Answer:**")
        st.write(res.output_text)
