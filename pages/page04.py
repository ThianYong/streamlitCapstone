import streamlit as st


def app():
    """
    What is this page for?
    """
    st.title('Page 4') #set the title


    st.write('# This is a Page for Project Secret!')
    st.write('## This is Page 04')
    st.markdown(
        """
        Try only, do not follow. 
        Today is 4 March 2020
        """
    )
    st.markdown("[Section 4](#section-4)", unsafe_allow_html=True)




        