import streamlit as st
import numpy as np
import pandas as pd
import plotly.figure_factory as ff
import matplotlib
from matplotlib.backends.backend_agg import RendererAgg
import matplotlib.pyplot as plt


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

    @st.cache  ### use cache to buffer the data. Improve loading time.
    def get_data(filename):
        return pd.read_csv(url+filename)

    ''' Plot the distribution of time consumed. Read in the data '''
    # cols_filt = ['num', 'epoch', 'time', 'J', 'length']
    df_4 = get_data('MLP_combined_length_4.csv') #, usecols=cols_filt)
    df_8 = get_data('MLP_combined_length_8.csv') #, usecols=cols_filt)

    df = pd.concat([df_4, df_8], ignore_index=True, sort=False) ### combined all into 1 df.

    hist_data = [df_4['time'], df_8['time']]
    group_labels = ['Length = 4', 'Length = 8']
    fig = ff.create_distplot(hist_data, group_labels)
    fig.update_layout(title='Distribution Plot on Time(sec) Taken for Each Iteration for Different Sizes - MLP')

    st.plotly_chart(fig, use_container_width=True)
    if st.checkbox('Show Raw Data of Dist Plot Above'):
        st.dataframe(data=df)

    '''
    To display the Observables.
    '''
    st.write('### Benchmarking Parameters')
    col11, col12, col13 = st.columns(3)
    with col11:
        st.metric('J', "-5.0 to 5.0")
        st.metric('H', "1")

    with col12:
        st.metric('Iteration/J', '10')
        st.metric('Epoch Cap', '10,000')
    with col13:
        st.metric('Learning Rate', '0.001')
        st.metric('Stopping Threshold', '0.005')

    '''
    To Plot.
    '''
    filter_length = df['length'].unique().tolist()
    filter_J = df['J'].unique().tolist()
    filter_selected = st.multiselect('Choose the Length to Plot', filter_length, filter_length)

    matplotlib.use('agg')
    _lock = RendererAgg.lock ### use backend renderer to display graphs, more fluid.

    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((0.2, 1, .2, 1, .2))
    with row0_1, _lock:
        st.header("Length")
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.pie(filter_length, wedgeprops = { 'linewidth' : 7, 'edgecolor' : 'white'})

        #display a white circle in the middle of the pie chart
        p = plt.gcf()
        p.gca().add_artist(plt.Circle( (0,0), 0.7, color='white'))
        st.pyplot(fig)