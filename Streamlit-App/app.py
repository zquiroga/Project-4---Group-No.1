import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

# Configuración de la página
st.set_page_config(
    page_title="Vehicle Price Prediction",
    page_icon="🚗",
)

# Selección de la página
page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

# Cambiar el ícono y el texto del sidebar según la página seleccionada
if page == "Predict":
    st.sidebar.markdown("🚗", unsafe_allow_html=True)
    st.sidebar.write("Vehicle Price Prediction")
else:
    st.sidebar.markdown("📈",unsafe_allow_html=True)
    st.sidebar.write("Distribution of vehicles by state")
    st.sidebar.write("Mean Price Based On State")
    st.sidebar.write("Mean Price Based On Year")

# Mostrar la página correspondiente
if page == "Predict":
    show_predict_page()
else:
    show_explore_page()




