# Archivo para iniciar el programa.

import subprocess
import streamlit as st

# Path to your Streamlit app
app_path = 'src/src.py'

# Command to run Streamlit
command = ['streamlit', 'run', app_path]

# Execute the command in the background
subprocess.Popen(command)
