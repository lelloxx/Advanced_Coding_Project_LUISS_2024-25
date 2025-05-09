# Import necessary libraries
import streamlit as st
import pandas as pd
import joblib

# Load model and expected input columns
model = joblib.load("Outputs/decision_tree_model_over.pkl")
expected_columns = joblib.load("expected_columns.pkl")
expected_columns = [col for col in expected_columns if 'City' not in col]

# Streamlit App Title
st.set_page_config(page_title="Credit Score Predictor", layout="centered")
st.title("📊 Credit Score Prediction App")
st.markdown("Upload your CSV file to predict credit scores using a trained decision tree model.")

# Sidebar with Required Columns
st.sidebar.title("ℹ️ Required Input Columns")
st.sidebar.markdown("Make sure your data includes the following features:")
columns = pd.read_csv('Dataset/model_credit_card_data.csv').columns.tolist()
loans_columns = [
    'Not specified', 'Mortgage loan', 'Payday loan', 'Home equity loan',
    'Credit-builder loan', 'Student loan', 'Debt consolidation loan',
    'Personal loan', 'Auto loan'
]
columns = [col for col in columns if col not in loans_columns and col != "Credit_Score"]
for col in columns:
    st.sidebar.write(f"✅ {str(col).replace('_', ' ').capitalize()}")

# File upload
with st.expander("📁 Upload CSV File", expanded=True):
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    # Drop City column if exists
    if 'City' in data.columns:
        data = data.drop(columns=['City'])

    # Encode categorical variables
    data = pd.get_dummies(data)

    # Align columns to model input
    data = data.reindex(columns=expected_columns, fill_value=0)

    # Display preview
    with st.expander("🔍 Preview Processed Data"):
        st.dataframe(data.head())

    # Run prediction
    try:
        prediction = model.predict(data)
        results_df = pd.DataFrame(prediction, columns=["Predicted Credit Score"])

        st.subheader("📈 Prediction Results")
        st.dataframe(results_df)

        # Optional: Download predictions
        csv = results_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Predictions as CSV", data=csv, file_name="predictions.csv", mime="text/csv")

    except Exception as e:
        st.error(f"⚠️ Error during prediction: {e}")

else:
    st.info("⬆️ Please upload a CSV file to begin.")




