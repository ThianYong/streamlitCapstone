# Load important libraries 
import pandas as pd
import streamlit as st 
import os

#@st.cache
def app():
    """ what is this page for??
    """

    url = 'https://raw.githubusercontent.com/ThianYong/streamlitCapstone/main/data/'
    # url = '../Project/data/'

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
    df = pd.read_csv(url + 'ETH_1h.csv', parse_dates=['Date'], date_parser=d_parser, index_col='Date')

    st.write('## Close, High, Low, Volume - ETH')

    df_plot = df.resample('W').agg({'Close': 'mean', 'High':'max', 'Low': 'min'})
    chart = st.line_chart(df_plot)

    ### Set Data Set path
    # url = '../streamlitCapstone/data/'
    url_csv = url + 'ETH_1h.csv'

    st.markdown(
        """
        Plotting
        """
    )


    st.write('Get Data Using @st.cache')
    @st.cache
    def get_data():
        df = pd.read_csv(url_csv, parse_dates=['Date'], date_parser=d_parser, index_col='Date')
        return df

    df = get_data()
    st.dataframe(data=df)
    st.header("Plot 1")
    df = df.resample('W').agg({'Close': 'mean', 'High':'max', 'Low': 'min'})
    chart1 = st.line_chart(df)




