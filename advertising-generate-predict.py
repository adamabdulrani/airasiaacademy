import streamlit as st
import pandas as pd
import pickle

st.write("# Simple Advertising Prediction App")  # Write title
st.write("This app predicts the **Sales** type!")  # Write as subtitle

st.sidebar.header('User Input Parameters')  # To create sidebar


def user_input_features():
    TV = st.sidebar.slider('TV', 0.70, 296.40, 149.75)  # st.slider: element of interaction (name of sidebar, minimum value, maximum value, default) #sepal_length = variable
    Radio = st.sidebar.slider('Radio', 0.00, 36.52, 22.90)
    Newspaper = st.sidebar.slider('Newspaper', 0.30, 45.10, 25.75)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper}
    return data


df = user_input_features()
file_path = "AdvertisingANN.pkl"  # Change file extension to .pkl

try:
    with open(file_path, "rb") as file:
        loaded_model = pickle.load(file)

    input_data = pd.DataFrame(df, index=[0])
    print(input_data)

    input_data['MissingFeature'] = 0  # Assuming this is a placeholder for a missing feature

    prediction = loaded_model.predict(input_data.values)
    st.subheader('User Input parameters')  # Alternate function for subheader
    st.write(df)

    st.subheader('Prediction')
    st.write(prediction)

except FileNotFoundError:
    st.error(f"Model file {file_path} not found.")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")
