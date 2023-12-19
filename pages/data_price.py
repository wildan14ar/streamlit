import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

sheet_id = "11RwSeez-R99Zx9iek69GRjsiDV2jMLDPu4CmyexoXMM"
sheet_name = "price"
url2 = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name }"

df = pd.read_csv(url2)
st.header("Prediksi harga rumah")

gk=pd.DataFrame({'pil':["Preprosesing", "Analyst", "Modelling", "Prediksi"]})
cfd=st.sidebar.selectbox('Please select:', gk['pil'])
if cfd == "Preprosesing":
    st.subheader("Preprosessing data:")
    st.dataframe(df.head())
    code = '''df.dtypes'''
    st.code(code, language='python')
    st.text(df.dtypes)
    code = '''df.isnull().sum()'''
    st.code(code, language='python')
    st.text(df.isnull().sum())
    df = df.dropna()
    code = '''df = df.dropna() 
df.isnull().sum()
df.head()'''
    st.code(code, language='python')
    st.text(df.isnull().sum())
    st.dataframe(df.head())

if cfd == "Analyst":
    st.subheader("Analyst visual data")


if cfd == "Modelling":
   st.subheader("The number of rentals based on the Season")

if cfd == "Prediksi" :
   st.subheader("The number of rentals based on the Season")