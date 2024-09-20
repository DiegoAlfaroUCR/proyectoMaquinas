import streamlit as st
from PIL import Image
from funcGenerales import getInputsGenerales, getInputsEspecificos


# Header

st.title(':blue[Calculadora de circuitos magnéticos] ')
st.subheader("Diego Alfaro Segura (C20259)," +
             " Ismael José Alvarado Pérez (C20366). Grupo 1")

imagen_local = Image.open('img/imagen.png')
st.image(imagen_local, caption='Diagrama del circuito magnético',
         use_column_width=True)

# Inputs generales.
parametrosGenerales = getInputsGenerales()

# Inputs específicos.
parametrosEspecificos = getInputsEspecificos()

if parametrosGenerales['datosMu'][1] != 'error':
    st.write(parametrosGenerales)
    st.write(parametrosEspecificos)
