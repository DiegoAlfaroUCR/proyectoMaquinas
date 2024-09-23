import streamlit as st
import pandas as pd

# Function to create an initial DataFrame with the specified number of columns
def create_initial_df(num_columns):
    columns = [f'Column {i+1}' for i in range(num_columns)]
    data = {'Row 1': [''] * num_columns, 'Row 2': [''] * num_columns}
    df = pd.DataFrame(data, index=columns).T
    return df

# Streamlit app
def main():
    st.title("Editable Table with Adjustable Columns")

    # Sidebar for adjusting the number of columns
    num_columns = st.sidebar.slider('Number of Columns', min_value=1, max_value=20, value=5)

    # Create the DataFrame based on the selected number of columns
    df = create_initial_df(num_columns)

    # Display the DataFrame as editable text inputs
    st.write("Edit the table below:")
    edited_df = pd.DataFrame(index=df.index, columns=df.columns)

    for i, row_name in enumerate(df.index):
        for j, col_name in enumerate(df.columns):
            edited_df.loc[row_name, col_name] = st.text_input(f"{row_name} - {col_name}", df.loc[row_name, col_name], key=f"{row_name}-{col_name}")

    # Display the updated DataFrame
    st.write("Updated DataFrame:")
    st.dataframe(edited_df)

if __name__ == "__main__":
    main()
