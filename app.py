import streamlit as st
from PIL import Image

st.title("mi primera app!")

st.header("en este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")
st.write("faclmente puedo realizar backend y frontend")
image = Image.open('image.jpeg')

st.image(image, caption="Polos opuestos")


texto = st.text_input("sisas la k")
st.write("la cara del trap de medallo")

st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col2:
  st.subheader("Segunda columna")
  modo = st.radio("Que modalidad es la principal en tu interfaz", ("Visual","Auditiva","Táctil"))
  if modo == "Visual":
    st.write("La vista es fundamental para tu interfaz")
  if modo == "Auditivo":
    st.write("La audición es fundamental para tu interfaz")
if modo == "Táctil":
    st.write("El tacto es esencial para tu interfaz")


st.subheader("Uso de Botones")
if st.button('Presiona el botón'):
    st.write('Gracias por presionar')
else:
    st.write('No has presionado aún')

st.subheader("Selectbox")
in_mod = st.selectbox(
  "Selecciona la modalidad",
  ("Audio", "Visual", "Háptico"),
)
if in_mod == "Audio":
    set_mod = "Reproducir audio"
elif in_mod == "Visual":
    set_mod = "Reproducir video"
elif in_mod == "Háptico":
    set_mod = "Activar vibración"
st.write(" La acción es:", set_mod)


with st.sidebar:
  st.subheader("Configura la modalidad")
  mod_radio = st.radio(
    "Escoge la modalidad a usar",
    ("Visual", "Auditiva", "Háptica")
  )
