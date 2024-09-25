import streamlit as st
import os
import signal
import time
import keyboard
from PIL import Image
from funcGenerales import (getInputsGenerales,
                           getInputsEspecificos,
                           mostrarResultado,
                           calculadora)

# Limpieza de cache y establecer si se cierra
st.cache_data.clear()
st.cache_resource.clear()

# Header

st.title(':blue[Calculadora de circuitos magnéticos] ')
st.subheader("Diego Alfaro Segura (C20259)," +
             " Ismael José Alvarado Pérez (C20366). Grupo 01")

st.sidebar.write('Para cerrar la calculadora porfavor usar este botón, ' +
                 'no cerrar la pestaña pues tendrá que cerrar la terminal' +
                 ' con CTRL + C, y en windows podría tardar unos segundos!')
if st.sidebar.button("Cerrar calculadora."):
    time.sleep(0.0005)
    keyboard.press_and_release('ctrl+w')
    os.kill(os.getppid(), signal.SIGINT)
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
