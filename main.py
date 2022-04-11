import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

# Custom imports
from pages import overview, home, page02, RBM, MLP, hardware, contacts

# st.set_page_config(layout="wide") # set layout to wide for all pages
st.set_page_config(page_title='NUS Capstone 2022', page_icon=':panda_face:') # set the name of the page

# Customised the Streamlit Page
# add this if want to remove header color: header {visibility: hidden;}
# add this if want to remove the hamburger on top right: #MainMenu {visibility: hidden;}
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Title of the main page
display = Image.open('images/Logo2.png')
col1, col2 = st.columns(2)
with col1:
    placeholderLeft = st.empty()
    with placeholderLeft:
        st.image(display, width = 300)
with col2:
    placeholderRight = st.empty()
    with placeholderRight:
        st.markdown(
        '''
        # MAPALUS:
        #### Neural-Network Quantum States Library with GPU
        '''
        )


## Add all the pages here.
## Icon is using bootstrap.
with st.sidebar:
    st.write('Page Navigation')
with st.sidebar:
    selected = option_menu(
        menu_title='Main Menu',
        options=['Home', 'Overview', 'Hardware','Page 2', 'RBM', 'MLP', 'Contact Us'],
        icons = ['house', 'eyeglasses', 'pc-display-horizontal', 'journal-richtext', 'file-bar-graph', 'file-bar-graph-fill', 'envelope'],
        menu_icon='cast',
        default_index=0
    )

if selected == 'Home':
    home.app()
    # st.title(f'You have selected {selected}')

if selected == 'Hardware':
    hardware.app()
    # st.title(f'You have selected {selected}')
if selected == 'Contact Us':
    placeholderLeft.empty()
    placeholderRight.empty()
    contacts.app()
    # st.title(f'You have selected {selected}')

if selected == 'Overview':
    overview.app()
if selected == 'Page 2':
    page02.app()
if selected == 'RBM':
    RBM.app()
if selected == 'MLP':
    MLP.app()
    


