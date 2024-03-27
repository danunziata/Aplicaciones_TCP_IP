import streamlit as st
import pandas as pd #manipulación y análisis de datos
import numpy as np #especializada en el cálculo numérico y el análisis de datos,

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data #para caché
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
# load_data es una función antigua que descarga algunos datos, los coloca en un marco de datos de Pandas y convierte la columna de fecha del texto a fecha y hora. La función acepta un solo parámetro (nrows), que especifica el número de filas que desea cargar en el marco de datos.
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")

#Resulta que lleva mucho tiempo descargar datos y cargar 10,000 líneas en un dataframe. Convertir la columna de fecha en fecha y hora no es un trabajo rápido tampoco. No desea volver a cargar los datos cada vez que se actualiza la aplicación – afortunadamente Streamlit le permite almacenar en caché los datos.

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

#histograma
st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

#mapa
hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)