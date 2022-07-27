import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import timedelta

#@st.cache
def app():
    """
    Ising J1 J2 Page
    """
    with st.container():
        col11, col12, col13 = st.columns(3)
        with col11:
            st.metric('J2', "-5.0 to 5.0")
            st.metric('H', "1")

        with col12:
            st.metric('Iteration/J2', '10')
            st.metric('Epoch Cap', '10,000')
        with col13:
            st.metric('Learning Rate', '0.001')
            st.metric('Stopping Threshold', '0.005')
    st.write('---')

    st.header('Please Filter Data Here:')
    # ---- Select The model ---- ##
    option = st.selectbox(
        'Select the Model Type: ',
        ('MLP', 'RBM'))
    # st.write('You selected:', option)


    @st.cache  ### use cache to buffer the data. Improve loading time.
    def get_data(filename):
        return pd.read_csv(filename)

    if option == 'MLP':
        df = get_data('data/RBM_J1J2_combined.csv')
    else:
        df = get_data('data/RBM_J1J2_combined.csv')


    ### --- uncomment this part of do not want the selection to be on the sidebar ---#
    col1, col2, col3 = st.columns([0.6,0.1, 0.3])

    with col1:
        Col_Y_Select = st.selectbox(
            'Select the Graph to be Plotted:',
            # options=df.columns,
            options = ['Epoch', 'Time', 'Energy-Std', 'Cz-Ferro', 'Cz-Antiferro', 'Mz2-Ferro', 'Mz2-Antiferro', 'Mx-Ferro', 'Nz-Ferro', 'Nz-Antiferro', 'Std_Mean' ]
        )
        J2 = st.slider(
        'Select the J2:',
        min_value=min(df['J2'].unique()),
        max_value=max(df['J2'].unique()),
        value=(-5.0, -4.5),
        step=0.1
        )


    with col3:
        J1 = st.selectbox(
            'Select the J value: ',
            options=df['J1'].unique()
        )

        length = st.radio(
            'Select the Length:',
            options=df['Length'].unique(),
            # default=4
        )

    st.write('---')

    ## Create a list of numbers selected, round the numbers to 1 decimal place
    J2 = np.arange(J2[0], J2[1]+0.1, 0.1).tolist()
    J2 = [round(num, 1) for num in J2]

    df_selection = df.query(
        'Length == @length & J1 == @J1 & J2==@J2'
    )



    # ---- Dashboard ---- #
    st.title(':bar_chart: Chart')
    st.markdown("##")

    # KPIs
    total_time_sec = int(df_selection['Time'].sum())
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

    select_chart = (
        df_selection.groupby(by=['J2']).mean()[[Col_Y_Select]]
    )
    select_chart['J2'] = select_chart.index.astype(str)

    col1, col2 = st.columns(2)
    with col1:
        fig_select_chart = px.bar(
            select_chart,
            x='J2',
            y=Col_Y_Select,
            orientation='v',
            title=('<b>' + str.title(Col_Y_Select) + '</b>'),
            color_discrete_sequence=['#0083B8'],
            template='plotly_white',
            text=round(select_chart[Col_Y_Select], 3)
        )
        fig_select_chart.update_layout(
            # xaxis=dict(tickmode='linear'),
            plot_bgcolor='rgba(0,0,0,0)',
            yaxis=(dict(showgrid=False))
        )
        fig_select_chart.update_yaxes(title_text=str.title(Col_Y_Select))

        st.plotly_chart(fig_select_chart, use_container_width=True)



    # ---- Error Bars ---- #
    with col2:
        error_chart = (
            df_selection.groupby(by=['J2'])[[Col_Y_Select]]
        )

        error_chart_mean = error_chart.mean()[Col_Y_Select].tolist()
        error_chart_min = error_chart.min()[Col_Y_Select].tolist()
        error_chart_max = error_chart.max()[Col_Y_Select].tolist()
        error_chart = error_chart.mean()[Col_Y_Select]

        error_chart = pd.DataFrame(error_chart)
        error_chart['J2'] = error_chart.index.astype(str)

        error_chart_x = error_chart['J2'].tolist()
        error_chart_y = error_chart_mean

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
            title_text = ('<b>' + str.title(Col_Y_Select) + '</b>'),
            yaxis=(dict(showgrid=False)),
            # xaxis={'visible': True, 'showticklabels': True},
        )

        fig.update_xaxes(title_text="J2")
        fig.update_yaxes(title_text=str.title(Col_Y_Select))

        st.plotly_chart(fig, use_container_width=True)

    st.write('---')

    ## ==== Show table ==== ##
    st.title(':clipboard: Table')  # set the title
    st.dataframe(df_selection)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col4:
        st.write(f'Rows: {df_selection.shape[0]}')
    with col5:
        st.write(f'Columns: {df_selection.shape[1]}')






