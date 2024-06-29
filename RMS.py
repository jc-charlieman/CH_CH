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
  orden = st.number_input("\# Orden:", min_value=0, value=0)
with col2:
  ch = st.number_input("\# Chilaquiles:", min_value=0, value=0)

total = 0
# contenedores
plato, torta, jamon, manchego, huevo = [0]*ch, [0]*ch, [0]*ch, [0]*ch, [0]*ch 
pollo, bisteck, milanesa, arrachera, aguacate = [0]*ch, [0]*ch, [0]*ch, [0]*ch, [0]*ch
d = {}

for i in range(1, ch + 1):
  st.subheader(f"Chilaquil-{i}")
  # Diccionario para almacenar los artículos
  d["articulo"] = f"ch-{i}"
  d["ingredientes"] = []
  d["volumen"] = []
  d["costo"] = []
  
  # Widgets 
  c1, c2, c3, c4, c5 = st.columns([1, 1, 1, 1, 1])
  c6, c7, c8, c9, c10 = st.columns([1, 1, 1, 1, 1])
  if i == 1:
    k = [k for k in range(i, i + 10)]
    with c1:
      plato[i-1] = (st.number_input("Plato:", min_value=0, value=0, key=k[0]))
      if plato[i-1] > 0:
        d["orden"].append(orden)
        d["volumen"].append(plato[i-1])
        d["costo"].append(plato[i-1] * 65)
    with c2:
      torta[i-1] = st.number_input("Torta:", min_value=0, value=0, key=k[1])
    with c3:
      jamon[i-1] = st.number_input("Jamón:", min_value=0, value=0, key=k[2])
    with c4:
      manchego[i-1] = st.number_input("Manchego:", min_value=0, value=0, key=k[3])
    with c5:
      huevo[i-1] = st.number_input("Huevo", min_value=0, value=0, key=k[4])
    with c6:
      pollo[i-1] = (st.number_input("Pollo:", min_value=0, value=0, key=k[5]))
    with c7:
      bisteck[i-1] = st.number_input("Bisteck:", min_value=0, value=0, key=k[6])
    with c8:
      milanesa[i-1] = st.number_input("Milanesa:", min_value=0, value=0, key=k[7])
    with c9:
      arrachera[i-1] = st.number_input("Arrachera:", min_value=0, value=0, key=k[8])
    with c10:
      aguacate[i-1] = st.number_input("Aguacate", min_value=0, value=0, key=k[9])
    
  else:
    k = [k for k in range(10*i, 10*i - 10, -1)]
    with c1:
      plato[i-1] = (st.number_input("Plato:", min_value=0, value=0, key=k[0]))
    with c2:
      torta[i-1] = st.number_input("Torta:", min_value=0, value=0, key=k[1])
    with c3:
      jamon[i-1] = st.number_input("Jamón:", min_value=0, value=0, key=k[2])
    with c4:
      manchego[i-1] = st.number_input("Manchego:", min_value=0, value=0, key=k[3])
    with c5:
      huevo[i-1] = st.number_input("Huevo", min_value=0, value=0, key=k[4])
    with c6:
      pollo[i-1] = (st.number_input("Pollo:", min_value=0, value=0, key=k[5]))
    with c7:
      bisteck[i-1] = st.number_input("Bisteck:", min_value=0, value=0, key=k[6])
    with c8:
      milanesa[i-1] = st.number_input("Milanesa:", min_value=0, value=0, key=k[7])
    with c9:
      arrachera[i-1] = st.number_input("Arrachera:", min_value=0, value=0, key=k[8])
    with c10:
      aguacate[i-1] = st.number_input("Aguacate", min_value=0, value=0, key=k[9])

st.write(d)





