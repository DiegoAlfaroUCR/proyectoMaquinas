import subprocess
import importlib.util
import threading
import time

lib_spec = importlib.util.find_spec('streamlit')
if lib_spec is not None:
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
                print("Streamlit app closed.")
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
    print('No tiene la librería streamlit instalada. ' +
          'Para usar el programa, debe instalarla con el comando:\n' +
          'pip install streamlit')
