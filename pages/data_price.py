import streamlit as st
import pandas as pd
import numpy as np

sheet_id = "11RwSeez-R99Zx9iek69GRjsiDV2jMLDPu4CmyexoXMM"
sheet_name = "price"
url2 = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name }"

df = pd.read_csv(url2)
st.dataframe(df.head())