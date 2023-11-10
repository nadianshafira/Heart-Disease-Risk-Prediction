import streamlit as st
import eda
import models


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediksi'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.write('')
    st.write('Milestone 2')
    st.write('Nama      : Nadia Nabilla')
    st.write('Batch     : HCK - 009')
    st.write('Objectives: Project ini bertujuan untuk memprediksi apakah seseorang mengidap penyakit jantung atau tidak berdasarkan beberapa faktor menggunakan SVM.')
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('Untuk memprediksi apakah seseorang mengidap penyakit jantung atau tidak, dapat dilakukan dengan membangun model. Pada project ini, prediksi akan dilakukan dengan beberapa model (KNN, SVM, Decision Tree, Random Forest, AdaBoosting) dan nantinya akan dipilih 1 model terbaik.')

    with st.expander("Kesimpulan"):
        st.caption('Setelah melakukan pemodelan untuk memprediksi apakah seseorang mengidap penyakit jantung atau tidak dengan beberapa model, diperoleh 1 model terbaik, yaitu SVM. Kemudian untuk mendapatkan performa model SVM yang lebih baik, dilakukan hyperparameter tuning untuk mengetahui hyperparameter apa saja yang digunakan. Dan diketahui model SVM yang terbaik dalam memprediksi seseorang mengidap penyakit jantung atau tidak adalah model SVM dengan `kernel = RBF`, `C = 0.1`, `coef0 = 0.1`, dan `gamma = 0.1`.')

elif page == 'Exploration Data Analysis':
    eda.run()
else:
    models .run()