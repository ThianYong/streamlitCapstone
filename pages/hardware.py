import streamlit as st
import pandas as pd
import plotly.figure_factory as ff



#@st.cache
def app():
    """
    What is this page for?
    """
    st.title(':computer: Hardware Specification') #set the title

    st.write('#')
    st.markdown(
    """
    We use the **MAPALUS** library for the application to find the ground state of Ising model.
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
        return pd.read_csv(filename)

    ''' Plot the distribution of time consumed. Read in the data '''
    # cols_filt = ['num', 'epoch', 'time', 'J', 'length']
    # df_4 = get_data('MLP_combined_length_4.csv') #, usecols=cols_filt)
    # df_8 = get_data('MLP_combined_length_8.csv') #, usecols=cols_filt)

    df = get_data('data/MLP_combined.csv') ### combined all into 1 df.
    filt_4 = df['length']==4
    filt_8 = df['length']==8
    filt_16 = df['length']==16

    hist_data = [df[filt_4]['time'], df[filt_8]['time'], df[filt_16]['time']]
    group_labels = ['Length = 4', 'Length = 8', 'Length = 16']
    fig = ff.create_distplot(hist_data, group_labels)
    fig.update_layout(title='Distribution Plot on Time(sec) Taken for Each Iteration for Different Sizes - MLP')

    st.plotly_chart(fig, use_container_width=True)


