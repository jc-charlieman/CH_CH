
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

for n in range(1, chilaquiles + 1):
  st.subheader(f"Chilaquil-{n}")
  c3, c4, c5, c6, c7 = st.columns([1, 1, 1, 1, 1])
  with c3:
    plato = st.number_input("Plato:", min_value=0, value=0)
  with c4:
    torta = st.number_input("Torta:", min_value=0, value=0)
  with c5:
    jamon = st.number_input("Jamón:", min_value=0, value=0)
  with c6:
    manchego = st.number_input("Manchego:", min_value=0, value=0)
  with c7:
    huevo = st.number_input("Huevo", min_value=0, value=0)

st.write("Done")





