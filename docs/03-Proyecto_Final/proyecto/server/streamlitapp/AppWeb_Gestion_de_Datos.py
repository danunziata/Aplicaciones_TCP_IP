import streamlit as st
import pandas as pd
import plotly.express as px
from influxdb_client import InfluxDBClient

# Configuración de la conexión a InfluxDB
url = "http://localhost:8086"
token = "my-token"
org = "my-org"
bucket = "my-bucket"

# Creación del cliente de InfluxDB
client = InfluxDBClient(url=url, token=token, org=org)
query_api = client.query_api()

# Definición de opciones de datos
data_options = {
    "Temperatura de CPU": ("cpu_temperature", "value"),
    "Uso de CPU": ("cpu_usage", "value"),
    "Humedad de Ambiente": ("ambient_humidity", "value"),
    "Temperatura de Ambiente": ("ambient_temperature", "value"),
    "Voltaje": ("voltage", "value"),
    "Corriente": ("current", "value")
}

# Sidebar para selección de tipo de dato
st.sidebar.header("Seleccionar Tipo de Dato")
option = st.sidebar.selectbox("", list(data_options.keys()))
measurement, field = data_options[option]

# Consulta a la base de datos
query = f'''
from(bucket: "{bucket}")
|> range(start: -1d)
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
