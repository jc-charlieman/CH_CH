
# import pandas as pd
# import numpy as np
import streamlit as st

# Sidebar
st.title("CHILAQUIL CHILANGO by Wisho!.")

# Subtitulo
st.subheader("Menú:")

# Comida


# col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
# with col1:
#   i1 = st.number_input("Ch-1:", value=0, min_value=0)
# with col2:
#   i2 = st.number_input("Ch-2", value=0)
# with col3:
#   i3 = st.number_input("Ch-3", value=0)
# with col4:
#   i4 = st.number_input("Ch-4", value=0)

# chilaquiles = 2
col1, col2 = st.columns([1, 1])
with col1:
  st.subheader("Total de Chilaquiles")
with col2:
  chilaquiles = st.number_input(min_value=0, value=0)
  



