import streamlit as st
import pandas as pd
import numpy as np

sheet_id = "1psNXpDTQVr_PrxGz3kRsW7N4NjHW6TXmGf_WpwLfmt0"
sheet_name = "kaggle_survey_2022_responses2"
url1 = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name }"

df = pd.read_csv(url1)
st.dataframe(df.head())