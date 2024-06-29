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
  ch = st.number_input("\# Chilaquiles:", min_value=0, value=0)

total = 0
# contenedores
plato, torta, jamon, manchego, huevo = [0]*ch, [0]*ch, [0]*ch, [0]*ch, [0]*ch
for i in range(ch):
  st.subheader(f"Chilaquil-{i + 1}")
  #cols = chilaquiles * 5
  "c" + str(i+3), "c" + str(i+4), "c" + str(i+5), "c" + str(i+6), "c" + str(i+7) = st.columns([1, 1, 1, 1, 1])
  with "c" + str(i+3):
    plato[i] = (st.number_input("Plato:", min_value=0, value=0))
  with f"c{i+4}":
    torta[i] = st.number_input("Torta:", min_value=0, value=0)
  with f"c{i+5}":
    jamon[i] = st.number_input("Jamón:", min_value=0, value=0)
  with f"c{i+6}":
    manchego[i] = st.number_input("Manchego:", min_value=0, value=0)
  with f"c{i+7}":
    huevo[i] = st.number_input("Huevo", min_value=0, value=0)

st.write(plato)
st.write(torta)
st.write(jamon)
st.write(manchego)
st.write(huevo)





