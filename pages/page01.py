import streamlit as st
import numpy as np
import pandas as pd
from annotated_text import annotated_text


#@st.cache
def app():
    """
    What is this page for?
    """

    url = 'https://raw.githubusercontent.com/ThianYong/streamlitCapstone/main/data/'
    # url = '../Project/data/'

    st.title('Page 01') #set the title

    st.write('# This is a Page for Project Secret!')
    st.write('## This is The Home Page')
    st.markdown(
    """
    Explain the project here..
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

    ### Set Data Set path
    url = 'https://raw.githubusercontent.com/ThianYong/streamlitCapstone/main/data/'
    # url = '../streamlitCapstone/data/'
    url_csv = url + '06_experiment_logs_L8_J-5.csv'

    df = pd.read_csv(url_csv)
    st.dataframe(data=df)
    chart = st.line_chart(df)


    def pretty(s: str) -> str:
        try:
            return dict(js="JavaScript")[s]
        except KeyError:
            return s.capitalize()
    @st.cache
    def get_data():
        df = pd.read_csv(url_csv)
        df["num"] = df.num.map(pretty)
        return df

    # df = get_data()

    st.header("Plot 1")

    all_num = df.num.unique().tolist()
    nums = st.multiselect(
        "Numbers", options=all_num, default=all_num
    )
    plot_df = df[df.num.isin(nums)]
    # plot_df["std_mean"] = plot_df


