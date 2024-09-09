import streamlit as st
from PIL import Image

# Title of the app
st.title('Image Display Example')

# Display an image from a local file
st.write('### Image from Local File')
image_local = Image.open('imagen.png')  # Replace with your image path
st.image(image_local, caption='Local Image', use_column_width=True)

# Display an image from a URL
# st.write('### Image from URL')
# image_url = 'https://www.example.com/path_to_your_image.jpg'  # Replace with your image URL
# st.image(image_url, caption='URL Image', use_column_width=True)
