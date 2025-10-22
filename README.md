# Retail Insights Chatbot

**Author:** Chandan Kumar | 

## Overview
An LLM-powered chatbot that answers natural language questions about retail sales using OpenAI GPT and a small CSV dataset. Includes a Streamlit demo app.

## Files
- `Retail_Insights_Chatbot.ipynb` - Notebook with setup and examples
- `app_retail_chatbot.py` - Streamlit demo app
- `retail_sales_small.csv` - Sample dataset

## Requirements
```
pip install openai langchain duckdb pandas streamlit
```

## Run Demo
1. Set environment variable `OPENAI_API_KEY`
2. Run: `streamlit run app_retail_chatbot.py`

## Notes
- Uses OpenAI GPT family models. Replace `model` parameter as needed.
- Be mindful of API costs and rate limits.
