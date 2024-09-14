import streamlit as st
import pandas as pd


def main():
    st.title("Table Input Tool")

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
    st.session_state.df = st.dataframe(st.session_state.df)


if __name__ == "__main__":
    main()
