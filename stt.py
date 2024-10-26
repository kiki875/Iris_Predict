import streamlit as st 
import pandas as pandas
import pickle

st.title('Iris Prediction')
st.write('My first Streamlit App')

sl = float(st.number_input('Enter Sepal Length'))
sw = float(st.number_input('Enter Sepal Width'))
pl = float(st.number_input('Enter Petal Length'))
pw = float(st.number_input('Enter Petal Width'))

if st.button('Predict?'):
    st.write('Processing ..... ')
    with open('model_iris.pkl','rb') as model:
        pred_model = pickle.load(model)
    pred_value = pred_model.predict([[sl,sw,pl,pw]])
    st.write(f'The Predicted Species is {pred_value}')