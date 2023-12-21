import streamlit as st
import pandas as pd
import pickle

st.write("# Simple Advertising Prediction App") #write title
st.write("This app predicts the **Sales** type!") #write as subtitle

st.sidebar.header('User Input Parameters') #to create sidebar

def user_input_features():
    TV = st.sidebar.slider('TV', 0.70, 296.40, 149.75) #st.slider : element of interaction (name of sidebar, minimum value, maximum value, default) #sepal_length = variable
    Radio = st.sidebar.slider('Radio', 0.00, 36.52, 22.90)
    Newspaper = st.sidebar.slider('Newspaper', 0.30, 45.10, 25.75)
    data = {'TV': TV, 
            'Radio': Radio,
            'Newspaper': Newspaper}
    return data

df = user_input_features()
file_path = "AdvertisingANN.h5"

try:
    with open(file_path, "rb") as file:
        loaded_model = pickle.load(file)

input_data = pd.DataFrame(df, index=[0])

                          input_data['MissingFeature'] = 0

prediction = loaded_model.predict(input_data.values)
st.subheader('User Input parameters') #alternate function untuk subheader
st.write(df)

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)
