import streamlit as st
from PIL import Image
from funcGenerales import getInputsGenerales, inputVector


# Header

st.title(':blue[Calculadora de circuitos magnéticos] ')
st.subheader("Diego Alfaro Segura (C20259)," +
             " Ismael José Alvarado Pérez (C20366). Grupo 1")

imagen_local = Image.open('img/imagen.png')
st.image(imagen_local, caption='Diagrama del circuito magnético',
         use_column_width=True)

# Inputs generales.
parametrosGenerales = getInputsGenerales()

# Ingreso de opciones e inputs específicos.
listaVariables = ['Flujos magnéticos 1 y 2', 'Corriente 1', 'Corriente 2']
variableBuscada = st.selectbox('Escoja la variable a calcular', listaVariables)

if variableBuscada == 'Flujos magnéticos 1 y 2':
    flujoEntrehierro = inputVector('Flujo de entrehierro', 'weber')
elif variableBuscada == 'Corriente 1':
    corriente2 = inputVector('Corriente 2', 'A')
else:
    corriente1 = inputVector('Corriente 1', 'A')
