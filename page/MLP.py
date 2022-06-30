import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import plotly.graph_objects as go
import numpy as np
from datetime import timedelta


def app():
    """
    MLP Page
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


    @st.cache  ### use cache to buffer the data. Improve loading time.
    def get_data(filename):
        return pd.read_csv(filename)


    df = get_data('data/MLP_combined.csv')

    ### --- SideBar --- ###
    st.sidebar.header('Please Filter Data Here:')
    # length = st.sidebar.multiselect(
    #     'Select the Length:',
    #     options=df['length'].unique(),
    #     default=4
    # )
    ## Radio button Style
    length = st.sidebar.radio(
        'Select the Length:',
        options=df['length'].unique(),
        # default=4
    )

    # MultiSelect not needed.
    # J = st.sidebar.multiselect(
    #     'Select the J:',
    #     options=df['J'].unique(),
    #     default=df['J'].unique() #{-5.0, -4.9, -4.8, -4.7}
    # )

    J1 = st.sidebar.slider(
        'Select the J:',
        min_value=min(df['J'].unique()),
        max_value=max(df['J'].unique()),
        value=(-5.0, -4.5),
        step=0.1
    )

    G1 = st.sidebar.selectbox(
        'Select the Graph to be Plotted:',
        # options=df.columns,
        options = ['time', 'Energy-Std', 'Cz-Ferro', 'Cz-Antiferro', 'Mz2-Ferro', 'Mz2-Antiferro', 'Mx-Ferro', 'Nz-Ferro', 'Nz-Antiferro', 'std_mean' ]
    )

    # st.sidebar.write('You selected:', G1)

    ## Create a list of numbers selected, round the numbers to 1 decimal place
    J1 = np.arange(J1[0], J1[1]+0.1, 0.1).tolist()
    J1 = [round(num, 1) for num in J1]
    # st.write(J1_list)

    df_selection = df.query(
        'length == @length & J == @J1'
    )
    # st.write(J1)

    ### --- Show Table --- ###
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
    total_time_sec = int(df_selection['time'].mean())
    total_time = timedelta(seconds=total_time_sec)
    average_energy_mean = round(df_selection['Energy-Mean'].mean(), 1)
    average_energy_std = round(df_selection['Energy-Std'].mean(), 2)

    col11, col12, col13 = st.columns(3)
    with col11:
        st.subheader('Average Time:')
        st.subheader(f'{total_time}')
    with col12:
        st.subheader('Average Energy Mean:')
        st.subheader(f'{average_energy_mean}')
    with col13:
        st.subheader('Average Energy Std:')
        st.subheader(f'{average_energy_std}')

    st.markdown('---')


    # ---- Time Bar Chart ---- #
    # time_chart = (
    #     df_selection.groupby(by=['J']).mean()[['time']]#.sort_values(by='time')
    # )
    # time_chart['J'] = time_chart.index.astype(str)
    # fig_time_chart = px.bar(
    #     time_chart,
    #     x='J',
    #     y='time',
    #     orientation='v',
    #     title='<b> Average Time Consumed </b>',
    #     color_discrete_sequence=['#0083B8'], # * len(time_chart),
    #     template='plotly_white',
    #     labels ={'time': 'Time in Seconds'},
    #     text=time_chart['time'].astype(int)
    # )
    # fig_time_chart.update_layout(
    #     plot_bgcolor='rgba(0,0,0,0)',
    #     yaxis=(dict(showgrid=False))
    # )
    # st.plotly_chart(fig_time_chart)

    select_chart = (
        df_selection.groupby(by=['J']).mean()[[G1]]
    )
    select_chart['J'] = select_chart.index.astype(str)

    fig_select_chart = px.bar(
        select_chart,
        x='J',
        y=G1,
        orientation='v',
        title=('<b>' + G1 + '</b>'),
        color_discrete_sequence=['#0083B8'],
        template='plotly_white',
        text=round(select_chart[G1], 3)
    )
    fig_select_chart.update_layout(
        # xaxis=dict(tickmode='linear'),
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis=(dict(showgrid=False))
    )

    st.plotly_chart(fig_select_chart)

    ## Show table for selected data
    #st.dataframe(time_chart.assign(hack='').set_index('hack'))

    # ---- Energy-STD Bar Chart ---- #
    # energy_chart = (
    #     df_selection.groupby(by=['J']).mean()[['Energy-Std']]#.sort_values(by='Energy-Std') # mean
    # )
    # energy_chart['J'] = energy_chart.index.astype(str)
    # fig_time_chart = px.bar(
    #     energy_chart,
    #     x='J',
    #     y='Energy-Std',
    #     orientation='v',
    #     title='<b> Energy-Std</b>',
    #     color_discrete_sequence=['#F63366'],
    #     template='plotly_white',
    # )
    # fig_time_chart.update_layout(
    #     # xaxis=dict(tickmode='linear'),
    #     plot_bgcolor='rgba(0,0,0,0)',
    #     yaxis=(dict(showgrid=False))
    # )
    #
    # st.plotly_chart(fig_time_chart)



    # ---- Error Bars ---- #
    error_chart = (
        df_selection.groupby(by=['J'])[[G1]]
    )


    st.write('Selected Data :' + G1 )
    col21, col22 = st.columns(2)
    with col21:

        st.write(
            'Select Chart: '
        )
        st.dataframe(select_chart)

    error_chart = error_chart.mean()[G1]

    error_chart = pd.DataFrame(error_chart)
    error_chart['J'] = error_chart.index.astype(str)

    with col22:

        st.write(
            'Error Chart: '
        )
        st.dataframe(error_chart)

    error_x = error_chart['J'].tolist()
    error_y = error_chart[G1].tolist()

    # st.write(error_x)
    # st.write(error_y)

    valueError = 25

    st.write('Value of Error :', valueError, '%')
    fig = go.Figure(
        data=go.Scatter(
            x=error_x,
            y=error_y,
            error_y=dict(
                type='percent', #  value of error bar given as percentage of y value
                value=valueError,
                visible=True),
        )
    )

    fig.update_layout(
        # xaxis=dict(tickmode='linear'),
        plot_bgcolor='rgba(0,0,0,0)',
        title_text = ('<b>' + G1 + '</b>'),
        yaxis=(dict(showgrid=False)),
    )

    st.plotly_chart(fig)

