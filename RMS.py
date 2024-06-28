
# import pandas as pd
# import numpy as np
import streamlit as st


# Sidebar
st.title("CHILAQUIL CHILANGO by Wisho!.")

# Subtitulo
st.subheader("Menú:")

# Comida
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
  i1 = st.number_input("Ch-1:", value=0, min_value=0)
with col2:
  i2 = st.number_input("Ch-2", value=0)
with col3:
  i3 = st.number_input("Ch-3", value=0)
with col4:
  i4 = st.number_input("Ch-4", value=0)
  
col5, col6, col7, col8 = st.columns([1, 1, 1, 1])
with col5:
  i1 = st.number_input("Ch-5:", value=0, min_value=0)
with col6:
  i2 = st.number_input("Ch-6", value=0)
with col7:
  i3 = st.number_input("Ch-7", value=0)
with col8:
  i4 = st.number_input("Ch-8", value=0)


