# Importing libraries
import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Creating functions for models
# Function for Decision Tree Regressor Model
def load_model():
    with open('../Pickle-files/saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

dec_tree_reg = data["model"]
le_brand = data["le_brand"]
le_model = data["le_model"]
le_used = data["le_used"]
le_transmission = data["le_transmission"]
le_state = data["le_state"]

#Function for Random Forest Regressor Model
def random_forest():
   with open('../Pickle-files/random_model_steps.pkl', 'rb') as file:
    data_1 = pickle.load(file)
    return data_1

data_1 = random_forest()

random_forest_reg = data_1["model"]

# Creating function to show the prediction page of the website
def show_predict_page():
    st.title("Vehicle Price Prediction")

    st.write("""### We need some information to predict the price of the vehicle""")

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

    # Getting values for organise brand and model menus
    car_data = pd.read_csv("../Resources/unique_brands.csv")

    df = pd.DataFrame(car_data)

    def filter_models_by_brand(selected_brand):
        # Filter models based on the selected brand
        filtered_models = df[df['Brand'] == selected_brand]['Model'].unique()
        return filtered_models

    used_new = (
        "USED",
        "NEW"
    )

    transmissions = (
        "Automatic",
        "Manual"
    )

    selected_brand = st.selectbox("Select Brand", df['Brand'].unique())

    # Use the selected brand to filter models
    filtered_models = filter_models_by_brand(selected_brand)

    # Selectbox for choosing the model (filtered based on the selected brand)
    selected_model = st.selectbox("Select Model", filtered_models)

    state = st.selectbox("State", states)
    used = st.selectbox("Used or New type", used_new)
    transmission = st.selectbox("Transmission", transmissions)

    litres = st.slider("Engine", min_value=0.7, max_value=6.8, value=1.3, step=0.1)

    kilometres = st.number_input("Enter odometer value:", min_value=0, step=1, value=150000)
    year = st.number_input("Enter the year of manufacture:", min_value=1900, max_value=2050, step=1, value=2010)

    ok = st.button("Calculate Vehicle Price")
    if ok:
        X = np.array([[selected_brand, year, selected_model, used, transmission, kilometres, state, litres]])
        X[:, 0] = le_brand.transform(X[:,0])
        X[:, 2] = le_model.transform(X[:,2])
        X[:, 3] = le_used.transform(X[:,3])
        X[:, 4] = le_transmission.transform(X[:,4])
        X[:, 6] = le_state.transform(X[:,6])        
        X = X.astype(float)

        y_pred = dec_tree_reg.predict(X)
        y_pred_1 = random_forest_reg.predict(X)
        st.subheader(f"The estimated price of the vehicle using a Decision Tree Regressor Model is ${y_pred[0]:.2f}")
        st.subheader(f"The estimated price of the vehicle using a Random Forest Regressor Model is ${y_pred_1[0]:.2f}")

show_predict_page()