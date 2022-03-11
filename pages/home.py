import streamlit as st
import numpy as np
import pandas as pd
st.set_page_config(layout="wide") # set layout to wide for all pages

#@st.cache
def app():
    """
    What is this page for?
    """

    url = 'https://raw.githubusercontent.com/ThianYong/streamlitCapstone/main/data/'
    # url = '../Project/data/'

    st.title('HOME') #set the title

    st.write('# This is a Page for Project Secret!')
    st.write('## This is The Home Page')
    st.markdown(
    """
    Explain the project here
    """
    )

