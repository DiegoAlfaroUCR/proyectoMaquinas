import streamlit as st
import pandas as pd

# Title of the app
st.title('Interactive Table Input and Calculation')

# Instructions for the user
st.write('Enter values into the table below and click "Submit" to calculate the sum of each column.')

# Create an empty DataFrame with columns
columns = st.text_input('Enter column names (comma-separated)', 'Column 1, Column 2, Column 3')
column_names = [col.strip() for col in columns.split(',')]

# Create a DataFrame with the specified columns
df = pd.DataFrame(columns=column_names)

# Display a form for user to input table data
with st.form(key='table_form'):
    # Create an input field for each row
    num_rows = st.number_input('Number of rows', min_value=1, value=3)
    
    # Input for each cell in the table
    data = []
    for i in range(num_rows):
        row_data = st.text_input(f'Row {i+1} (comma-separated)', '')
        if row_data:
            data.append([float(value.strip()) for value in row_data.split(',')])
    
    # Convert the input data into a DataFrame
    if data:
        df = pd.DataFrame(data, columns=column_names)

    # Submit button to calculate sums
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    # Display the table
    st.write('Your table:')
    st.dataframe(df)
    
    # Calculate and display the sum of each column
    column_sums = df.sum()
    st.write('Sum of each column:')
    st.write(column_sums)
