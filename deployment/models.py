import streamlit as st
import pandas as pd
import pickle
from PIL import Image

def run():

    # load model
    with open('best_svm.pkl', 'rb') as model:
        svm_model = pickle.load(model)

    General_Health = st.selectbox('General Health', options=['Poor', 'Fair', 'Good', 'Very Good', 'Excellent'])
    Exercise = st.selectbox('Exercise', options=['Yes', 'No'])
    Skin_Cancer = st.selectbox('Skin Cancer', options=['Yes', 'No'])
    Other_Cancer = st.selectbox('Other Cancer', options=['Yes', 'No'])
    Diabetes = st.selectbox('Diabetes', options=['Yes', 'No'])
    Arthritis = st.selectbox('Arthritis', options=['Yes', 'No'])
    Sex = st.selectbox('Sex', options=['Male', 'Female'])
    Age_Category = st.selectbox('Age Category', options=['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80+'])
    BMI = st.number_input('BMI', min_value=0.0, max_value=100000.00)
    Smoking_History = st.selectbox('Smoking History', options=['Yes', 'No'])
    Alcohol_Consumption = st.number_input('Alcohol Consumption', min_value=0.0, max_value=100000.00)


    st.markdown('**In the following is the result of the data you have input:**')
    

    dataInf = pd.DataFrame({
        'General_Health': General_Health,
        'Exercise': Exercise,
        'Skin_Cancer': Skin_Cancer,
        'Other_Cancer': Other_Cancer,
        'Diabetes': Diabetes,
        'Arthritis': Arthritis,
        'Sex': Sex,
        'Age_Category': Age_Category,
        'BMI': BMI,
        'Smoking_History': Smoking_History,
        'Alcohol_Consumption': Alcohol_Consumption
    }, index=[0])

    st.table(dataInf)


    if st.button(label='Predict'):
        # data dummy prediction
        yPred_inf = svm_model.predict(dataInf)

        # result of prediction
        if yPred_inf[0] == 0:
            st.write('Tidak Mengidap Penyakit Jantung')

        else:
            st.write('Mengidap Penyakit Jantung')
