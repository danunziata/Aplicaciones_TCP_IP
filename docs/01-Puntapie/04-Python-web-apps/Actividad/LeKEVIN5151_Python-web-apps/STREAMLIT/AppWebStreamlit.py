import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
from datetime import datetime

# Función para obtener las probabilidades de cierre al alza y a la baja
def obtener_probabilidades(bitcoin_data):
    up_days = bitcoin_data[bitcoin_data['Daily Change'] > 0]
    down_days = bitcoin_data[bitcoin_data['Daily Change'] < 0]
    prob_up = len(up_days) / len(bitcoin_data)
    prob_down = len(down_days) / len(bitcoin_data)
    return prob_up, prob_down

# Función para obtener los datos históricos del precio del Bitcoin
def obtener_datos(periodo):
    if periodo == '1 día':
        return yf.download(tickers='BTC-USD', period='1d', interval='1m')
    elif periodo == '1 mes':
        return yf.download(tickers='BTC-USD', period='1mo', interval='1d')
    elif periodo == '1 año':
        return yf.download(tickers='BTC-USD', period='1y', interval='1d')

# Obtener datos históricos
bitcoin_data = obtener_datos('1 año')

# Calcular cambio porcentual diario
bitcoin_data['Daily Change'] = bitcoin_data['Close'].pct_change()

# Calcular las probabilidades de cierre al alza y a la baja
prob_up, prob_down = obtener_probabilidades(bitcoin_data)

# Obtener el precio actual del Bitcoin
btc_price = bitcoin_data['Close'][-1]

# Configuración de la página
st.title("Análisis de Bitcoin")
st.subheader("Precio actual del Bitcoin:")
st.write(f"${btc_price:.2f}")

st.subheader("Probabilidades de cierre:")
st.write(f"Probabilidad de cierre al alza: {prob_up:.2%}")
st.write(f"Probabilidad de cierre a la baja: {prob_down:.2%}")

# Graficar el valor del Bitcoin
st.subheader("Valor del Bitcoin")
periodo_grafica = st.selectbox("Seleccione el período para la gráfica", ['1 día', '1 mes', '1 año'])

if periodo_grafica == '1 día':
    datos_grafica = obtener_datos('1 día')
elif periodo_grafica == '1 mes':
    datos_grafica = obtener_datos('1 mes')
elif periodo_grafica == '1 año':
    datos_grafica = obtener_datos('1 año')

fig = go.Figure()
fig.add_trace(go.Scatter(x=datos_grafica.index, y=datos_grafica['Close'], mode='lines', name='Precio de cierre'))
fig.update_layout(title=f'Precio del Bitcoin ({periodo_grafica})', xaxis_title='Fecha', yaxis_title='Precio (USD)')
st.plotly_chart(fig)
