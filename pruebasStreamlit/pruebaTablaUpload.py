import streamlit as st
import pandas as pd

# Title of the app
st.title('Excel File Upload and Column Sum Calculation')

# Instructions for the user
st.write('Upload an Excel file below and click "Submit" to view the table and calculate the sum of each column.')

# File uploader widget
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file:
    # Read the uploaded Excel file into a DataFrame
    df = pd.read_excel(uploaded_file)
    
    # Display the dataframe
    st.write('Uploaded Data:')
    st.dataframe(df)
    
    # Calculate and display the sum of each column
    if not df.empty:
        # Handle numerical columns only
        numerical_columns = df.select_dtypes(include=['number']).columns
        column_sums = df[numerical_columns].sum()
        
        st.write('Sum of each column:')
        st.write(column_sums)
else:
    st.write('Please upload an Excel file to proceed.')
