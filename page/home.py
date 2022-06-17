import streamlit as st
import numpy as np
import pandas as pd
from annotated_text import annotated_text, annotation
from PIL import Image

#@st.cache
def app():

    """
    This is the Main Home Page.
    """

    st.title(':house: Home ') #set the title

    st.write('## Background')
    annotated_text(
        # ('MAPALUS ', '', '#aaf', '#ffa'),
        'MAPALUS'
        'implements the ',
        ('neural-network quantum states ', '[1] ', '#afa', '#000'),
        'with ',
        'Python 3 ',
        'and ',
        'Tensorflow 2',
        'library to speed-up the process with general-purpose ',
        # ('graphics processing units (GPU). ', '', '#8CD9FA', '#000'),
        'graphics processing units (GPU)'
        'The implementation is inspired by',
        ('NetKet library ','[2] ','#F6A1F3','#000'),
        '.'
    )
    st.write('')

    st.write('### List of papers that use MAPALUS: ')

    st.markdown('''
    1. Zen, Remmy, et al. "Transfer learning for scalability of neural-network quantum states." Physical Review E 101.5 (2020): 053301.
    2. Zen, Remmy, et al. "Finding quantum critical points with neural-network quantum states." arXiv preprint arXiv:2002.02618 (2020).
    3. Zen, Remmy, and Stéphane Bressan. "Transfer Learning for Larger, Broader, and Deeper Neural-Network Quantum States." International Conference on Database and Expert Systems Applications. Springer, Cham, 2021.
    ''')

    st.write('')
    with st.expander("References:"):
        st.markdown("""
        1. G. Carleo and M. Troyer, Science 355, 602 (2017)
        2. G. Carleo, K. Choo, D. Hofmann, J. E. T. Smith,T. Westerhout, F. Alet, E. J. Davis, S. Efthymiou,I. Glasser, S.-H. Lin, M. Mauri, G. Mazzola, C. B. Mendl,E. van Nieuwenburg, O. O’Reilly, H. Th ́eveniaut, G. Tor-lai, F. Vicentini, and A. Wietek, SoftwareX , 100311(2019).
             """)

    with st.container():
        st.write('---')
        st.title('Useful Links')
        st.markdown("""
                    The library can be found in the GitHub repository here: [Github](https://github.com/remmyzen/nqs-tensorflow2) 
                    """)
        st.markdown("""
                    The different examples to run the code is available in the notebooks directory here: [Python Notebook](https://github.com/remmyzen/nqs-tensorflow2/tree/main/notebooks)
                    """)
        st.write('---')
