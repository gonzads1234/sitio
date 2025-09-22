import streamlit as st
from PIL import Image
import pandas as pd

df_flow_cash = pd.read_csv('clean_data_mc_sim.csv', encoding='utf-8')

df_flow_cash.drop('index', axis=1, inplace=True)

image = Image.open('./pc_data.jpeg')

st.title("Hola, Bienvenido/a a mi Portafolio de Código y Data Science.")
st.image(image=image, caption='Data Science and Coding')

st.markdown("#### Mi nombre es **Gonzalo Cayunao Erices**.")
st.write("Soy Ingeniero Civil Industrial especializado en programación, data science y docencia.")
st.write("En este sitio podrás ver los múltiples proyectos que he realizado.")
st.write("Enjoy it! :sunglasses:")




