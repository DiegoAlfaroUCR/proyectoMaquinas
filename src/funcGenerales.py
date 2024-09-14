# Funciones de uso general

import streamlit as st
import pandas as pd


def getInputsGenerales():
    st.write('Edite los parámetros generales del circuito magnético:')

    minNoCero = 0.0000000000000001

    col1, col2 = st.columns(2)
    with col1:
        vueltas1 = st.number_input("Número de vueltas de bobina 1",
                                   min_value=1, step=1)
        vueltas2 = st.number_input("Número de vueltas de bobina 2",
                                   min_value=1, step=1)
        SL = st.number_input("Área transversal SL (m)", min_value=minNoCero,
                             value=1.00, format="%.5f")
        SC = st.number_input("Área transversal SC (m)", min_value=minNoCero,
                             value=1.00, format="%.5f")

    with col2:
        A = st.number_input("Alto del circuito A (m)", min_value=minNoCero,
                            value=1.00, format="%.5f")
        L1 = st.number_input("Longitud L1 (m)", min_value=minNoCero,
                             value=1.00, format="%.5f")
        L2 = st.number_input("Longitud L2 (m)", min_value=minNoCero,
                             value=1.00, format="%.5f")
        L3 = st.number_input("Altura media del entrehierro L3 (m)",
                             value=1.00, min_value=0.0, format="%.5f")

    stringFP = "Factor de apilado de las láminas del núcleo"
    factorApilado = st.number_input(stringFP,
                                    min_value=0.0,
                                    max_value=1.0,
                                    format="%.5f")

    seleccionMu = st.selectbox('Escoja una forma de ingresar Mu',
                               ['Por tabla', 'Por ecuación'])

    if seleccionMu == 'Por tabla':
        datosMu = tablaMu()
    else:
        datosMu = ecuacionMu()

    parametrosGenerales = {
        'vueltas1': vueltas1,
        'vueltas2': vueltas2,
        'factorApilado': factorApilado,
        'SL': SL,
        'SC': SC,
        'A': A,
        'L1': L1,
        'L2': L2,
        'L3': L3,
        'datosMu': datosMu
    }

    return parametrosGenerales


def getInputsEspecificos():
    listaVariables = ['Flujos magnéticos 1 y 2', 'Corriente 1', 'Corriente 2']
    variableBuscada = st.selectbox('Escoja la variable a calcular',
                                   listaVariables)

    if variableBuscada == 'Flujos magnéticos 1 y 2':
        [nombreVariable, unidades] = ['Flujo de entrehierro', 'weber']
    elif variableBuscada == 'Corriente 1':
        [nombreVariable, unidades] = ['Corriente 2', 'A']
    else:
        [nombreVariable, unidades] = ['Corriente 1', 'A']

    st.write(f'Ingrese los datos de {nombreVariable}')

    if nombreVariable == 'Flujo de entrehierro':
        opcionesSentido = {'Hacia arriba': 1, 'Hacia abajo': -1}
    else:
        opcionesSentido = {'Hacia la derecha': 1, 'Hacia la izquierda': -1}

    # Create columns to place widgets side-by-side
    # Adjust the ratio to control the width of columns
    col1, col2 = st.columns([2, 1])

    with col1:
        # Create a number input field
        magnitud = st.number_input(f"Magnitud ({unidades})",
                                   min_value=0.0, format="%.5f")

    with col2:
        # Create a select box for choosing units
        sentido = st.selectbox(
            "Sentido",
            list(opcionesSentido.keys()),
            index=0  # Optionally, set the default selection
        )

    parametrosEspecificos = {
        'variableBuscada': variableBuscada,
        'variableDada': nombreVariable,
        'magnitud': magnitud,
        'sentido': opcionesSentido[sentido]}
    return parametrosEspecificos


def tablaMu():
    # Create a session state to store the current data
    if 'df' not in st.session_state:
        st.session_state.df = pd.DataFrame()

    # Set up DataFrame for manual input
    num_rows = 2
    num_cols = st.number_input("Numero de columnas",
                               min_value=3, max_value=30,
                               value=3)

    # Initialize empty DataFrame or update with session state
    if st.session_state.df.empty:
        st.session_state.df = pd.DataFrame(
            columns=[f"Columna {i+1}" for i in range(num_cols)],
            index=range(num_rows))
    else:
        st.session_state.df = pd.DataFrame(
            columns=[f"Columna {i+1}" for i in range(num_cols)],
            index=range(num_rows))

    # Show editable table
    st.session_state.df = st.data_editor(
        st.session_state.df,
        use_container_width=True)

    if st.session_state.df.isnull().values.any():
        st.error("La tabla contiene valores vacíos (NaN). " +
                 "Por favor, complete todos los campos.")
        return 'error'

    return st.session_state.df


def ecuacionMu():
    st.write('No he diseñado lo de la ecuacion :p')
    return 0
