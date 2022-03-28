import streamlit as st
import numpy as np
import pandas as pd

#@st.cache
def app():
    """
    What is this page for?
    """
    ### Set Data Set path
    url = 'https://raw.githubusercontent.com/ThianYong/streamlitCapstone/main/data/'
    # url = '../streamlitCapstone/data/'
    url_csv = url + '06_experiment_logs_L8_J-5.csv'

    st.title('Page 6') #set the title

    st.write('# This is a Page for Project Secret!')
    st.write('## This is Page 06.  Data Visualisation Page')
    st.markdown(
        """
        
        """
    )

    df = pd.read_csv(url_csv)
    st.dataframe(data=df)
    chart = st.line_chart(df)


    def pretty(s: str) -> str:
        try:
            return dict(js="JavaScript")[s]
        except KeyError:
            return s.capitalize()
    @st.cache
    def get_data():
        df = pd.read_csv(url_csv)
        df["num"] = df.num.map(pretty)
        return df

    # df = get_data()

    st.header("Plot 1")

    all_num = df.num.unique().tolist()
    nums = st.multiselect(
    "Numbers", options=all_num, default=all_num
    )
    plot_df = df[df.num.isin(nums)]
    # plot_df["std_mean"] = plot_df

    chart = (
        alt.Chart(
            plot_df,
            title="Chart 1",
        )
            .mark_bar()
            .encode(
            x=alt.X("std_mean", title="'std_mean"),
            y=alt.Y(
                "num",
                sort=alt.EncodingSortField(field="std_mean", order="descending"),
                title="",
            ),
            color=alt.Color(
                "num",
                legend=alt.Legend(title="Numbers"),
                # scale=alt.Scale(scheme="category10"),
            ),
            tooltip=["std_mean", "num", "num"],
        )
    )


    st.altair_chart(chart, use_container_width=True)

