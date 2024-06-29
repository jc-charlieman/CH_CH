# import pandas as pd
# import numpy as np
import streamlit as st

# Sidebar
st.title("CHILAQUIL CHILANGO by Wisho!.")

# Subtitulo
st.subheader("Menú:")

# Comida
col1, col2 = st.columns([1, 1])
with col1:
  pedido = st.number_input("\# Pedido:", min_value=0, value=0)
with col2:
  ch = st.number_input("\# Chilaquiles:", min_value=0, value=0)

total = 0
# contenedores
plato, torta, jamon, manchego, huevo = [0]*ch, [0]*ch, [0]*ch, [0]*ch, [0]*ch
for i in range(1, ch + 1):
  st.subheader(f"Chilaquil-{i + 1}")
  #cols = chilaquiles * 5
  #c = [f"c{ch * (col + 3)}" for col in range(5)]
  if i == 1:
      c = [f"c{ch * (col + 3)}" for col in range(5)]
    c[0], c[1], c[2], c[3], c[4] = st.columns([1, 1, 1, 1, 1])
    with c[0]:
      plato[i] = (st.number_input("Plato:", min_value=0, value=0))
    with c[1]:
      torta[i] = st.number_input("Torta:", min_value=0, value=0)
    with c[2]:
      jamon[i] = st.number_input("Jamón:", min_value=0, value=0)
    with c[3]:
      manchego[i] = st.number_input("Manchego:", min_value=0, value=0)
    with c[4]:
      huevo[i] = st.number_input("Huevo", min_value=0, value=0)
  else:
    c = [f"c{col}" for col in range(5*ch, 5*ch - 5, -1)]
    c[0], c[1], c[2], c[3], c[4] = st.columns([1, 1, 1, 1, 1])
    with c[0]:
      plato[i] = (st.number_input("Plato:", min_value=0, value=0))
    with c[1]:
      torta[i] = st.number_input("Torta:", min_value=0, value=0)
    with c[2]:
      jamon[i] = st.number_input("Jamón:", min_value=0, value=0)
    with c[3]:
      manchego[i] = st.number_input("Manchego:", min_value=0, value=0)
    with c[4]:
      huevo[i] = st.number_input("Huevo", min_value=0, value=0)
    
st.write(plato)
st.write(torta)
st.write(jamon)
st.write(manchego)
st.write(huevo)





