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
    st.title('Experiments Logs Page') #set the title


    st.write('# This Page Shows the Experiment Logs')
    st.markdown(
        """
        Describe the Data here.
        
        """
    )
    ''' Read in the data '''
    data = pd.read_csv(url + 'logs.csv')
    chart = st.line_chart(data)

    if st.checkbox('Show Raw Data'):
        st.dataframe(data=data)