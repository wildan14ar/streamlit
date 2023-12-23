import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sheet_id = "11RwSeez-R99Zx9iek69GRjsiDV2jMLDPu4CmyexoXMM"
sheet_name = "price"
url2 = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name }"

df = pd.read_csv(url2)
st.header("Prediksi harga rumah")

gk=pd.DataFrame({'pil':["Preprosesing", "Analyst", "Modelling", "Prediksi"]})
cfd=st.sidebar.selectbox('Please select:', gk['pil'])
if cfd == "Preprosesing":
    st.subheader("Preprosessing data:")
    code = '''
df.head() # Menampilkan 5 data pertarma
df.info()
'''
    st.code(code, language='python')
    st.dataframe(df.head())
    st.write(df.info())
    code = '''df.dtypes'''
    st.code(code, language='python')
    st.text(df.dtypes)
    code = '''df.isnull().sum()'''
    st.code(code, language='python')
    st.text(df.isnull().sum())
    df = df.dropna()
    code = '''
df = df.dropna() 
df.isnull().sum()
df.head() # Menampilkan 5 data pertarma
'''
    st.code(code, language='python')
    st.text(df.isnull().sum())
    st.dataframe(df.head())

if cfd == "Analyst":
    st.subheader("Analyst visual data")
    df = df.dropna()
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total rumah",  df['Observation'].count())
    col2.metric("Builtup", round(df['Builtup'].mean()))
    col3.metric("Carpet", round(df['Carpet'].mean()))
    col4.metric("House Price", round(df['House_Price'].mean()))
    st.dataframe(df.head())
    fig, ax = plt.subplots()
    ax.bar(df['City_Category'], df['House_Price'])
    ax.set_xlabel('City Category')
    ax.set_ylabel('House Price')
    st.pyplot(fig)

    
    


if cfd == "Modelling":
   st.subheader("The number of rentals based on the Season")

if cfd == "Prediksi" :
   st.subheader("The number of rentals based on the Season")