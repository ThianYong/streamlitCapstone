import streamlit as st
import numpy as np
import pandas as pd
st.set_page_config(layout="wide") # set layout to wide for all pages

#@st.cache
def app():
    """
    What is this page for?
    """
    st.title('Page 1') #set the title

    st.write('# This is a Page for Project Secret!')
    st.write('## This is Page 01')
    st.markdown(
    """
    Try only, do not follow. 
    Today is 4 March 2020
    """
    )

    """ Test code for ETH """
    st.write('## ETH Data')

    d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p')
    df = pd.read_csv('https://raw.githubusercontent.com/ThianYong/streamlitCapstone/main/data/ETH_1h.csv', parse_dates=['Date'], date_parser=d_parser, index_col='Date')

    st.write('## Highest - ETH')
    highs = df['High'].resample('D').max()
    highs['2020-01-01']
    chart = st.line_chart(highs)
