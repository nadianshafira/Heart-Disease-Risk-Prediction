import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from phik.report import plot_correlation_matrix
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Welcome to Exploration Data Analysis')
#Memanggil data csv 
    df= pd.read_csv('P1M2_nadia_nabilla.csv')

#menampilakn 5 data teratas
    st.table(df.head(5))


#menampilkan label Hear_Disease
    st.title('Number of People Diagnosed and Not Diagnosed with Heart Disease')
    image1 = Image.open('pict1.png')
    st.image(image1, caption='figure 1')

#menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Berdasarkan bar chart di atas, dapat dilihat bahwa dari 308774 data, terdapat 283803 orang memiliki tidak mengidap penyakit jantung (91.9%), dan 24971 lainnya mengidap penyakit jantung (8.1%). Perbandingan antara orang yang mengidap penyakit jantung dan tidak mengidap penyakit cukup jauh, hal ini mengindikasikan data yang dimiliki imbalanced.')

    st.title('Correlation Matrix')
    image2 = Image.open('pict2.png')
    st.image(image2, caption='figure 2')

#menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Berdasarkan matriks korelasi di atas, `FriedPotato_Consumption`, `Green_Vegetables_Consumption`, `Fruit_Consumption`, `BMI`, `Weight`, `Height`, `Depression`, dan `Checkup` tidak memiliki korelasi dengan diagnosis seseorang mengidap penyakit jantung atau tidak.')