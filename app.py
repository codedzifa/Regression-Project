import os
import joblib
import pickle
import numpy as np
import pandas as pd
import streamlit as st
!pip install streamlit


# Useful functions
def load_ml_components(fp):
    "Load the ml components to re-use in app"
    with open(fp, "rb") as f:
        object = pickle.load(f)
        return object


# interface
with st.sidebar:
    st.markdown("# Hi")
    st.markdown("# Welcome. This app is on time series forecasting")

st.title('Sales Prediction in Favorita Stores')

st.subheader('Using Time Series Forecasting')

# Add some text
st.write("""Welcome to Favorita Corporation, an Ecuadorian company which engages in the development and investment of commercial, industrial, and real estate ventures. Its subsidiaries operate in six countries within the region, namely Panama, Paraguay, Peru, Colombia, Costa Rica, and Chile. The company is committed to delivering top-notch products, services, and experiences in a manner that is both efficient and environmentally responsible, aiming to enhance the overall quality of life.


         
         Please ENTER the relevant data and CLICK Predict.
         
         """)


# Input
# input_data = {}
# col1,col2,col3 = st.columns(3)
# with col1:Products
#     input_data['store_nbr'] = st.slider("Store Number",0,54)
#     input_data['products'] = st.selectbox(" Family", ['OTHERS', 'CLEANING', 'FOODS', 'STATIONERY', 'GROCERY', 'HARDWARE',
#        'HOME', 'CLOTHING'])
#     input_data['onpromotion'] =st.number_input("Discount Amt On Promotion",step=1)
#     input_data['state'] = st.selectbox("State", ['Pichincha', 'Cotopaxi', 'Chimborazo', 'Imbabura',
#        'Santo Domingo de los Tsachilas', 'Bolivar', 'Pastaza',
#        'Tungurahua', 'Guayas', 'Santa Elena', 'Los Rios', 'Azuay', 'Loja',
#        'El Oro', 'Esmeraldas', 'Manabi'])
# with col2:
#     input_data['store_type'] = st.selectbox("Store Type",['D', 'C', 'B', 'E', 'A'])
#     input_data['cluster'] = st.number_input("Cluster",step=1)
#     input_data['dcoilwtico'] = st.number_input("DCOILWTICO",step=1)
#     input_data['year'] = st.number_input("Year to Predict",step=1)
# with col3:
#     input_data['month'] = st.slider("Month",1,12)
#     input_data['day'] = st.slider("Day",1,31)
#     input_data['dayofweek'] = st.number_input("Day of Week,0=Sunday and 6=Satruday",step=1)
#     input_data['end_month'] = st.selectbox("Is it End of the Month?",['True','False'])
store_nbr = st.slider("Enter store nbr", 0, 54)
products = st.selectbox(" Family", ['OTHERS', 'CLEANING', 'FOODS', 'STATIONERY', 'GROCERY', 'HARDWARE',
                                    'HOME', 'CLOTHING'])
onpromotion = st.number_input(
    "Discount Amt On Promotion_Expressed in Percentage %", step=1)
state = st.selectbox("State", ['Choose a State', 'Pichincha', 'Cotopaxi', 'Chimborazo', 'Imbabura',
                               'Santo Domingo de los Tsachilas', 'Bolivar', 'Pastaza',
                               'Tungurahua', 'Guayas', 'Santa Elena', 'Los Rios', 'Azuay', 'Loja',
                               'El Oro', 'Esmeraldas', 'Manabi'])

store_type = st.selectbox(
    "Store Type", ['Choose Store Type', 'D', 'C', 'B', 'E', 'A'])
Cluster = st.number_input("Cluster", step=1)
dcoilwtico = st.number_input("DCOILWTICO", step=1)
year = st.number_input("Year to Predict", step=1)

month = st.slider("Month", 1, 12)
day = st.slider("Day", 1, 31)
dayofweek = st.number_input("Day of Week,0=Sunday and 6=Satruday", step=1)


# prediction executed
if st.button("Predict"):

    # Dataframe creation
    df = pd.DataFrame(
        {
            "store_nbr": [store_nbr],  "products": [products], "onpromotion": [onpromotion], "state": [state], "store_type": [store_type],
            "Cluster": [Cluster], "dcoilwtico": [dcoilwtico], "year": [year], "month": [month], "day": [day], "dayofweek": [dayofweek],

        }
    )
    print(f"[Info] Input data as dataframe:\n{df.to_markdown()}")

    st.text(f"The Predicted Sales: '{''}'.")
