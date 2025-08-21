import streamlit as st
st.title ("Mi primera app")

from PIL import image 

image = Image.open('Escarabajo_de_Blue_Beetle.jpg')
st.image(image, caption = 'Interfaces Multimodales')
