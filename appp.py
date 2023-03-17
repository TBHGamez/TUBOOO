import pickle
import streamlit as st
import numpy as np

model = pickle.load(open('model.pickle', "rb"))
st.balloons()
st.title('Revenue Prediction')
x = st.number_input('Input Temperature')

if st.button('Predict'):
    x = np.array(x).reshape(-1,1)
    res = model.predict(x)
    st.caption('Revenue Prediction')
    kq = res[0]
    st.success(f'kq')
