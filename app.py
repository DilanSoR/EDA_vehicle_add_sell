import streamlit as st
import pandas as pd
import plotly.graph_objects as go


data = pd.read_csv('./vehicles_us.csv')

st.header('Vehicle Data Analysis')

st.write('Distribución del Odómetro')

hist_option = st.checkbox('Histograma')
if hist_option:
    fig = go.Figure(data=[go.Histogram(x=data['odometer'])])
    fig.update_layout(title='Distribución del Odómetro',
                      xaxis_title='Odómetro',
                      yaxis_title='Frecuencia')
    st.plotly_chart(fig)

st.write('Dispersión del Odómetro')

scat_option = st.checkbox('Gráfico de dispersión')
if scat_option:
    fig = go.Figure(data=go.Scatter(
        x=data['odometer'], y=data['price'], mode='markers'))
    fig.update_layout(title='Dispersión del Odómetro vs Precio',
                      xaxis_title='Odómetro',
                      yaxis_title='Precio')
    st.plotly_chart(fig)
