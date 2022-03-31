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
	st.title('Page 5') #set the title
	url = 'https://raw.githubusercontent.com/ThianYong/streamlitCapstone/main/data/'


	st.write('# Sample plots to see the visual')
	st.write('## ')

	@st.cache  ### use cache to buffer the data. Improve loading time.
	def get_data(filename):
		return pd.read_csv(url+filename)

	''' Plot the distribution of time consumed. Read in the data '''
	# cols_filt = ['num', 'epoch', 'time', 'J', 'length']
	df_4 = get_data('MLP_combined_length_4.csv') #, usecols=cols_filt)
	df_plot = df_4[{'epoch', 'time','energy','Cz-Ferro', 'Cz-Antiferro' ,'J'}]

	matplotlib.use('agg')
	_lock = RendererAgg.lock ### use backend renderer to display graphs, more fluid.

	st.write('## matplotlib')
	with _lock:
		st.dataframe(df_plot)
		fig, ax = plt.subplots()
		ax.boxplot(df_plot)
		st.pyplot(fig)

	# st.write('## Seaborn')
	# fig = sns.boxplot(df_plot)
	# st.pyplot(fig)


	