import os
import streamlit as st
import numpy as np
from PIL import Image
from annotated_text import annotated_text
from streamlit_option_menu import option_menu

# Custom imports 
from multipage import MultiPage
from pages import page01, home, page02, RBM, page04, MLP, hardware# import pages here

# Create an instance of the app 
main = MultiPage()
# st.set_page_config(layout="wide") # set layout to wide for all pages
st.set_page_config(page_title='NUS Capstone 2022', page_icon='🐙') # set the name of the page

# Title of the main page
display = Image.open('images/Logo5.png')
display = np.array(display)
# st.image(display, width = 400)
# st.title("NUS Capstone")
col1, col2 = st.columns(2)
col1.image(display, width = 300)
col2.title("MAPALUS:")
col2.markdown(
'''
#### Neural-Network Quantum States Library with GPU 
'''
)


# Add all the pages here

main.add_page("Home", home.app)
main.add_page("Page 1", page01.app)
main.add_page("Page 2", page02.app)
main.add_page("Page 3", page03.app)
main.add_page("Page 4", page04.app)
main.add_page("Page 5", page05.app)
main.add_page('Data', data.app)

# The main app
main.run()



## To change the page navigation method
# with st.sidebar:
#     st.write('Option 2')
# with st.sidebar:
#     selected = option_menu(
#         menu_title='Main Menu',
#         options=['Home', 'Data', 'Contacts'],
#         icons = ['house', 'book', 'envelope'],
#         menu_icon='cast',
#         default_index=0
#     )
# if selected == 'Home':
#     # home.app()
#     st.title(f'You have selected {selected}')
#
# if selected == 'Data':
#     # data.app()
#     st.title(f'You have selected {selected}')
# if selected == 'Contacts':
#     st.title(f'You have selected {selected}')
    


