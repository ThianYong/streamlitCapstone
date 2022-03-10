import os
import streamlit as st
import numpy as np
from PIL import Image

# Custom imports 
from multipage import MultiPage
from pages import page01, page02, page03, page04, page05, data01 # import pages here

# Create an instance of the app 
main = MultiPage()

# Title of the main page
display = Image.open('images/Logo5.png')
display = np.array(display)
# st.image(display, width = 400)
# st.title("NUS Capstone")
col1, col2 = st.columns(2)
col1.image(display, width = 300)
col2.title("NUS Capstone 2022")

# Add all your application here
'''
New pages are to be added here. 
'''
main.add_page("Page 1", page01.app)
main.add_page("Page 2", page02.app)
main.add_page("Page 3", page03.app)
main.add_page("Page 4", page04.app)
main.add_page("Page 5", page05.app)
main.add_page('Data 1', data01.app)

# The main app
main.run()
