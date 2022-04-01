import streamlit as st
import numpy as np
import pandas as pd
from annotated_text import annotated_text, annotation
from PIL import Image

#@st.cache
def app():
    """
    What is this page for?
    """
    url = 'https://raw.githubusercontent.com/ThianYong/streamlitCapstone/main/data/'
    # url = '../Project/data/'

    st.title('Home :wave:') #set the title

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

    with st.container():

        st.write('---')
        st.title('Overview of the Library')
        st.markdown("""
        In **Mapalus**, the users can use neural-network quantum states to find the ground state or excited states of a given system. 
        The system is described by the structure and the quantum model of the system. 
        Users can choose to train the neural-network quantum states in an unsupervised or supervised manner with different neural network architectures.  
        For the unsupervised training, the users can use different Monte Carlo sampling algorithms. 
        The library also provide a logging mechanism that saves the necessary information from the training. 
        This includes the computation of an observable on the system. 
        **Mapalus** is purely written in Python with TensorFlow framework that can run parallelly on Message Passing Interface (MPI) or general-purpose graphics processing units (GPUs). 
        The library also provides an exact diagonalisation method for comparison.
                   """)
        st.markdown('''
        The structure of the system is described by a graph that describes the connection between particles. 
        This includes the number of particles, dimensions,  boundary conditions, and the connections between particles. 
        The quantum model of the system is described by defining the Hamiltonian matrix of the system. 
        The library has the quantum Ising, Ising J_1-J_2, Heisenberg, and Heisenberg J_1-J_2 Hamiltonians. 
        The sampling can be done with Gibbs or Metropolis sampling.  
        For the supervised training, users need to provide the training and testing data that consists of the configurations and the value of the wave function. 
        The following neural network architectures are available in the library: restricted Boltzmann machine, multilayer perceptron, recurrent neural network, and convolutional neural network. 
        The users can customise the activation functions to be used in the neural network. The architectures support real or complex weights depending on the wave function of the systems. 
        The library also provides magnetisation and correlation observables for the users to use. 
        The exact diagonalisation method supports the calculation of system up to $10$ particles to get all of the states and $20$ particles to get some of the states.
        ''')
        st.markdown('''
        The more details documentation of the library can be find here [later we will put a pdf file]
        ''')

    with st.container():
        st.write('---')
        st.title('Benchmarking')
        st.markdown('''
        We compare the MAPALUS library run on a general-purpose GPUs to a parallel CPUs implementation, for which we use the NetKe  library. 
        At the time of comparison, we are using NetKet version 2.0, which was still mainly written in C++. 
        We have compared both codes with the same set of parameters, using restricted Boltzmann machines with real weights and sampling with the Metropolis algorithm that flips a random spin.  
        ''')

        col1, col2 = st.columns(2) ## no meaning, just to center the picture.
        with col1:
            st.markdown('''
                This is illustrated, for reference only, in Figure on the right where the computation time (in seconds) needed by different numerical strategies to reach the stopping criterion is
            plotted as the function of the size of the system N for the one-dimensional Ising model at the quantum phase transition point (J=1.0).
            For a system of 128 spins, our library runs about 5 times faster than the NetKet implementation.
            ''')
        with col2:
            image1 = Image.open('images/home01.png')
            image1 = np.array(image1)
            st.image(image1, caption='Figure name')




