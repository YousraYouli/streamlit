import streamlit as st
import pandas as pd
import numpy as np


df=pd.read_csv('usa_companies.csv')
st.write(df)
dd=pd.DataFrame(
    np.random.randn(20,3),
    columns=["a","b","c"]
)
st.bar_chart(dd)
st.line_chart(dd)