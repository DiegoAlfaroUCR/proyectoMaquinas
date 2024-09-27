import streamlit as st
import os
import signal
import time
from pynput.keyboard import Controller, Key
from PIL import Image
from funcGenerales import (getInputsGenerales,
                           getInputsEspecificos,
                           mostrarResultado,
                           calculadora)

# Limpieza de cache y establecer si se cierra quitar ventana
st.cache_data.clear()
st.cache_resource.clear()

keyboard = Controller()

# Header

st.title(':blue[Calculadora de circuitos magnéticos] ')
st.subheader("Diego Alfaro Segura (C20259)," +
             " Ismael José Alvarado Pérez (C20366). Grupo 01")

st.sidebar.write(':blue[Instrucciones de uso: ]\n' +
                 'Ingrese los datos pedidos deacuerdo a las unidades ' +
                 'indicadas y a las magnitudes que corresponden en el' +
                 ' diagrama. Finalmente, presione \'Calcular\' \n'
                 )
st.sidebar.write('El circuito asume que las corrientes hacia la derecha en las bobinas generan flujo para arriba.\n'+
                 'Asímismo, corrientes para la izquierda generan flujo hacia bajo.')

st.sidebar.write('Para cerrar la calculadora porfavor usar este botón, ' +
                 'no cerrar la pestaña pues tendrá que cerrar la terminal' +
                 ' con CTRL + C ¡En windows podría tardar unos segundos!')
if st.sidebar.button("Cerrar calculadora."):
    time.sleep(0.0005)
    with keyboard.pressed(Key.ctrl):  # This will hold down the 'ctrl' key
        keyboard.press('w')            # Press 'w'
        time.sleep(0.1)
        keyboard.release('w')          # Release 'w'
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
        #st.write(parametrosGenerales)
        #st.write(parametrosEspecificos)
        #st.write(resultados)
        if st.button('Calcular'):
            resultados = calculadora(parametrosGenerales,
                                        parametrosEspecificos)
            mostrarResultado(resultados, parametrosEspecificos)
    

