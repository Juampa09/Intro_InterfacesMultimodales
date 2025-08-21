import streamlit as st
st.title ("Mi primera app")

from PIL import image 


st.header("En este espacio comienzo a crear mis apps para interfaces multimodales.")
st.write("Fácilmente puedo realizar backend y frontend.")
image = Image.open('Escarabajo_de_Blue_Beetle.jpg')
st.image(image, caption = 'Interfaces Multimodales')
