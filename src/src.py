import streamlit as st
from PIL import Image


st.title('Calculadora de circuitos magnéticos.')
st.subheader("Diego Alfaro Segura (C20259), Ismael José Alvarado Pérez (C20366). Grupo 1")


st.write('Main de prueba.')

image_local = Image.open('img/imagen.png')  # Replace with your image path
st.image(image_local, caption='Local Image', use_column_width=True)
