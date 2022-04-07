import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie  #need to create free account at lottie

def app():
    #This uses formsubmit. Documentation is here : https://formsubmit.co
    #CSS from W3schools, here: https://www.w3schools.com/howto/howto_css_contact_form.asp

    # url = 'https://raw.githubusercontent.com/ThianYong/streamlitCapstone/main/'
    url = '/Users/thianyong/Library/Mobile Documents/com~apple~CloudDocs/Master Study/NUS/Capstone/Project/Capstone Codes/streamlitCapstone/'

    '''
    To do Animation
    '''
    ## load the animation locally
    def load_lottiefile(filepath: str):
        with open(filepath, 'r') as f:
            return json.load(f)

    # ## load the animation directly from the web.
    # def load_lottieurl(url:str):
    #     r = request.get(url)
    #     if r.status_code !=200:
    #         return None
    #     return r.json()

    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        lottie_email = load_lottiefile(url+'lottie/contact.json')
        st_lottie(
            lottie_email,
            speed=1,
            reverse=False,
            loop=True,
            quality='low', #medium, high
            height=350,
            width=350,
            key=None
        )

    st.header(':mailbox: Get In Touch With The Team!')
    contact_form = '''
    <form action="https://formsubmit.co/thianyong@u.nus.edu" method="POST">
         <input type="text" name="name" placeholder = 'Your Name' required>
         <input type="email" name="email" placeholder = 'Your Email' required>
         <textarea name="message" placeholder="Your Message Here"></textarea>
         <button type="submit">Send</button>
    </form>
    '''

    st.markdown(contact_form, unsafe_allow_html=True)

    ## read in the CSS style for contact forms
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    ### call the function
    local_css(url+"style/contactStyle.css")

