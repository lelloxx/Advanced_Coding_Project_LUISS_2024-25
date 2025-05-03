# Import necessary libraries
import streamlit as st
import pandas as pd

# Generate an Interface for the user to upload a CSV file or enter data manually
st.title("Credit Score Prediction")
st.write("Upload your CSV file or enter data manually to predict your credit score.")

columns = pd.read_csv('Dataset\model_credit_card_data.csv').columns.tolist()
loans_columns = [
    'Not specified',
    'Mortgage loan',
    'Payday loan',
    'Home equity loan',
    'Credit-builder loan',
    'Student loan',
    'Debt consolidation loan',
    'Personal loan',
    'Auto loan'
]
columns = [col for col in columns if col not in loans_columns]

st.write("Make sure your data has the following information:")
for col in columns: # Exclude 'Credit_Score' and the Loans columns from the list of columns to display
    if col == "Credit_Score" or col in loans_columns:
        continue
    st.write(f"- {str(col).replace('_', ' ').capitalize()}")

st.write("If you prfefer to upload data manually, you can do so in the next section.")
for col in columns:
    st.text_input(f"Enter {col}:")
    st.write("")


