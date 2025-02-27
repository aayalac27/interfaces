import streamlit as st
from PIL import Image

st.title("mi primera app!")

st.header("en este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("faclmente puedo realizar backend y frontend")
image = Image.open('image.jpeg')

st.image(image, caption="ggg")
