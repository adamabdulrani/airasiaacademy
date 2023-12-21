import streamlit as st
import pandas as pd
import pickle
import os

# Function to get user input features
def user_input_features():
    TV = st.sidebar.slider('TV', 0.70, 296.40, 149.75)
    Radio = st.sidebar.slider('Radio', 0.00, 36.52, 22.90)
    Newspaper = st.sidebar.slider('Newspaper', 0.30, 45.10, 25.75)
    data = {'TV': TV, 'Radio': Radio, 'Newspaper': Newspaper}
    return data

# Main Streamlit app
def main():
    st.write("# Simple Advertising Prediction App")
    st.write("This app predicts the **Sales** type!")

    st.sidebar.header('User Input Parameters')

    # Get user input
    df = user_input_features()

    # Model loading and prediction
    file_path = "AdvertisingANN.h5"  # Assuming it's a Pickle file
    try:
        with open(file_path, "rb") as file:
            loaded_model = pickle.load(file)

        # Create DataFrame for input data
        input_data = pd.DataFrame(df, index=[0])

        # Prediction
        prediction = loaded_model.predict(input_data.values)

        # Display results
        st.subheader('User Input parameters')
        st.write(df)

        st.subheader('Prediction')
        st.write(prediction)

    except FileNotFoundError:
        st.error(f"Model file {file_path} not found. Please check the file path.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

    # Debugging information
    st.write("Current working directory:", os.getcwd())
    st.write("List of files in the directory:", os.listdir())

if __name__ == "__main__":
    main()
