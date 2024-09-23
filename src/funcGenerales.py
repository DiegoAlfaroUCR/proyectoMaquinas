# Funciones de uso general

import streamlit as st
import pandas as pd
import numpy as np

minNoCero = 0.0000000000000001


def getInputsGenerales():
    st.write('Edite los parámetros generales del circuito magnético:')

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
        #cambie el nombre de L3 al LE, que lo otro es sólo la altura a la que empieza el entre hierro
        LE = st.number_input("Altura media del entrehierro LE (m)",
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
    #Datos del flujo en el entrehierro
    st.write(f'Ingrese los datos de flujo en el entrehierro deseado')
    col1, col2 = st.columns(2)
    with col1:
        flujoEntreHierro = st.number_input("Flujo [Wb]",
                                   min_value=0.0, format="%.5f")
    with col2:
        # Create a select box for choosing units
        sentidoW = st.selectbox(
            "Sentido",
            {'Hacia arriba': 1, 'Hacia abajo': -1},
            index=0  # Optionally, set the default selection
            )
    parametrosGenerales = {
        'vueltas1': vueltas1,
        'vueltas2': vueltas2,
        'factorApilado': factorApilado,
        'SL': SL,
        'SC': SC,
        'A': A,
        'L1': L1,
        'L2': L2,
        'LE': LE,
        'datosMu': datosMu,
        'flujoEntreHierro' : flujoEntreHierro,
        'sentidoEntreHierro': sentidoW
    }

    return parametrosGenerales


def getInputsEspecificos():
    listaVariables = ['Corriente 1', 'Corriente 2']
    variableBuscada = st.selectbox('Escoja la variable a calcular',
                                   listaVariables)

    if variableBuscada == 'Corriente 1':
        [nombreVariable, unidades] = ['Corriente 2', 'A']
    else:
        [nombreVariable, unidades] = ['Corriente 1', 'A']

    st.write(f'Ingrese los datos de {nombreVariable}')
    
    
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
        'sentido': opcionesSentido[sentido]
        }
    return parametrosEspecificos


def tablaMu():
    # Default values to be shown in the table
    default_data = {
        'B (T)': [0.02, 0.2],
        'H (Av/m)': [20, 40]
    }

    # Check if 'df' is in session state;
    # if not, initialize it with default data
    if 'df' not in st.session_state:
        st.session_state.df = pd.DataFrame(default_data)

    # Get the number of rows for the DataFrame from user input
    num_rows = st.number_input("Numero de filas", min_value=2,
                               max_value=30, value=len(st.session_state.df))

    # Adjust the number of rows in the DataFrame based on user input
    if num_rows != len(st.session_state.df):
        # Add or remove rows while keeping the data intact
        if num_rows > len(st.session_state.df):
            # Create new rows but remove all-NA columns
            # to avoid the FutureWarning
            additional_rows = pd.DataFrame(
                index=range(len(st.session_state.df), num_rows),
                columns=st.session_state.df.columns)
            additional_rows = additional_rows.dropna(how='all', axis=1)
            # Exclude all-NA columns
            st.session_state.df = pd.concat(
                [st.session_state.df, additional_rows], ignore_index=True)
        else:
            # Remove excess rows
            st.session_state.df = st.session_state.df.iloc[:num_rows]

    # Display editable table
    edited_df = st.data_editor(st.session_state.df, use_container_width=True)

    # Update session state with the edited DataFrame
    st.session_state.df = edited_df

    # Error checking for NaN and negative values
    if st.session_state.df.isnull().values.any():
        st.error("ERROR: La tabla contiene valores vacíos (NaN). " +
                 "Por favor, complete todos los campos.")
        return [st.session_state.df, 'error']

    if (st.session_state.df < 0).any().any():
        st.error("ERROR: La tabla contiene valores negativos." +
                 "Por favor, use solo valores positivos.")
        return [st.session_state.df, 'error']


    return [st.session_state.df, 'dataFrame']


def ecuacionMu():
    st.write('Ingrese las variables \'a\' y \'b\' ' +
             'correspondientes a la ecuación: B = aH/(1+bH)')
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("a: ", min_value=minNoCero,
                            value=1.00, format="%.5f")
    with col2:
        b = st.number_input("b: ", min_value=minNoCero,
                            value=1.00)
    dictMu = {'a': a, 'b': b}
    return [dictMu, 'ecuacion']

def calculadora():
    #se tiene la matriz principal
    # se debe hallar la fmm del medio
    # entrehierro+ nucleo
    #por el momento nada tiene valor real

    tipo=1
    a=1
    b=1

    flujoE=1
    LE=1
    mu=4*np.pi*10^(-7)
    SC=1
    A=1
    factorApilado=1
    I1=None
    I2=None

    H3=sacarH(flujoE,factorApilado,SC, tipo,a,b)
    
    Fmmc= flujoE*LE/(mu*SC)+ H3*A
    if I1 is not None:

        pass
    else:
        pass
    
    


    pass
def sacarH(flujoE,factorApilado,SC, tipo,a=1,b=1):
    #Saco B3
    B3=flujoE/(factorApilado*SC)
    if tipo=='ecuacion':
        if (a-b*B3)==0:
            H3=1
        else:
            H3= B3/(a-b*B3)
    else:
        #Hacer lo de interpolación acá
        pass


    return H3
