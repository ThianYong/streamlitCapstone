import streamlit as st
import numpy as np
from PIL import Image


#@st.cache
def app():
    """
    This is the overview Page.
    """
    st.title(':orange_book: Overview') #set the title

    with st.container():

        st.title('Library')
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

        col1, col2 = st.columns(2)
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


