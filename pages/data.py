import streamlit as st
import numpy as np
import pandas as pd
import plotly.figure_factory as ff

#@st.cache
def app():
    """
    What is this page for?
    """
    url = 'https://raw.githubusercontent.com/ThianYong/streamlitCapstone/main/data/'
    # url = '/Users/thianyong/Library/Mobile Documents/com~apple~CloudDocs/Master Study/NUS/Capstone/Project/Capstone Codes/streamlitCapstone/data/'

    st.title('Application with Ising Model and Experiment Logs') #set the title


    st.write('#')
    st.markdown(
    """
    We use the **MAPALUS** library for the application to find the ground state of Ising model.
    The logs shown below are on google colab.
    """
    )

    st.write('### Server Specifications')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('CPU',"Intel Xeon")
        st.metric('CPU Speed',"2.20GHz")

    with col2:
        st.metric('L1 Cache', '32K')
        st.metric('L2 Cache', '256K')
    with col3:
        st.metric('Memory','12.69GB')
        st.metric('Disk','107.72GB')


    ''' Plot the distribution of time consumed. Read in the data '''
    # cols_filt = ['num', 'epoch', 'time', 'J', 'length']
    df_4 = pd.read_csv(url + 'MLP_combined_length_4.csv') #, usecols=cols_filt)
    df_8 = pd.read_csv(url + 'MLP_combined_length_8.csv') #, usecols=cols_filt)
    # chart = st.line_chart(df)

    hist_data = [df_4['time'], df_8['time']]
    group_labels = ['Length = 4', 'Length = 8']
    fig = ff.create_distplot(hist_data, group_labels)
    fig.update_layout(title='Distribution Plot on Time(sec) Taken for Each Iteration for Different Sizes')

    st.plotly_chart(fig, use_container_width=True)
    if st.checkbox('Show Raw Data of Dist Plot Above'):
        df = pd.concat([df_4, df_8], ignore_index=True, sort=False)
        st.dataframe(data=df)