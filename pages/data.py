import streamlit as st
import numpy as np
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import matplotlib
from matplotlib.backends.backend_agg import RendererAgg
import matplotlib.pyplot as plt
from annotated_text import annotated_text, annotation
import altair as alt


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

    df = get_data('MLP_combined.csv') ### combined all into 1 df.

    hist_data = [df_4['time'], df_8['time']]
    group_labels = ['Length = 4', 'Length = 8']
    fig = ff.create_distplot(hist_data, group_labels)
    fig.update_layout(title='Distribution Plot on Time(sec) Taken for Each Iteration for Different Sizes - MLP')

    st.plotly_chart(fig, use_container_width=True)


    '''
    Plot the epoch
    '''
    hist_data = [df_4['epoch'], df_8['epoch']]
    group_labels = ['Length = 4', 'Length = 8']
    fig = ff.create_distplot(hist_data, group_labels)
    fig.update_layout(title='Distribution Plot on Epoch Taken for Each Iteration for Different Sizes - MLP')

    st.plotly_chart(fig, use_container_width=True)

    ### To highlight certain cell of dataframes
    val_threshold = 0 # set the value that need to change color
    def color_df(val):
        if val>=val_threshold:  ## add more condition if need to change more colors
            color = 'red'
        return f'background-color: {color}'

    if st.checkbox('Show Raw Data of Dist Plot Above'):
        st.dataframe(df.style.applymap(color_df, subset=['epoch']))
        # st.dataframe(data=df)

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

    ### prepare data for plots
    df_plot = df_4[{'Cz-Ferro', 'Cz-Antiferro' ,'Mz2-Ferro', 'Mz2-Antiferro', 'Nz-Ferro', 'Nz-Antiferro'}]

    st.write('## Observables')
    col21, col22, col23, col24= st.columns(4)
    with col21:
        st.metric('Size/Length', '4')
    with col22:
        annotated_text(
            ('Cz-Ferro', '', '#A1DCF6', '#000'),
        )
        annotated_text(
            (' Cz-Antiferro', '', '#A1DCF6', '#000'),
        )

    with col23:
        annotated_text(
            (' Mz2-Ferro', '', '#8DF875', '#000'),
        )
        annotated_text(
            (' Mz2-Antiferro', '', '#ACF89B', '#000'),
        )
    with col24:
        annotated_text(
            (' Nz-Ferro', '', '#E49BF8', '#000'),
        )
        annotated_text(
            (' Nz-Antiferro', '', '#DB70F8', '#000'),
        )
    fig = px.box(df_plot)
    st.plotly_chart(fig)

    ### prepare data for plots
    df_plot = df_4[{'energy', 'energy_std', 'Energy-Mean', 'Energy-Std'}]

    colors = {
        'energy': '#A1DCF6',
        'energy_std': '#A1DCF6',
        'Energy-Mean': '#8DF875',
        'Energy-Std': '#ACF89B',
        }

    st.write('## Observables')
    col21, col22, col23= st.columns(3)
    with col21:
        st.metric('Size/Length', '4')
    with col22:
        annotated_text(
            ('energy', '', '#A1DCF6', '#000'),
        )
        annotated_text(
            (' energy_std', '', '#A1DCF6', '#000'),
        )

    with col23:
        annotated_text(
            (' Energy-Mean', '', '#8DF875', '#000'),
        )
        annotated_text(
            (' Energy-Std', '', '#ACF89B', '#000'),
        )

    fig = px.box(df_plot)
    st.plotly_chart(fig)

    '''
    Length = 8
    '''
    ### prepare data for plots
    df_plot = df_8[{'Cz-Ferro', 'Cz-Antiferro' ,'Mz2-Ferro', 'Mz2-Antiferro', 'Nz-Ferro', 'Nz-Antiferro'}]

    st.write('## Observables')
    col21, col22, col23, col24= st.columns(4)
    with col21:
        st.metric('Size/Length', '8')
    with col22:
        annotated_text(
            ('Cz-Ferro', '', '#A1DCF6', '#000'),
        )
        annotated_text(
            (' Cz-Antiferro', '', '#A1DCF6', '#000'),
        )

    with col23:
        annotated_text(
            (' Mz2-Ferro', '', '#8DF875', '#000'),
        )
        annotated_text(
            (' Mz2-Antiferro', '', '#ACF89B', '#000'),
        )
    with col24:
        annotated_text(
            (' Nz-Ferro', '', '#E49BF8', '#000'),
        )
        annotated_text(
            (' Nz-Antiferro', '', '#DB70F8', '#000'),
        )
    fig = px.box(df_plot)
    st.plotly_chart(fig)
    # fig = alt.Chart(df_plot).mark_boxplot(extent='min-max')
    # st.altair_chart(fig, use_container_width=True)

    ### prepare data for plots
    df_plot = df_8[{'energy', 'energy_std', 'Energy-Mean', 'Energy-Std'}]

    colors = {
        'energy': '#A1DCF6',
        'energy_std': '#A1DCF6',
        'Energy-Mean': '#8DF875',
        'Energy-Std': '#ACF89B',
    }

    st.write('## Observables')
    col21, col22, col23= st.columns(3)
    with col21:
        st.metric('Size/Length', '8')
    with col22:
        annotated_text(
            ('energy', '', '#A1DCF6', '#000'),
        )
        annotated_text(
            (' energy_std', '', '#A1DCF6', '#000'),
        )

    with col23:
        annotated_text(
            (' Energy-Mean', '', '#8DF875', '#000'),
        )
        annotated_text(
            (' Energy-Std', '', '#ACF89B', '#000'),
        )

    fig = px.box(df_plot)
    st.plotly_chart(fig)



    '''
    box plot not good, yet. 

        st.header("J = -5.0")
        fig = px.box(df, x='J', y='energy')
        fig.show()
    '''
    st.write('')
    st.write('')
    st.write('## Allow Users Interaction ??')
    '''
    To Plot.
    '''
    filter_length = df['length'].unique().tolist()
    filter_selected = st.radio('Choose the Length', filter_length)
    if filter_selected == 4:
        filt = (df['length'] == filter_selected)
        # selected_df = df[str(filter_selected[0])]
        st.write(f'Rows: {df[filt].shape[0]}')
        st.write(f'Columns: {df[filt].shape[1]}')
        st.dataframe(df[filt])

    elif filter_selected == 8:
        filt = (df['length'] == filter_selected)
        # selected_df = df[str(filter_selected[0])]
        st.write(f'Rows: {df[filt].shape[0]}')
        st.write(f'Columns: {df[filt].shape[1]}')
        st.dataframe(df[filt])

    # get the list of columns
    columns = df.columns.tolist()
    st.write("#### Select the columns to display:")
    selected_cols = st.multiselect("", columns)
    if len(selected_cols) > 0:
        selected_df = df[selected_cols]
        st.write(f'Rows: {df.shape[0]}')
        st.write(f'Columns: {df.shape[1]}')
        # st.write(df.describe())
        st.dataframe(selected_df)