# Import necessary libraries

import pandas as pd
import streamlit as st
import webbrowser
from PIL import Image


def app():
    """
    What is this page for?
    """
    st.title('Page 2') #set the title

    st.write('# This is a Page for Project Secret!')
    st.write('## This is Page 02')
    st.markdown(
        """
        This page is to demo different type of URL link.
        """
    )


    st.write('=== To open an URL, click this button ====')
    url1 = 'https://www.google.com'
    if st.button('Open Browser'):
        webbrowser.open_new_tab(url1)

    st.write('=== To open an URL, click this link ====')
    url2 = '[Google](https://www.google.com)'
    st.markdown(url2, unsafe_allow_html=True)

    st.write('=== Or this link ===')
    url3 = 'https://www.google.com'
    st.write('[Google](%s)' % url3)

    col1, col2 = st.columns(2)
    display = Image.open('images/image01.png')
    col1.header('Singapore Map')
    col1.image(display, use_column_width=True)

    col2.header('Details')
    col2.markdown(
    """
    Modern Singapore was founded in 1819 by Sir Stamford Raffles as a trading post of the British Empire. In 1867, the colonies in Southeast Asia were reorganised and Singapore came under the direct control of Britain as part of the Straits Settlements. During the Second World War, Singapore was occupied by Japan in 1942, and returned to British control as a separate crown colony following Japan's surrender in 1945. Singapore gained self-governance in 1959 and in 1963 became part of the new federation of Malaysia, alongside Malaya, North Borneo, and Sarawak. 
    Ideological differences led to Singapore being expelled from the federation two years later and it became an independent country.
    
    """
)

