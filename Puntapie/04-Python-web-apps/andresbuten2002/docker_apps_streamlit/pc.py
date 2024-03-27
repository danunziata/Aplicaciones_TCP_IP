import streamlit as st
import psutil

# Función para obtener y mostrar información del sistema
def mostrar_info_sistema():
    # Obtener información del CPU
    cpu_percent = psutil.cpu_percent()
    cpu_temp = "No disponible"  # La temperatura del CPU puede variar dependiendo del sistema operativo y hardware
    try:
        # Esto puede variar según tu sistema operativo y hardware específico
        with open("/sys/class/thermal/thermal_zone0/temp") as temp_file:
            cpu_temp_raw = temp_file.readline()
            cpu_temp = int(cpu_temp_raw) / 1000.0
    except Exception as e:
        st.warning(f"No se pudo obtener la temperatura del CPU: {e}")

    # Obtener información de la memoria RAM
    ram = psutil.virtual_memory()
    ram_total = ram.total
    ram_usada = ram.used

    # Obtener información del disco
    disco = psutil.disk_usage('/')
    disco_total = disco.total
    disco_usado = disco.used
    disco_disponible = disco.free

    # Mostrar la información en la interfaz
    st.write(f"Porcentaje de uso del CPU: {cpu_percent}%")
    st.write(f"Temperatura del CPU: {cpu_temp}°C")
    st.write(f"Memoria RAM usada: {ram_usada / 1024**3:.2f} GB de {ram_total / 1024**3:.2f} GB")
    st.write(f"Espacio en disco usado: {disco_usado / 1024**3:.2f} GB de {disco_total / 1024**3:.2f} GB")
    st.write(f"Espacio en disco disponible: {disco_disponible / 1024**3:.2f} GB")

# Configurar la página de Streamlit
st.title("Visualización de Datos del Sistema en Tiempo Real")
st.header("Información del Sistema")

# Llamar a la función para mostrar la información del sistema
mostrar_info_sistema()
