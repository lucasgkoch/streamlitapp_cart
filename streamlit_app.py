import streamlit as st
import pickle
import numpy as np

# Configurar el ancho total de la página
st.set_page_config(layout="wide")


# Interfaz de usuario de la aplicación
st.title('Predicción de Abandono de Carrito')

# Subtítulo
st.markdown("<h2 style='text-align: center;'>Ingrese los detalles de la sesión que desea predecir</h2>", unsafe_allow_html=True)


column1, column2, column3 = st.columns(3)

with column1:
    detalles_producto = st.selectbox('Detalles_Del_Producto_Vistos', [0, 1])
    articulos_eliminados = st.number_input('Nro_Articulos_Eliminados_Del_Carrito', min_value=0, step=1)
    sesiones_usuario = st.number_input('Nro_Inicios_Sesion', min_value=0, step=1)

with column2:
    paginas_cambiadas = st.number_input('Nro_Visualizaciones_Articulos__Carrito', min_value=0, step=1)
    visualizaciones_carrito = st.number_input('Nro_Visualizaciones_Del_Carrito', min_value=0, step=1)
    paginas_visitadas = st.number_input('Nro_Paginas_VistaS', min_value=1, step=1)

with column3:
    articulos_carrito = st.number_input('Nro_Articulos_En_Carrito', min_value=0, step=1)
    inicios_pago = st.number_input('Nro_Pago_Iniciado', min_value=0, step=1)
    tipo_cliente = st.selectbox('Tipo_De_Cliente', [0, 1, 2])

# Centrar el botón
st.markdown("<h1 style='text-align: center;'></h1>", unsafe_allow_html=True)

if st.button('Predecir'):
    st.write('La probabilidad de que el cliente abandone el carrito es: X.XX')
