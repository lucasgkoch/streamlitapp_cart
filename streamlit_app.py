import streamlit as st
import pickle
import numpy as np



# Interfaz de usuario de la aplicación
st.title('Predicción de Abandono de Carrito')

column1, column2, column3 = st.columns(3)

with column1:
    detalles_producto = st.selectbox('Detalles del producto vistos', [0, 1])
    articulos_eliminados = st.number_input('Cantidad de artículos eliminados del carrito', min_value=0, step=1)
    sesiones_usuario = st.number_input('Cantidad de inicios de sesión del usuario', min_value=0, step=1)

with column2:
    paginas_cambiadas = st.number_input('Cantidad de veces que el cliente cambia de página', min_value=0, step=1)
    visualizaciones_carrito = st.number_input('Número de visualizaciones del carrito', min_value=0, step=1)
    paginas_visitadas = st.number_input('Cantidad de páginas visitadas', min_value=1, step=1)

with column3:
    articulos_carrito = st.number_input('Cantidad de artículos en el carrito', min_value=0, step=1)
    inicios_pago = st.number_input('Número de veces que se inició el proceso de pago', min_value=0, step=1)
    tipo_cliente = st.selectbox('Tipo de cliente', [0, 1, 2])


if st.button('Predecir'):
    st.write('La probabilidad de que el cliente abandone el carrito es: X.XX')
