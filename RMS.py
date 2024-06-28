
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

# for chilaquil in chilaquiles:
st.header(f"{chilaquil}")
c3, c4, c5, c6, c7 = st.columns([1, 1, 1, 1, 1])
with c3:
  pedido = st.number_input("Plato:", min_value=0, value=0)
with c4:
  chilaquiles = st.number_input("Torta:", min_value=0, value=0)
with c5:
  chilaquiles = st.number_input("Jamón:", min_value=0, value=0)
with c6:
  chilaquiles = st.number_input("Manchego:", min_value=0, value=0)
with c7:
  chilaquiles = st.number_input("Huevo", min_value=0, value=0)






