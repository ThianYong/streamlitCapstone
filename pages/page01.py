import streamlit as st
import numpy as np
import pandas as pd

#@st.cache
def app():
    url = 'https://raw.githubusercontent.com/ThianYong/streamlitCapstone/main/data/'
    # url = '../Project/data/'
    """
    What is this page for?
    """
    st.title('HOME') #set the title

    st.write('# This is a Page for Project Secret!')
    st.write('## This is The Home Page')
    st.markdown(
        """
        Explain the project here
        """
    )