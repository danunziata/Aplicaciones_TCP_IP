# Streamlit
## Descripción
La aplicación Streamlit es una herramienta interactiva de visualización de datos que permite a los usuarios explorar y analizar métricas de varios sensores en tiempo real. Utilizando InfluxDB como fuente de datos, la aplicación proporciona gráficos dinámicos y estadísticas descriptivas, facilitando la interpretación de los datos recogidos por los sensores.

## Dockerfile
El siguiente Dockerfile se utiliza para construir la imagen de la aplicación Streamlit, configurando las dependencias necesarias para su ejecución:

```dockerfile
# streamlit/Dockerfile
FROM python:3.9-slim

# Instalación de dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia del código fuente
COPY . /app
WORKDIR /app

# Exposición del puerto por defecto de Streamlit
EXPOSE 8501

# Comando para ejecutar la aplicación
CMD ["streamlit", "run", "app.py"]
``` 
Este archivo se encuentra en: `/streamlitapp/Dockerfile`

## docker-compose.yaml
La configuración de docker-compose.yaml para el servicio de Streamlit se detalla a continuación. Este servicio se construye a partir del Dockerfile y utiliza variables de entorno para la configuración de la conexión a InfluxDB.

```yaml
streamlit:
  build: ./streamlit
  ports:
    - "8501:8501"
  environment:
    INFLUXDB_URL: http://influxdb:8086
    INFLUXDB_TOKEN: your_actual_token_here
    INFLUXDB_ORG: your_actual_org_here
    INFLUXDB_BUCKET: your_bucket
```

Este archivo se encuentra en: [docker-compose.yaml](https://github.com/danunziata/Aplicaciones_TCP_IP/blob/develop/docs/03-Proyecto_Final/proyecto/server/docker-compose.yaml)

Explicación de la Configuración
- build: Especifica la ruta al directorio que contiene el Dockerfile de la aplicación Streamlit.
- ports: Expone el puerto 8501 del contenedor para que la aplicación sea accesible desde el host.
environment: Configura las variables de entorno necesarias para la conexión a InfluxDB.

## Requisitos
El archivo requirements.txt contiene las dependencias necesarias para la aplicación:

- streamlit
- pandas
- plotly
- influxdb-client

## Código de la Aplicación
El archivo principal de la aplicación es `app.py`, el cual contiene el código para conectarse a InfluxDB, realizar consultas y visualizar los datos.

### Conexión a InfluxDB y Configuración
La conexión a InfluxDB se realiza utilizando las variables de entorno configuradas en `docker-compose.yam`. También se pueden configurar directamente en `app.py`.

```python
import os
from influxdb_client import InfluxDBClient
import pandas as pd
import streamlit as st
import plotly.express as px

# Configuración de la conexión a InfluxDB usando variables de entorno
url = os.getenv("INFLUXDB_URL", "http://influxdb:8086")
token = os.getenv("INFLUXDB_TOKEN", "your_actual_token_here")
org = os.getenv("INFLUXDB_ORG", "your_actual_org_here")
bucket = os.getenv("INFLUXDB_BUCKET", "iot_data")

# Creación del cliente de InfluxDB
client = InfluxDBClient(url=url, token=token, org=org)
query_api = client.query_api()
```
### Definición de Opciones de Datos
Las opciones de datos están predefinidas para facilitar la selección y visualización de diferentes métricas. Para otro tipo de sensores deberás editar los valores "field" y "measurment" para cada uno de tus tipos de datos. Para esta implementación son los siguientes:

```python

# Definición de opciones de datos basadas en la configuración de tu base de datos
data_options = {
    "Temperatura de CPU": ("cpu_metrics", "temperature"),
    "Uso de CPU": ("cpu_metrics", "usage"),
    "Humedad de Ambiente": ("environment_metrics", "humidity"),
    "Temperatura de Ambiente": ("environment_metrics", "temperature"),
    "Voltaje": ("power_metrics", "voltage"),
    "Corriente": ("power_metrics", "current")
}
```
### Construcción y Ejecución de la Consulta
La consulta Flux se construye dinámicamente en función de la selección del usuario y se ejecuta para obtener los datos desde InfluxDB.

```python
# Sidebar para selección de tipo de dato
st.sidebar.header("Seleccionar Tipo de Dato")
option = st.sidebar.selectbox("Selecciona el tipo de dato:", list(data_options.keys()))
measurement, field = data_options[option]

# Construcción de la consulta
query = f'''
from(bucket: "{bucket}")
|> range(start: -1d)
|> filter(fn: (r) => r["_measurement"] == "{measurement}")
|> filter(fn: (r) => r["_field"] == "{field}")
|> sort(columns: ["_time"], desc: false)
'''

# Ejecución de la consulta
df = query_api.query_data_frame(query)
```

### Visualización y Estadísticas
Si se obtienen datos, se visualizan en un gráfico y se calculan estadísticas descriptivas.

```python
# Verificación si hay datos y visualización
if not df.empty:
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
else:
    st.warning(f"No se encontraron datos para {option} en el período seleccionado.")
```
### Integración con InfluxDB
La aplicación Streamlit se conecta a InfluxDB utilizando los parámetros configurados en `docker-compose.yaml`. A través de consultas Flux, extrae los datos necesarios y los permite visualizar de manera interactiva. 

### Resumen
Esta configuración asegura que la aplicación Streamlit esté correctamente preparada para visualizar y analizar los datos almacenados en InfluxDB. Utilizando Docker y Docker Compose, se puede desplegar fácilmente la aplicación junto con su entorno de bases de datos, facilitando la gestión y escalabilidad del sistema. La interfaz de Streamlit permite a los usuarios interactuar con los datos y obtener información valiosa de manera intuitiva y eficaz.