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
        # Cambie el nombre de L3 al LE,
        # que lo otro es sólo la altura a la que empieza el entre hierro
        LE = st.number_input("Altura media del entrehierro LE (m)",
                             value=1.00, min_value=0.0, format="%.5f")

    stringFP = "Factor de apilado de las láminas del núcleo"
    factorApilado = st.number_input(stringFP, value=1.00,
                                    min_value=minNoCero,
                                    max_value=1.0,
                                    format="%.5f")

    seleccionPorcentaje = st.selectbox('Indique porcentaje de deformación' +
                                       'del área en el entrehierro (%)',
                                       ['Automático', 'Porcentaje'])

    if seleccionPorcentaje == 'Porcentaje':
        porcentajeArea = st.number_input('Coloque el dato como un porcentaje',
                                         value=50.00,
                                         min_value=0.0,
                                         max_value=100.0,
                                         format="%.5f")
    else:
        porcentajeArea = 'automatico'

    seleccionMu = st.selectbox('Escoja una forma de ingresar Mu',
                               ['Por tabla', 'Por ecuación'])

    if seleccionMu == 'Por tabla':
        datosMu = tablaMu()
    else:
        datosMu = ecuacionMu()
    # Datos del flujo en el entrehierro
    st.write('Ingrese los datos de flujo en el entrehierro deseado')
    col1, col2 = st.columns(2)
    with col1:
        flujoEntreHierro = st.number_input("Flujo [Wb]",
                                           min_value=0.0, format="%.5f")
    with col2:
        # Create a select box for choosing units
        sentidoW = st.selectbox(
            "Sentido",
            {'Hacia arriba': -1, 'Hacia abajo': 1},
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
        'flujoEntreHierro': flujoEntreHierro,
        'sentidoEntreHierro': sentidoW,
        'porcentajeArea': porcentajeArea
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


def calculadora(generales, especificos):
    # Se tiene la matriz principal, se debe hallar la fmm del medio
    # entrehierro + nucleo. Por el momento nada tiene valor real

    # Valores de generales
    mu = 4*np.pi/(10**(7))
    vueltas1 = float(generales['vueltas1'])
    vueltas2 = float(generales['vueltas2'])
    factorApilado = float(generales['factorApilado'])
    if factorApilado == 0:
        factorApilado = 1
    SL = float(generales['SL'])
    SC = float(generales['SC'])
    A = float(generales['A'])
    L1 = float(generales['L1'])
    L2 = float(generales['L2'])
    LE = float(generales['LE'])
    datosMu = generales['datosMu']
    flujoEntreHierro = float(generales['flujoEntreHierro'])
    # sentidoW = generales['sentidoEntreHierro']
    porcentajeArea = generales['porcentajeArea']
    if porcentajeArea == 'automatico':
        AreaEntrehierro = (np.sqrt(SC)+LE)**2
    else:
        AreaEntrehierro = SC*(1+float(porcentajeArea)/100)

    """No he puesto como afecta la dirección"""
    # Valores especificos
    Iconocida = especificos['variableDada']
    magnitud = especificos['magnitud']
    sentido = especificos['sentido']
    if st.button("Calcular"):
        H3 = sacarH(flujoEntreHierro, SC, datosMu, factorApilado)
        # Sacar datos del centro
        Fmmcentro = flujoEntreHierro*LE/(mu*AreaEntrehierro) + H3*(A-LE)
        # x = flujoEntreHierro*LE/(mu*AreaEntrehierro)
        # print(x)
        # print(AreaEntrehierro)
        # print(mu)
        # print('Fmm')
        # print(Fmmcentro)
        # print(H3*(A-LE))
        # Identificar los datos conocidos
        corrienteConocida = magnitud
        if sentido == 'Hacia la izquierda':
            corrienteConocida = -magnitud
        if Iconocida == 'Corriente 1':
            Idesconocida = 'Corriente 2'
            Lconocido = A+2*L1
            Nconocido = vueltas1
            Ldesconocido = A+2*L2
            Ndesconocido = vueltas2

        else:
            Idesconocida = 'Corriente 1'
            Lconocido = A+2*L2
            Nconocido = vueltas2
            Ldesconocido = A+2*L1
            Ndesconocido = vueltas1

        # Sacar datos de la bobina con I conocido
        Hconocido = (Nconocido*corrienteConocida-Fmmcentro)/(Lconocido)
        # print('H1')
        # print(Hconocido)
        flujoconocido = sacarFlujo(Hconocido, SL, datosMu, factorApilado)

        # Sacar datos de la bobina con I desconocida
        flujoDesconocido = flujoEntreHierro-flujoconocido
        Hdesconocido = sacarH(flujoDesconocido, SL, datosMu, factorApilado)
        corrienteDesconocida = ((Fmmcentro+Hdesconocido*Ldesconocido)
                                / Ndesconocido)
        # print('Corriente calculada')
        # print(corrienteDesconocida)
        # print('flujo de bobina calculada')
        # print(flujoDesconocido)
        # print('flujo de bobina conocida')
        # print(flujoconocido)
        diccResultados = {Iconocida: flujoconocido,
                          Idesconocida: [corrienteDesconocida,
                                         flujoDesconocido]}
        return diccResultados


def sacarH(flujoE, SC, datosMu, factorApilado=1):
    # Saco B3 realmente
    datos = datosMu[0]
    B = flujoE/(factorApilado*SC)

    if datosMu[1] == 'ecuacion':
        a = datosMu[0]['a']
        b = datosMu[0]['b']
        if (a-b*B) == 0:
            H = 1
            st.write('Hay un problema con la fórmula')
        else:
            H = abs(B)/(a-b*abs(B))
    else:
        menorB = 0
        mayorB = 0
        menorH = 0
        mayorH = 0
        b_array = datos['B (T)'].to_numpy()
        h_array = datos['H (Av/m)'].to_numpy()
        b_array, h_array = bubble_sort(b_array, h_array)
        print(h_array)
        print(b_array)
        if B < b_array[0]:
            menorB = b_array[0]
            menorH = h_array[0]
            mayorB = b_array[1]
            mayorH = h_array[1]
        elif B > b_array[len(b_array)-1]:
            menorB = b_array[len(b_array)-2]
            menorH = h_array[len(b_array)-2]
            mayorB = b_array[len(b_array)-1]
            mayorH = h_array[len(b_array)-1]
        else:
            for i in range(len(b_array)):
                if b_array[i] < abs(B):
                    menorB = b_array[i]
                    menorH = h_array[i]

                if b_array[i] > abs(B):
                    mayorB = b_array[i]
                    mayorH = h_array[i]
                    break
        H = menorH + (B - menorB) * (mayorH - menorH) / (mayorB - menorB)
        print(menorB)
        print(mayorB)
    print(B)
    print(H)
    return H


def mostrarResultado(diccResultados, parametrosEspecificos):
    # De momento no tenemos el formato del resultado.
    st.header("Resultados del cálculo")
    corrienteResult = parametrosEspecificos['variableBuscada']
    if parametrosEspecificos['sentido'] == -1:
        sentido = 'Hacia la izquierda'
    else:
        sentido = 'Hacia la derecha'

    mensajeResultado = str(corrienteResult) + sentido

    """
    if resultados[peticion] < 0:
        corrienteResult = str(abs(float(resultados[peticion])))+' Hacia la izquierda'
    else:
        corrienteResult = str(abs(float(resultados[peticion])))+' Hacia la derecha'
    """
    st.metric("Corriente pedida (A)", mensajeResultado)


def bubble_sort(arr, otro):
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:

                # Swap elements if they are in the wrong order
                # swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                otro[i], otro[i + 1] = otro[i + 1], otro[i]
    return arr, otro


def sacarFlujo(H, SL, datosMu, factorApilado=1):
    # Saco B3 realmente
    datos = datosMu[0]

    if datosMu[1] == 'ecuacion':
        a = datosMu[0]['a']
        b = datosMu[0]['b']
        if (1+b*H) == 0:
            H = 1
            st.write('Hay un problema con la fórmula')
        else:
            B = a*H/(1+b*H)
    else:
        menorB = 0
        mayorB = 0
        menorH = 0
        mayorH = 0
        b_array = datos['B (T)'].to_numpy()
        h_array = datos['H (Av/m)'].to_numpy()
        b_array, h_array = bubble_sort(b_array, h_array)
        print(h_array)
        print(b_array)
        for i in range(len(b_array)):
            if h_array[i] < abs(H):
                menorB = b_array[i]
                menorH = h_array[i]

            if h_array[i] > abs(H):
                mayorB = b_array[i]
                mayorH = h_array[i]
                break
        B = menorB + (H - menorH) * (mayorB - menorB) / (mayorH - menorH)
    print(B)
    print(H)
    # Lo estaba dividiendo por error
    flujo = B*(SL*factorApilado)
    print('flujo')
    print(flujo)
    return flujo
