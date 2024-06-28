import streamlit as st
import pandas as pd
import plotly.express as px
from influxdb_client import InfluxDBClient

# Configuración de la conexión a InfluxDB
url = "http://influxdb:8086"
token = "labtcpip-iotdata-auth-token"
org = "labiot2024"
bucket = "iotdata"

# Creación del cliente de InfluxDB
client = InfluxDBClient(url=url, token=token, org=org)
query_api = client.query_api()

# Definición de opciones de datos
data_options = {
    "Temperatura de CPU": ("raspy_measurement", "cpu_temp"),
    "Uso de CPU": ("raspy_measurement", "cpu_usage"),
    "Humedad de Ambiente": ("dht11_measurement", "DHT11_Humidity"),
    "Temperatura de Ambiente": ("dht11_measurement", "DHT11_Temperature"),
    "Voltaje": ("sonoff_measurement", "ENERGY_Voltage"),
    "Corriente": ("sonoff_measurement", "ENERGY_Current")
}

# Sidebar para selección de tipo de dato
st.sidebar.header("Seleccionar Tipo de Dato")
option = st.sidebar.selectbox("", list(data_options.keys()))
measurement, field = data_options[option]

# Sidebar para selección de periodo de tiempo
st.sidebar.header("Seleccionar Periodo de Tiempo")
time_options = {
    "Últimos 15 minutos": "-15m",
    "Última hora": "-1h",
    "Últimas 6 horas": "-6h",
    "Últimas 12 horas": "-12h",
    "Último día": "-1d"
}
time_selection = st.sidebar.selectbox("", list(time_options.keys()), index=0)
time_range = time_options[time_selection]

# Consulta a la base de datos
query = f'''
from(bucket: "{bucket}")
|> range(start: {time_range})
|> filter(fn: (r) => r["_measurement"] == "{measurement}")
|> filter(fn: (r) => r["_field"] == "{field}")
|> sort(columns: ["_time"], desc: false)
'''

# Ejecución de la consulta
df = query_api.query_data_frame(query)

# Visualización de los datos
fig = px.line(df, x='_time', y='_value', title=f'{option}')
st.plotly_chart(fig)

# Cálculo de estadísticas
mean_value = df['_value'].mean()
median_value = df['_value'].median()
max_value = df['_value'].max()
min_value = df['_value'].min()
std_value = df['_value'].std()

# Mostrar estadísticas
st.write(f"### Estadísticas para {option}")
st.write(f"Media: {mean_value:.2f}")
st.write(f"Mediana: {median_value:.2f}")
st.write(f"Máximo: {max_value:.2f}")
st.write(f"Mínimo: {min_value:.2f}")
st.write(f"Desviación Estándar: {std_value:.2f}")
