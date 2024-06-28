
# import pandas as pd
# import numpy as np
import streamlit as st


# Sidebar
st.title("CHILAQUIL CHILANGO by Wisho!.")

col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
  i1 = st.number_input("Ch-1:")
with col2:
  i2 = st.number_input("Ch-2")
with col3:
  i3 = st.number_input("Ch-3")
with col4:
  i4 = st.number_input("Ch-4")

