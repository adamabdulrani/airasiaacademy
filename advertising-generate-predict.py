import streamlit as st
import pandas as pd
import seaborn as sns
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

st.write("# Simple Advertising Prediction App") #write title
st.write("This app predicts the **Sales** type!") #write as subtitle

st.sidebar.header('User Input Parameters') #to create sidebar

def user_input_features():
    sepal_length = st.sidebar.slider('TV', 0.70, 296.40, 149.75) #st.slider : element of interaction (name of sidebar, minimum value, maximum value, default) #sepal_length = variable
    sepal_width = st.sidebar.slider('Radio', 0.00, 36.52, 22.90)
    petal_length = st.sidebar.slider('Newspaper', 0.30, 45.10, 25.75)
    data = {'TV': TV, 
            'Radio': Radio,
            'Newspaper': Newspaper}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters') #alternate function untuk subheader
st.write(df)

loaded_model = pickle.load(open("AdvertisingANN.h5", "rb"))
prediction = AdvertisingANN.predict(df)

st.subheader('Prediction')
st.write(prediction)
