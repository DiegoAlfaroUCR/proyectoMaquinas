# Archivo para iniciar el programa.

# Diego Alfaro Segura (C20259), Ismael José Alvarado Pérez (C20366). Grupo 1

import subprocess
import importlib.util

lib_spec = importlib.util.find_spec('streamlit')
if lib_spec is not None:
    # Path to your Streamlit app
    app_path = 'src/Interfaz.py'

    # Command to run Streamlit
    command = ['streamlit', 'run', app_path]

    # Execute the command in the background
    subprocess.Popen(command)
else:
    print('No tiene la librería streamlit instalada. ' +
          'Para usar el programa, debe instalarla con el comando:\n' +
          'pip install streamlit')
