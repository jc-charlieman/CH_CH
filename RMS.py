
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
  pedido = st.number_input("\#Pedido:", min_value=0, value=0)
with c2:
  chilaquiles = st.number_input("No. Chilaquiles:", min_value=0, value=0)


# for chilaquil in chilaquiles:
#   st.write("")




