import streamlit as st
from PIL import Image
from funcGenerales import (getInputsGenerales,
                           getInputsEspecificos,
                           mostrarResultado)

st.cache_data.clear()
st.cache_resource.clear()

# Header

st.title(':blue[Calculadora de circuitos magnéticos] ')
st.subheader("Diego Alfaro Segura (C20259)," +
             " Ismael José Alvarado Pérez (C20366). Grupo 01")

imagen_local = Image.open('img/imagen.png')
st.image(imagen_local, caption='Diagrama del circuito magnético',
         use_column_width=True)

# Inputs generales.
parametrosGenerales = getInputsGenerales()

# Inputs específicos.
parametrosEspecificos = getInputsEspecificos()

if parametrosGenerales['datosMu'][1] != 'error':
    mostrarResultado()
    st.write(parametrosGenerales)
    st.write(parametrosEspecificos)
