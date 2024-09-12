import streamlit as st

# Create columns to place widgets side-by-side
col1, col2 = st.columns([3, 1])  # Adjust the ratio to control the width of columns

with col1:
    # Create a number input field
    number = st.number_input("Enter a number", value=1.0, format="%.2f")

with col2:
    # Create a select box for choosing units
    units = st.selectbox(
        "Unidades",
        ["meters", "kilometers", "miles", "feet"],
        index=0  # Optionally, set the default selection
    )

# Display the entered number and selected unit
st.write(f"You entered: {number} {units}")
