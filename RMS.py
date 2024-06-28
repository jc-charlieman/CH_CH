
# import pandas as pd
# import numpy as np
import streamlit as st

# Sidebar
st.title("CHILAQUIL CHILANGO by Wisho!.")

# Subtitulo
st.subheader("Menú:")



# Comida
c1, c2 = st.columns([1, 4])
with c1:
  st.write("\n")
  st.write("\n")
  st.write("Total de Chilaquiles:")
with c2:
  # chilaquiles = st.number_input("", min_value=0, value=0)
  chilaquiles = st.text_input("")



