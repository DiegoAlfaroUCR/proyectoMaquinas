import streamlit as st

# Title of the app
st.title('Dynamic Input Options Based on Selectbox')

# Define the categories and corresponding options
categories = {
    'Select Category': [],
    'Fruits': ['Apple', 'Banana', 'Orange'],
    'Animals': ['Dog', 'Cat', 'Elephant'],
    'Colors': ['Red', 'Green', 'Blue']
}

# Create a selectbox for choosing the category
category = st.selectbox('Choose a category', list(categories.keys()))

# Display different input options based on the selected category
if category in categories:
    options = categories[category]
    
    # Check if options are available
    if options:
        st.write(f'You selected the category: {category}')
        selected_option = st.selectbox('Choose an option', options)
        
        # Perform some action based on the selected option
        st.write(f'You selected: {selected_option}')
        
        # Example of additional input based on selection
        if category == 'Fruits':
            quantity = st.number_input('How many fruits?', min_value=1, max_value=100)
            st.write(f'Total fruits: {quantity}')
        elif category == 'Animals':
            animal_sound = st.text_input('Enter the sound this animal makes', 'Roar')
            st.write(f'The sound of a {selected_option} is {animal_sound}')
        elif category == 'Colors':
            hex_code = st.color_picker('Pick a color')
            st.write(f'You picked color: {hex_code}')
    else:
        st.write('No options available for this category.')
else:
    st.write('Please select a valid category.')
