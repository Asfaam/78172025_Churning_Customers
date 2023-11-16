# Import libraries
import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('churn_model.h5')

def main():
    # Set page config to wider layout and give some padding
    st.set_page_config(layout="wide")
    st.markdown(
        """
        <style>
            .main {
                padding: 8px;
                color: maroon;
            }
            .st-bw {
                background-color:  orange;
                color: white;
                padding: 12px;
                border-radius: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.title("Customer Churn Predictor")
    st.markdown("""
        :dart: Use this predictor app to predict customer churn
    """)
    st.warning("Provide customer details for prediction.")

    # The input field for user features
    Gender = st.selectbox('Select gender:', ['female', 'male'])
    SeniorCitizen = st.selectbox('Is the customer a SeniorCitizen :', [0, 1])
    Partner = st.selectbox('Does the customer have a Partner:', ['yes', 'no'])
    PaperlessBilling = st.selectbox('Does the customer use PaperlessBilling:', ['yes', 'no'])
    OnlineSecurity = st.selectbox('Does the customer have OnlineSecurity:', ['yes', 'no'])
    TechSupport = st.selectbox('Does the customer have: TechSupport', ['yes', 'no'])
    OnlineBackup = st.selectbox('Does the customer have OnlineBackup:', ['yes', 'no'])
    DeviceProtection = st.selectbox('Does the customer have DeviceProtection:', ['yes', 'no'])
    Dependents = st.selectbox('Does the customer have any Dependents:', ['yes', 'no'])

    # Convert categorical values to numerical values
    Gender = 1 if Gender == 'male' else 0
    Partner = 1 if Partner == 'yes' else 0
    PaperlessBilling = 1 if PaperlessBilling == 'yes' else 0
    OnlineSecurity = 1 if OnlineSecurity == 'yes' else 0
    TechSupport = 1 if TechSupport == 'yes' else 0
    OnlineBackup = 1 if OnlineBackup == 'yes' else 0
    DeviceProtection = 1 if DeviceProtection == 'yes' else 0
    Dependents = 1 if Dependents == 'yes' else 0
    

    # Convert "InternetService" input to a numerical value
    InternetService_mapping = {'DSL': 0, 'Fiber optic': 1, 'no': 2}
    InternetService = st.selectbox('Select Internet Service:', list(InternetService_mapping.keys()))
    InternetService = InternetService_mapping[InternetService]

    # Convert "PaymentMethod" input to a numerical value
    PaymentMethod_mapping = {'Bank transfer (automatic)': 0, 'Credit card (automatic)': 1, 'Electronic check': 2, 'Mailed check':3}
    PaymentMethod = st.selectbox('Select PaymentMethod:', list(PaymentMethod_mapping.keys()))
    PaymentMethod = PaymentMethod_mapping[PaymentMethod]

    # Convert "Contract" input to a numerical value
    contract_mapping = {'month-to-month': 0, 'one_year': 1, 'two_years': 2}
    Contract = st.selectbox('Select Contract duration:', list(contract_mapping.keys()))
    Contract = contract_mapping[Contract]
    
    Tenure = st.number_input('Select number of months the customer has been with the company:', min_value=0, max_value=240, value=0)
    MonthlyCharges = st.number_input('Select MonthlyCharges:', min_value=0, max_value=1000000, value=0)
    TotalCharges = Tenure * MonthlyCharges

    # Display TotalCharges
    st.warning(f'TotalCharges: {TotalCharges}')


    #  Make prediction; by clicking the prediction button
    if st.button('Predict'):
        predictions = model.predict([[MonthlyCharges, TotalCharges, Tenure, Contract, PaymentMethod, InternetService, Gender, PaperlessBilling, OnlineSecurity, Partner, TechSupport, OnlineBackup, SeniorCitizen, DeviceProtection, Dependents]])
        prediction = np.round(predictions[0],2)
        st.success(f"Predict Churn : {prediction}")

        # Based on the prediction, make a comment whether the customer will churn or not.
        if prediction >= 0.5:
            st.warning("Yes, customer will most likely churn.")
        else:
            st.warning("No, customer will not churn.")

        # confidence factor
        confidence_factor = 2.58 * np.sqrt((prediction * (1 - prediction)) / 1) 
        st.write(f"Confidence Factor: {confidence_factor}")


if __name__ == "__main__":
    main()