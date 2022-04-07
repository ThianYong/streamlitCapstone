import streamlit as st
from PIL import Image
from annotated_text import annotated_text
from streamlit_option_menu import option_menu

# Custom imports
from pages import page01, home, page02, page03, page04, table, data, contacts


# st.set_page_config(layout="wide") # set layout to wide for all pages
st.set_page_config(page_title='NUS Capstone 2022', page_icon=':panda_face:') # set the name of the page

# Title of the main page
display = Image.open('images/Logo5.png')
# display = np.array(display)
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



## Add all the pages here.
## Icon is using bootstrap.
with st.sidebar:
    st.write('Page Navigation')
with st.sidebar:
    selected = option_menu(
        menu_title='Main Menu',
        options=['Home', 'Data', 'Page 1','Page 2', 'Page 3', 'Page 4', 'Table', 'Contact Us'],
        icons = ['house', 'book', 'journal-richtext', 'journal-richtext','journal-richtext','journal-richtext','table', 'envelope'],
        menu_icon='cast',
        default_index=0
    )

if selected == 'Home':
    home.app()
    # st.title(f'You have selected {selected}')

if selected == 'Data':
    data.app()
    # st.title(f'You have selected {selected}')
if selected == 'Contact Us':
    contacts.app()
    # st.title(f'You have selected {selected}')

if selected == 'Page 1':
    page01.app()
if selected == 'Page 2':
    page02.app()
if selected == 'Page 3':
    page03.app()
if selected == 'Page 4':
    page04.app()
if selected == 'Table':
    table.app()
    


