# Funciones de uso general

import streamlit as st


def getInputsGenerales():
    st.write('Edite los parámetros generales del circuito magnético:')
    col1, col2 = st.columns(2)

    with col1:
        vueltas1 = st.number_input("Número de vueltas de bobina 1",
                                   min_value=1, step=1)
        vueltas2 = st.number_input("Número de vueltas de bobina 2",
                                   min_value=1, step=1)
        SL = st.number_input("Área transversal SL (m)", min_value=0.0,
                             format="%.3f")
        SC = st.number_input("Área transversal SC (m)", min_value=0.0,
                             format="%.3f")

    with col2:
        A = st.number_input("Alto del circuito A (m)", min_value=0.0,
                            format="%.3f")
        L1 = st.number_input("Longitud L1 (m)", min_value=0.0,
                             format="%.3f")
        L2 = st.number_input("Longitud L2 (m)", min_value=0.0,
                             format="%.3f")
        L3 = st.number_input("Altura media del entrehierro L3 (m)",
                             min_value=0.0, format="%.3f")

    stringFP = "Factor de apilado de las láminas del núcleo"
    factorApilado = st.number_input(stringFP,
                                    min_value=0.0,
                                    max_value=1.0,
                                    format="%.3f")

    diccGeneral = {
        'vueltas1': vueltas1,
        'vueltas2': vueltas2,
        'factorApilado': factorApilado,
        'SL': SL,
        'SC': SC,
        'A': A,
        'L1': L1,
        'L2': L2,
        'L3': L3
    }

    return diccGeneral


def inputVector(nombreVariable, unidades):
    st.write(f'Ingrese los datos de {nombreVariable}')

    if nombreVariable == 'Flujo de entrehierro':
        opcionesSentido = {'Hacia arriba': 1, 'Hacia abajo': -1}
    else:
        opcionesSentido = {'Hacia la derecha': 1, 'Hacia la izquierda': -1}

    # Create columns to place widgets side-by-side
    # Adjust the ratio to control the width of columns
    col1, col2 = st.columns([3, 1])

    with col1:
        # Create a number input field
        magnitud = st.number_input(f"Magnitud ({unidades})",
                                   min_value=0.0, format="%.2f")

    with col2:
        # Create a select box for choosing units
        sentido = st.selectbox(
            "Sentido",
            list(opcionesSentido.keys()),
            index=0  # Optionally, set the default selection
        )
    diccCorriente = {'magnitud': magnitud, 'sentido': opcionesSentido[sentido]}
    return diccCorriente
