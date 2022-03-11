import streamlit as st
import numpy as np
import pandas as pd

#@st.cache
def app():
    """
    What is this page for?
    """
    url = 'https://raw.githubusercontent.com/ThianYong/streamlitCapstone/main/data/'
    # url = '../Project/data/'

    st.title('Page 1') #set the title

    st.write('# This is a Page for Project Secret!')
    st.write('## This is Page 01')
    st.markdown(
        """
        This page demostrate the graph plots.
        user can zoom in and out. 
        """
    )

    """ Test code for ETH """
    st.write('## ETH Data')

    d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p')
    # df = pd.read_csv('../Project/data/ETH_1h.csv', parse_dates=['Date'], date_parser=d_parser, index_col='Date')
    df = pd.read_csv(url + 'ETH_1h.csv', parse_dates=['Date'], date_parser=d_parser, index_col='Date')

    st.write('## Highest - ETH')
    highs = df['High'].resample('D').max()
    highs['2020-01-01']
    chart = st.line_chart(highs)