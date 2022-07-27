import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import timedelta


def app():
    """
    Ising Page
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

    # st.header('Please Filter Data Here:')
    ## ---- Select The model ---- ##
    # option = st.selectbox(
    #     'Select the Model Type: ',
    #     ('MLP', 'RBM'))
    # st.write('You selected:', option)


    @st.cache  ### use cache to buffer the data. Improve loading time.
    def get_data(filename):
        return pd.read_csv(filename)



    ### --- uncomment this part of do not want the selection to be on the sidebar ---#
    # col1, col2, col3 = st.columns([0.6,0.1, 0.3])
    #
    # with col1:
    #     G1 = st.selectbox(
    #         'Select the Graph to be Plotted:',
    #         # options=df.columns,
    #         options = ['Epoch', 'Time', 'Energy-Std', 'Cz-Ferro', 'Cz-Antiferro', 'Mz2-Ferro', 'Mz2-Antiferro', 'Mx-Ferro', 'Nz-Ferro', 'Nz-Antiferro', 'Std_Mean' ]
    #     )
    #     J = st.slider(
    #     'Select the J:',
    #     min_value=min(df['J'].unique()),
    #     max_value=max(df['J'].unique()),
    #     value=(-5.0, -4.5),
    #     step=0.1
    #     )
    #
    #
    # with col3:
    #
    #     length = st.radio(
    #         'Select the Length:',
    #         options=df['Length'].unique(),
    #         # default=4
    #     )
    #
    # st.write('---')

    ### --- SideBar --- ###
    st.sidebar.header('Please Filter Data Here:')

    option = st.sidebar.selectbox(
        'Select the Model Type: ',
        ('MLP', 'RBM'))
    if option == 'MLP':
        df = get_data('data/MLP_combined.csv')
    else:
        df = get_data('data/RBM_combined.csv')

    # Radio button Style
    length = st.sidebar.radio(
        'Select the Length:',
        options=df['Length'].unique(),
        # default=4
    )

    J = st.sidebar.slider(
        'Select the J:',
        min_value=min(df['J'].unique()),
        max_value=max(df['J'].unique()),
        value=(-5.0, -4.5),
        step=0.1
    )

    G1 = st.sidebar.selectbox(
        'Select the Graph to be Plotted:',
        # options=df.columns,
        options = ['Epoch', 'Time', 'Energy-Std', 'Cz-Ferro', 'Cz-Antiferro', 'Mz2-Ferro', 'Mz2-Antiferro', 'Mx-Ferro', 'Nz-Ferro', 'Nz-Antiferro', 'Std_Mean' ]
    )

    # st.sidebar.write('You selected:', G1)

    ## Create a list of numbers selected, round the numbers to 1 decimal place
    J = np.arange(J[0], J[1]+0.1, 0.1).tolist()
    J = [round(num, 1) for num in J]
    # st.write(J_list)

    df_selection = df.query(
        'Length == @length & J == @J'
    )
    # st.write(J)

    # ---- Dashboard ---- #
    st.title(':bar_chart: Chart')
    st.markdown("##")

    # KPIs
    total_time_sec = int(df_selection['Time'].mean())
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
        title=('<b>' + str.title(G1) + '</b>'),
        color_discrete_sequence=['#0083B8'],
        template='plotly_white',
        text=round(select_chart[G1], 3)
    )
    fig_select_chart.update_layout(
        # xaxis=dict(tickmode='linear'),
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis=(dict(showgrid=False))
    )
    fig_select_chart.update_yaxes(title_text=str.title(G1))

    st.plotly_chart(fig_select_chart, use_container_width=True)

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

    # st.write(error_chart)
    # st.write(error_chart.describe())
    # st.write('Selected Data :' + G1 )


    ''' ==== This section is for debug purpose only.  It prints both Select table and Error table side by side ==== '''
    ''' 
    col21, col22 = st.columns(2)
    with col21:

        st.write(
            'Select Chart: '
        )
        st.dataframe(select_chart) #mean

    error_chart_mean = error_chart.mean()[G1].tolist()
    error_chart_min = error_chart.min()[G1].tolist()
    error_chart_max = error_chart.max()[G1].tolist()
    error_chart = error_chart.mean()[G1]

    error_chart = pd.DataFrame(error_chart)
    error_chart['J'] = error_chart.index.astype(str)

    with col22:

        st.write(
            'Error Chart: '
        )
        st.dataframe(error_chart) #mean

    error_chart_x = error_chart['J'].tolist()
    error_chart_y = error_chart_mean
    '''

    ''' ==== End of Debug Code ==== '''

    ''' ==== Definition of the axes ====
    x = J 
    y = mid point is the mean
    array =  is the max value
    arrayminus =  is the min value
    '''
    error_chart_mean = error_chart.mean()[G1].tolist()
    error_chart_min = error_chart.min()[G1].tolist()
    error_chart_max = error_chart.max()[G1].tolist()
    error_chart = error_chart.mean()[G1]

    error_chart = pd.DataFrame(error_chart)
    error_chart['J'] = error_chart.index.astype(str)

    error_chart_x = error_chart['J'].tolist()
    error_chart_y = error_chart_mean

    # st.write(error_chart)
    # st.write(error_chart_x)
    # st.write(error_chart_y)
    # st.write('array :', error_chart_max)
    # st.write('arrayminus :', error_chart_min)

    fig = go.Figure(
        data=go.Scatter(
            x=error_chart_x,
            y=error_chart_y,
            error_y=dict(
                type='data', #'percent', #  value of error bar given as percentage of y value
                symmetric = False,
                array = error_chart_max,
                arrayminus = error_chart_min,)
                # value=valueError,
                # visible=True),
        )
    )

    fig.update_layout(
        # xaxis=dict(tickmode='linear'),
        plot_bgcolor='rgba(0,0,0,0)',
        title_text = ('<b>' + str.title(G1) + '</b>'),
        yaxis=(dict(showgrid=False)),
        # xaxis={'visible': True, 'showticklabels': True},
    )

    fig.update_xaxes(title_text="J")
    fig.update_yaxes(title_text=str.title(G1))

    st.plotly_chart(fig, use_container_width=True)


    ### --- Show Table --- ###
    st.title(':clipboard: Table')  # set the title
    st.dataframe(df_selection)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col4:
        st.write(f'Rows: {df_selection.shape[0]}')
    with col5:
        st.write(f'Columns: {df_selection.shape[1]}')


''' 
    st.write(' ==== Test Run the split col. Left is Bar Chart, right is Error Bar ==== ')


    col21, col22 = st.columns(2)
    with col21:

        select_chart = (
            df_selection.groupby(by=['J']).mean()[[G1]]
        )
        select_chart['J'] = select_chart.index.astype(str)

        fig_select_chart = px.bar(
            select_chart,
            x='J',
            y=G1,
            orientation='v',
            title=('<b>' + str.title(G1) + '</b>'),
            color_discrete_sequence=['#0083B8'],
            template='plotly_white',
            text=round(select_chart[G1], 3)
        )
        fig_select_chart.update_layout(
            # xaxis=dict(tickmode='linear'),
            plot_bgcolor='rgba(0,0,0,0)',
            yaxis=(dict(showgrid=False))
        )
        fig_select_chart.update_yaxes(title_text=str.title(G1))

        st.plotly_chart(fig_select_chart, use_container_width=True)

    with col22:

        fig = go.Figure(
            data=go.Scatter(
                x=error_chart_x,
                y=error_chart_y,
                error_y=dict(
                    type='data', #'percent', #  value of error bar given as percentage of y value
                    symmetric = False,
                    array = error_chart_max,
                    arrayminus = error_chart_min,)
                # value=valueError,
                # visible=True),
            )
        )


        fig.update_layout(
            # xaxis=dict(tickmode='linear'),
            plot_bgcolor='rgba(0,0,0,0)',
            title_text = ('<b>' + str.title(G1) + '</b>'),
            yaxis=(dict(showgrid=False)),
            # xaxis={'visible': True, 'showticklabels': True},
        )

        fig.update_xaxes(title_text="J")
        fig.update_yaxes(title_text=str.title(G1))
        st.plotly_chart(fig, use_container_width=True)











    st.write(' ==== Test Run the split col. Left is RBM, right is MLP ==== ')
    col21, col22 = st.columns(2)
    with col21:
        st.write('Left is RBM: ')

        # st.write('Please Filter RBM Data Here:')
        #
        # ## Radio button Style
        # length_RBM = st.radio(
        #     'Select the Length:',
        #     key = 2,
        #     options=df_RBM['length'].unique(),
        # )
        #
        # J_RBM = st.slider(
        #     'Select the J:',
        #     key = 2,
        #     min_value=min(df_RBM['J'].unique()),
        #     max_value=max(df_RBM['J'].unique()),
        #     value=(-5.0, -4.5),
        #     step=0.1
        # )
        #
        # G1_RBM = st.selectbox(
        #     'Select the Graph to be Plotted:',
        #     key = 2,
        #     options = ['epoch', 'time', 'Energy-Std', 'Cz-Ferro', 'Cz-Antiferro', 'Mz2-Ferro', 'Mz2-Antiferro', 'Mx-Ferro', 'Nz-Ferro', 'Nz-Antiferro', 'std_mean' ]
        # )
        #
        # # st.sidebar.write('You selected:', G1)
        #
        # ## Create a list of numbers selected, round the numbers to 1 decimal place
        # J_RBM = np.arange(J_RBM[0], J_RBM[1]+0.1, 0.1).tolist()
        # J_RBM = [round(num, 1) for num in J1]
        # # st.write(J1_list)
        #
        df_RBM_selection = df_RBM.query(
            'Length == @length & J == @J1'
        )
        # # st.write(J1)
        #
        #
        # ### --- Show Table --- ###
        # st.dataframe(df_RBM_selection)
        error_chart = (
            df_RBM_selection.groupby(by=['J'])[[G1]]
        )
        error_chart_mean = error_chart.mean()[G1].tolist()
        error_chart_min = error_chart.min()[G1].tolist()
        error_chart_max = error_chart.max()[G1].tolist()
        error_chart = error_chart.mean()[G1]

        error_chart = pd.DataFrame(error_chart)
        error_chart['J'] = error_chart.index.astype(str)

        error_chart_x = error_chart['J'].tolist()
        error_chart_y = error_chart_mean
        fig_RBM = go.Figure(
            data=go.Scatter(
                x=error_chart_x,
                y=error_chart_y,
                error_y=dict(
                    type='data', #'percent', #  value of error bar given as percentage of y value
                    symmetric = False,
                    array = error_chart_max,
                    arrayminus = error_chart_min,)
                # value=valueError,
                # visible=True),
            )
        )


        fig_RBM.update_layout(
            # xaxis=dict(tickmode='linear'),
            plot_bgcolor='rgba(0,0,0,0)',
            title_text = ('<b>' + str.title(G1) + '</b>'),
            yaxis=(dict(showgrid=False)),
            # xaxis={'visible': True, 'showticklabels': True},
        )

        fig_RBM.update_xaxes(title_text="J")
        fig_RBM.update_yaxes(title_text=str.title(G1))
        st.plotly_chart(fig_RBM, use_container_width=True)

    with col22:
        st.write('Right is MLP: ')

        st.plotly_chart(fig, use_container_width=True)

'''
