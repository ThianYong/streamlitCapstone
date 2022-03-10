# Load important libraries 
import pandas as pd
import streamlit as st 
import os

#@st.cache
def app():
    """ what is this page for??
    """
    st.title('Page 3')

    st.write('# This is a Page for Project Secret!')
    st.write('## This is Page 03')
    st.markdown(
    """
    Try only, do not follow. 
    Today is 4 March 2022
    """
    )

    """ Test code for ETH """
    st.write('## ETH Data')

    d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p')
    df = pd.read_csv('../Project/data/ETH_1h.csv', parse_dates=['Date'], date_parser=d_parser, index_col='Date')

    st.write('## Close, High, Low, Volume - ETH')

    df_plot = df.resample('W').agg({'Close': 'mean', 'High':'max', 'Low': 'min'})
    chart = st.line_chart(df_plot)

