import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for the numbers
number1 = st.number_input("Enter the first number", value=0)
number2 = st.number_input("Enter the second number", value=0)

# Dropdown to select the operation
operation = st.selectbox("Select the operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform the calculation based on the selected operation
if operation == "Add":
    result = number1 + number2
elif operation == "Subtract":
    result = number1 - number2
elif operation == "Multiply":
    result = number1 * number2
elif operation == "Divide":
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Error: Division by zero"

# Display the result
st.write(f"The result of {operation.lower()}ing {number1} and {number2} is: {result}")
