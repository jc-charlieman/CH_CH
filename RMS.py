import pandas as pd
import streamlit as st
from datetime import datetime, timedelta

# Sidebar
st.title("CHILAQUIL CHILANGO by Wisho!.")

# Subtitulo
st.subheader("Menú:")

try:
  # Comida
  col1, col2 = st.columns([1, 1])
  with col1:
    orden = st.number_input("\# Orden:", min_value=0, value=0)
    now = datetime.now() - timedelta(hours=6)
    now = now.strftime("%d/%m/%y %H:%M:%S")
    now = datetime.strptime(now, "%d/%m/%y %H:%M:%S")
  with col2:
    ch = st.number_input("\# Chilaquiles:", min_value=0, value=0)
  
  total = 0
  # contenedores
  plato, torta, jamon, manchego, huevo = [0]*ch, [0]*ch, [0]*ch, [0]*ch, [0]*ch 
  pollo, bisteck, milanesa, arrachera, aguacate = [0]*ch, [0]*ch, [0]*ch, [0]*ch, [0]*ch
  d = {}
  df0 = pd.DataFrame()
  
  for i in range(1, ch + 1):
    st.subheader(f"Chilaquil-{i}")
    # Diccionario para almacenar los artículos
    d["Fecha"] = now
    d["orden"] = []
    d["articulo"] = []
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
          d["articulo"].append(f"ch-{i}")
          d["ingredientes"].append("plato")
          d["volumen"].append(plato[i-1])
          d["costo"].append(plato[i-1] * 65)
      with c2:
        torta[i-1] = st.number_input("Torta:", min_value=0, value=0, key=k[1])
        if torta[i-1] > 0:
          d["orden"].append(orden)
          d["articulo"].append(f"ch-{i}")
          d["ingredientes"].append("torta")
          d["volumen"].append(torta[i-1])
          d["costo"].append(torta[i-1] * 60)
      with c3:
        jamon[i-1] = st.number_input("Jamón:", min_value=0, value=0, key=k[2])
        if jamon[i-1] > 0:
          d["orden"].append(orden)
          d["articulo"].append(f"ch-{i}")
          d["ingredientes"].append("jamon")
          d["volumen"].append(jamon[i-1])
          d["costo"].append(jamon[i-1] * 10)
      with c4:
        manchego[i-1] = st.number_input("Manchego:", min_value=0, value=0, key=k[3])
        if manchego[i-1] > 0:
          d["orden"].append(orden)
          d["articulo"].append(f"ch-{i}")
          d["ingredientes"].append("manchego")
          d["volumen"].append(manchego[i-1])
          d["costo"].append(manchego[i-1] * 15)
      with c5:
        huevo[i-1] = st.number_input("Huevo", min_value=0, value=0, key=k[4])
        if huevo[i-1] > 0:
          d["orden"].append(orden)
          d["articulo"].append(f"ch-{i}")
          d["ingredientes"].append("huevo")
          d["volumen"].append(huevo[i-1])
          d["costo"].append(huevo[i-1] * 15)
      with c6:
        pollo[i-1] = (st.number_input("Pollo:", min_value=0, value=0, key=k[5]))
        if pollo[i-1] > 0:
          d["orden"].append(orden)
          d["articulo"].append(f"ch-{i}")
          d["ingredientes"].append("pollo")
          d["volumen"].append(pollo[i-1])
          d["costo"].append(pollo[i-1] * 20)  
      with c7:
        bisteck[i-1] = st.number_input("Bisteck:", min_value=0, value=0, key=k[6])
        if bisteck[i-1] > 0:
          d["orden"].append(orden)
          d["articulo"].append(f"ch-{i}")
          d["ingredientes"].append("bisteck")
          d["volumen"].append(bisteck[i-1])
          d["costo"].append(bisteck[i-1] * 30)
      with c8:
        milanesa[i-1] = st.number_input("Milanesa:", min_value=0, value=0, key=k[7])
        if milanesa[i-1] > 0:
          d["orden"].append(orden)
          d["articulo"].append(f"ch-{i}")
          d["ingredientes"].append("milanesa")
          d["volumen"].append(milanesa[i-1])
          d["costo"].append(milanesa[i-1] * 35)    
      with c9:
        arrachera[i-1] = st.number_input("Arrachera:", min_value=0, value=0, key=k[8])
        if arrachera[i-1] > 0:
          d["orden"].append(orden)
          d["articulo"].append(f"ch-{i}")
          d["ingredientes"].append("arrachera")
          d["volumen"].append(arrachera[i-1])
          d["costo"].append(arrachera[i-1] * 50)       
      with c10:
        aguacate[i-1] = st.number_input("Aguacate", min_value=0, value=0, key=k[9])
        if aguacate[i-1] > 0:
          d["orden"].append(orden)
          d["articulo"].append(f"ch-{i}")
          d["ingredientes"].append("aguacate")
          d["volumen"].append(aguacate[i-1])
          d["costo"].append(aguacate[i-1] * 10)        
  
      subtotal = sum(d["costo"])
      total += subtotal
      # df0 = pd.DataFrame()
      df1 = pd.DataFrame(d)
      df = pd.concat([df0, df1])
      st.write(df)
      
    else:
      k = [k for k in range(10*i, 10*i - 10, -1)]
      with c1:
        plato[i-1] = (st.number_input("Plato:", min_value=0, value=0, key=k[0]))
        if plato[i-1] > 0:
          d["orden"].append(orden)
          d["articulo"].append(f"ch-{i}")
          d["ingredientes"].append("plato")
          d["volumen"].append(plato[i-1])
          d["costo"].append(plato[i-1] * 65)  
      with c2:
        torta[i-1] = st.number_input("Torta:", min_value=0, value=0, key=k[1])
        if torta[i-1] > 0:
          d["orden"].append(orden)
          d["articulo"].append(f"ch-{i}")
          d["ingredientes"].append("torta")
          d["volumen"].append(torta[i-1])
          d["costo"].append(torta[i-1] * 60)
      with c3:
        jamon[i-1] = st.number_input("Jamón:", min_value=0, value=0, key=k[2])
        if jamon[i-1] > 0:
          d["orden"].append(orden)
          d["articulo"].append(f"ch-{i}")
          d["ingredientes"].append("jamon")
          d["volumen"].append(jamon[i-1])
          d["costo"].append(jamon[i-1] * 10)    
      with c4:
        manchego[i-1] = st.number_input("Manchego:", min_value=0, value=0, key=k[3])
        if manchego[i-1] > 0:
          d["orden"].append(orden)
          d["articulo"].append(f"ch-{i}")
          d["ingredientes"].append("manchego")
          d["volumen"].append(manchego[i-1])
          d["costo"].append(manchego[i-1] * 15)    
      with c5:
        huevo[i-1] = st.number_input("Huevo", min_value=0, value=0, key=k[4])
        if huevo[i-1] > 0:
          d["orden"].append(orden)
          d["articulo"].append(f"ch-{i}")
          d["ingredientes"].append("huevo")
          d["volumen"].append(huevo[i-1])
          d["costo"].append(huevo[i-1] * 15)      
      with c6:
        pollo[i-1] = (st.number_input("Pollo:", min_value=0, value=0, key=k[5]))
        if pollo[i-1] > 0:
          d["orden"].append(orden)
          d["articulo"].append(f"ch-{i}")
          d["ingredientes"].append("pollo")
          d["volumen"].append(pollo[i-1])
          d["costo"].append(pollo[i-1] * 20)      
      with c7:
        bisteck[i-1] = st.number_input("Bisteck:", min_value=0, value=0, key=k[6])
        if bisteck[i-1] > 0:
          d["orden"].append(orden)
          d["articulo"].append(f"ch-{i}")
          d["ingredientes"].append("bisteck")
          d["volumen"].append(bisteck[i-1])
          d["costo"].append(bisteck[i-1] * 30)      
      with c8:
        milanesa[i-1] = st.number_input("Milanesa:", min_value=0, value=0, key=k[7])
        if milanesa[i-1] > 0:
          d["orden"].append(orden)
          d["articulo"].append(f"ch-{i}")
          d["ingredientes"].append("milanesa")
          d["volumen"].append(milanesa[i-1])
          d["costo"].append(milanesa[i-1] * 35)       
      with c9:
        arrachera[i-1] = st.number_input("Arrachera:", min_value=0, value=0, key=k[8])
        if arrachera[i-1] > 0:
          d["orden"].append(orden)
          d["articulo"].append(f"ch-{i}")
          d["ingredientes"].append("arrachera")
          d["volumen"].append(arrachera[i-1])
          d["costo"].append(arrachera[i-1] * 50)      
      with c10:
        aguacate[i-1] = st.number_input("Aguacate", min_value=0, value=0, key=k[9])
        if aguacate[i-1] > 0:
          d["orden"].append(orden)
          d["articulo"].append(f"ch-{i}")
          d["ingredientes"].append("aguacate")
          d["volumen"].append(aguacate[i-1])
          d["costo"].append(aguacate[i-1] * 10)        
  
      subtotal = sum(d["costo"])
      total += subtotal
      # df0 = pd.DataFrame()
      df2 = pd.DataFrame(d)
      df = pd.concat([df, df2])
      st.write(df)
  
    st.write(total)
    
  @st.cache
  def convert_csv(df):
    return df.to_csv(index=False).encode("utf-8")
  
  csv = convert_csv(df)
  st.download_button(label="Download CSV", data=csv, file_name= "Cuenta" + ".csv", mime="text/csv")

except:
  st.write("Ingresa un pedido!.")
  pass
