import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

prediction_model = data["model"]
le_brand = data["le_brand"]
le_model = data["le_model"]
le_used = data["le_used"]
le_transmission = data["le_transmission"]
le_body_type = data["le_body_type"]
le_state = data["le_state"]

def show_predict_page():
    st.title("Vehicle Price Prediction")

    st.write("""### We need some information to predict the price of the vehicle""")

    brands = (
        "Audi",
        "BMW",
        "Ford",
        "GWM",
        "Holden",
        "Honda",
        "Hyundai",
        "Isuzu",
        "Jeep",
        "Kia",
        "Land",
        "Lexus",
        "Mazda",
        "Mercedes-Benz",
        "MG",
        "Mitsubishi",
        "Nissan",
        "Renault",
        "Subaru",
        "Suzuki",
        "Toyota",
        "Volkswagen"    
    )

    body_types = (
        "Commercial",
        "Convertible",
        "Coupe",
        "Hatchback",
        "People Mover",
        "Sedan",
        "SUV",
        "Ute / Tray",       
        "Wagon"
    )

    states = (
        "ACT",
        "NSW",
        "NT",
        "QLD",
        "SA",
        "TAS",
        "VIC",
        "WA"
    )

    models = (
        "Navara",
        "Convertible",
        "Coupe",
        "Hatchback",
        "People Mover",
        "Sedan",
        "SUV",
        "Ute / Tray",       
        "Wagon"
    )

    used_new = (
        "USED",
        "NEW"
    )

    transmissions = (
        "Automatic",
        "Manual"
    )

    brand = st.selectbox("Brand", brands)
    body_type = st.selectbox("Body type", body_types)
    state = st.selectbox("State", states)
    model = st.selectbox("Model", models)
    used = st.selectbox("Used or New type", used_new)
    transmission = st.selectbox("Transmission", transmissions)

    litres = st.slider("Litres of motor", 0.7, 6.8, 1.3)

    kilometres = st.number_input("Enter odometer value:", min_value=0, step=1)
    year = st.number_input("Enter the year of manufacture:", min_value=1900, max_value=2050, step=1)

    ok = st.button("Calculate Vehicle Price")
    if ok:
        X = np.array([[brand, year, model, used, transmission, kilometres, body_type, state, litres]])
        X[:, 0] = le_brand.transform(X[:,0])
        X[:, 2] = le_model.transform(X[:,2])
        X[:, 3] = le_used.transform(X[:,3])
        X[:, 4] = le_transmission.transform(X[:,4])
        X[:, 6] = le_body_type.transform(X[:,6]) 
        X[:, 7] = le_state.transform(X[:,7])        
        X = X.astype(float)

        y_pred = prediction_model.predict(X)
        st.subheader(f"The estimated price of the vehicle is ${y_pred[0]:.2f}")

show_predict_page()