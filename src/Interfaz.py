import streamlit as st
import os
import signal
import time
from PIL import Image
from funcGenerales import (getInputsGenerales,
                           getInputsEspecificos,
                           mostrarResultado,
                           calculadora)

# Limpieza de cache y establecer si se cierra
st.cache_data.clear()
st.cache_resource.clear()

if "close_clicked" not in st.session_state:
    st.session_state.close_clicked = False

# Header

st.title(':blue[Calculadora de circuitos magnéticos] ')
st.subheader("Diego Alfaro Segura (C20259)," +
             " Ismael José Alvarado Pérez (C20366). Grupo 01")


if st.sidebar.button("Cerrar calculadora."):
    st.session_state.close_clicked = True

if st.session_state.close_clicked:
    st.write('Ya cerró el proceso en la terminal, ' +
             'porfavor cierre esta ventana. Gracias!')
    time.sleep(0.01)
else:
    imagen_local = Image.open('img/imagen.png')
    st.image(imagen_local, caption='Diagrama del circuito magnético',
             use_column_width=True)

    # Inputs generales.
    parametrosGenerales = getInputsGenerales()

    # Inputs específicos.
    parametrosEspecificos = getInputsEspecificos()
    # Botón de calcular
    resultados = calculadora(parametrosGenerales, parametrosEspecificos)
    if parametrosGenerales['datosMu'][1] != 'error':
        # mostrarResultado(parametrosEspecificos)
        st.write(parametrosGenerales)
        st.write(parametrosEspecificos)

if st.session_state.close_clicked:
    os.kill(os.getppid(), signal.SIGINT)
