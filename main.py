import os
import streamlit as st
import numpy as np
from PIL import Image

# Custom imports 
from multipage import MultiPage
from pages import home, page01, page02, page03, page04, page05, data01, page06_plotData# import pages here

# Create an instance of the app 
main = MultiPage()
# st.set_page_config(layout="wide") # set layout to wide for all pages

# Title of the main page
display = Image.open('images/Logo5.png')
display = np.array(display)
# st.image(display, width = 400)
# st.title("NUS Capstone")
col1, col2 = st.columns(2)
col1.image(display, width = 300)
col2.title("NUS Capstone 2022")
col2.markdown(
    '''
    The National University of Singapore aspires to be a vital community of academics, researchers, staff, students and alumni working together in a spirit of innovation and enterprise for a better world.
    
    Our singular focus on talent will be the cornerstone of a truly great university that is dedicated to quality education, influential research and visionary enterprise, in service of country and society.
    '''
)

# Add all the pages here

main.add_page("Home", home.app)
main.add_page("Page 1", page01.app)
main.add_page("Page 2", page02.app)
main.add_page("Page 3", page03.app)
main.add_page("Page 4", page04.app)
main.add_page("Page 5", page05.app)
main.add_page('Data 1', data01.app)
main.add_page('Page 6', page06_plotData.app)

# The main app
main.run()
