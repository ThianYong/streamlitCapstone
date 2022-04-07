import streamlit as st
import numpy as np
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import matplotlib
from matplotlib.backends.backend_agg import RendererAgg
import matplotlib.pyplot as plt
import seaborn as sns


def app():
    """
    What is this page for?
    """
    with st.container():
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
    st.write('---')
    st.title(':clipboard: Table')  # set the title
    url = 'https://raw.githubusercontent.com/ThianYong/streamlitCapstone/main/data/'

    @st.cache  ### use cache to buffer the data. Improve loading time.
    def get_data(filename):
        return pd.read_csv(url + filename)

    df = get_data('MLP_combined.csv')

    st.sidebar.header('Please Filter Data Here:')
    length = st.sidebar.multiselect(
        'Select the Length:',
        options=df['length'].unique(),
        default=4
    )

    J = st.sidebar.multiselect(
        'Select the J:',
        options=df['J'].unique(),
        default={-5.0, -4.9, -4.8, -4.7}
    )

    df_selection = df.query(
        'length == @length & J==@J'
    )

    st.dataframe(df_selection)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col4:
        st.write(f'Rows: {df_selection.shape[0]}')
    with col5:
        st.write(f'Columns: {df_selection.shape[1]}')

    # ---- Dashboard ---- #
    st.title(':bar_chart: Chart')
    st.markdown("##")

    # KPIs
    total_time = int(df_selection['time'].sum())
    average_energy_mean = round(df_selection['Energy-Mean'].mean(), 1)
    average_energy_mean_star = ":star:" * int(round(average_energy_mean, 0))
    average_energy_std = round(df_selection['Energy-Std'].mean(), 2)

    col11, col12, col13 = st.columns(3)
    with col11:
        st.subheader('Total Time:')
        st.subheader(f'{total_time} seconds')
    with col12:
        st.subheader('Average Energy Mean:')
        st.subheader(f'{average_energy_mean} {average_energy_mean_star}')
    with col13:
        st.subheader('Average Energy Std:')
        st.subheader(f'{average_energy_std}')

    st.markdown('---')

    # ---- Time Bar Chart ---- #
    time_chart = (
        df_selection.groupby(by=['J']).sum()[['time']].sort_values(by='time')
    )
    fig_time_chart = px.bar(
        time_chart,
        x=time_chart.index,
        y='time',
        orientation='v',
        title='<b> Time Consumed</b>',
        color_discrete_sequence=['#0083B8'] * len(time_chart),
        template='plotly_white',
    )
    fig_time_chart.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis=(dict(showgrid=False))
    )

    st.plotly_chart(fig_time_chart)

    # ---- Energy-STD Bar Chart ---- #
    time_chart = (
        df_selection.groupby(by=['J']).sum()[['Energy-Std']].sort_values(by='Energy-Std')
    )
    fig_time_chart = px.bar(
        time_chart,
        x=time_chart.index,
        y='Energy-Std',
        orientation='v',
        title='<b> Energy-Std</b>',
        color_discrete_sequence=['#0083B8'] * len(time_chart),
        template='plotly_white',
    )
    fig_time_chart.update_layout(
        # xaxis=dict(tickmode='linear'),
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis=(dict(showgrid=False))
    )

    st.plotly_chart(fig_time_chart)

# ---- Put in 2 cols ---- #
# col21, col22 = st.columns(2)
# with col21:
# 	st.plotly_chart(fig_time_chart)
# with col22:
# 	st.plotly_chart(fig_time_chart)
