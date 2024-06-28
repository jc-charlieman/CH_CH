
# import pandas as pd
# import numpy as np
import streamlit as st

# Sidebar
st.title("CHILAQUIL CHILANGO by Wisho!.")

# Subtitulo
st.subheader("Menú:")

# Comida
c1, c2 = st.columns([1, 1])
with c1:
  pedido = st.number_input("\# Pedido:", min_value=0, value=0)
with c2:
  chilaquiles = st.number_input("\# Chilaquiles:", min_value=0, value=0)

total = 0
# contenedores
plato, torta, jamon, manchego, huevo = [0], [0], [0], [0], [0]
for i in range(chilaquiles):
  st.subheader(f"Chilaquil-{i + 1}")
  c3, c4, c5, c6, c7 = st.columns([1, 1, 1, 1, 1])
  with c3:
    plato[i] = st.number_input("Plato:", min_value=0, value=0)
  with c4:
    torta[i] = st.number_input("Torta:", min_value=0, value=0)
  with c5:
    jamon[i] = st.number_input("Jamón:", min_value=0, value=0)
  with c6:
    manchego[i] = st.number_input("Manchego:", min_value=0, value=0)
  with c7:
    huevo[i] = st.number_input("Huevo", min_value=0, value=0)

st.write(plato)
st.write(torta)
st.write(jamon)
st.write(manchego)
st.write(huevo)





