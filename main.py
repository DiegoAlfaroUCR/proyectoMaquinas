# Versión de python: 3.12.1

import subprocess
import importlib.util
import threading
import time

# Se busca si se tienen todos los paquetes

faltanPaquetes = False
listaPaquetes = ['streamlit', 'pynput', 'PIL']

print('Para usar este programa requiere tener instalado un navegador web' +
      ' . Se recomienda Firefox.')

for paquete in listaPaquetes:
    if importlib.util.find_spec(paquete) is None:
        faltanPaquetes = True

if not faltanPaquetes:
    # Path to your Streamlit app
    app_path = 'src/Interfaz.py'

    # Command to run Streamlit
    command = ['streamlit', 'run', app_path]

    # Start the process
    process = subprocess.Popen(command)

    def monitor_process(process):
        # Monitor the process and terminate it if closed
        while True:
            retcode = process.poll()  # Check if the process has terminated
            if retcode is not None:
                print("Calculadora cerrada correctamente.")
                break
            time.sleep(1)  # Wait a bit before checking again

    # Start monitoring in a separate thread
    monitor_thread = threading.Thread(target=monitor_process, args=(process,))
    monitor_thread.start()

    try:
        # Wait for the monitoring thread to finish
        monitor_thread.join()
    except KeyboardInterrupt:
        # Attempt to close the Streamlit app gracefully
        process.terminate()  # Send terminate signal to Streamlit
        process.wait()  # Wait for the process to terminate
        print("Programa finalizado con CTRL + C.")
    finally:
        # Ensure the process is killed if it's still running
        if process.poll() is None:
            print("Finalizando el proceso de streamlit...")
            process.kill()
else:
    print('\nNo tiene las librerías requeridas instaladas. ' +
          'Para usar el programa, debe instalarlas con el comando:\n' +
          'pip install streamlit pynput Pillow')
