# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:32:07 2023

@author: camac
"""
import webbrowser
import streamlit as st
from PIL import Image
import json
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title="SPACE SCAPE ", page_icon="👾")

st.markdown("# SPACE SCAPE 🕹️")
st.sidebar.header("GOTY 💀💀💀")
st.write("""ESPACE SCAPE es un juego 3D de aventura desarollado por Daniel Camacho y Santiago herrera
       con el motor de desarrollo de video juegos UNITY """)
image = Image.open('mapa.png')
st.image(image, caption='MAPA MENTAL')

st.markdown("# 🔧 UNITY 🛠")
st.markdown("""<p style='text-align: justify;'>La primera versión de Unity se lanzó en la
            Conferencia Mundial de Desarrolladores de Apple en 2005.Fue 
            construido exclusivamente para funcionar y generar proyectos en los equipos 
            de la plataforma Mac y obtuvo el éxito suficiente como para continuar con el
            desarrollo del motor y herramientas </p>""",unsafe_allow_html=True)

url = 'https://unity.com/es/download'

if st.button('USA UNITY'):
    webbrowser.open_new_tab(url)

video_file = open('C:/Users/sajoh/Desktop/multipagidaspace/thegame_Trim.mp4','rb')
video_bytes = video_file.read()
st.video(video_file)

lottie_load = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_ZQhQzO.json")

st_lottie(
        lottie_load,
        speed=1,
        reverse=False,
        loop=True,
        quality="high", # medium ; high
         # canvas
        height=300,
        width=300,
        key=None,
    )


