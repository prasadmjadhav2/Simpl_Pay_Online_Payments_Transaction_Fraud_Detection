import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('pay_fraud_predictor.pkl','rb'))

st.title('Online Payments Transaction Fraud Detection')

st.write('Enter The Transaction Details')

step = st.number_input('Enter the Step:', min_value=0, step=1)
payment_type = st.number_input('Enter the Payment Type:', min_value=0, step=1)
amount = st.number_input('Enter the Amount:', min_value=0.0, step=0.01)
oldbalance_org = st.number_input('Enter the Old Balance Org:', min_value=0.0, step=0.01)
newbalance_orig = st.number_input('Enter the New Balance Orig:', min_value=0.0, step=0.01)
oldbalance_dest = st.number_input('Enter the Old Balance Dest:', min_value=0.0, step=0.01)
newbalance_dest = st.number_input('Enter the New Balance Dest:', min_value=0.0, step=0.01)

input_point = np.array([[step, payment_type, amount, oldbalance_org, newbalance_orig, oldbalance_dest, newbalance_dest]])

if st.button('Predict'):
    prediction = model.predict(input_point)
    
    if prediction[0] == 0:
        st.success('Your Transaction is Non-Frauded ✔️ (Authorised)')
    else:
        st.error('Your Transaction is Frauded ✖️ (Unauthorised)')