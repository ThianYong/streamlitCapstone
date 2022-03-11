# Import necessary libraries

import pandas as pd
import streamlit as st
import webbrowser


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

