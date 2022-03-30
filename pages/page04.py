import streamlit as st
from PIL import Image


def app():
    """
        What is this page for?
    """

    st.title('Page 4') #set the title

    st.header("Section A")

    st.write('# This is a Page for Project Secret!')
    st.write('## This is Page 04')

    st.write('## This is to demo pages can be divided into columns')

    col1, col2 = st.columns(2)
    display = Image.open('images/image01.png')
    col1.header('Singapore Map')
    col1.image(display, use_column_width=True)

    col2.header('Details')
    col2.markdown(
        """
        Modern Singapore was founded in 1819 by Sir Stamford Raffles as a trading post of the British Empire. In 1867, the colonies in Southeast Asia were reorganised and Singapore came under the direct control of Britain as part of the Straits Settlements. During the Second World War, Singapore was occupied by Japan in 1942, and returned to British control as a separate crown colony following Japan's surrender in 1945. Singapore gained self-governance in 1959 and in 1963 became part of the new federation of Malaysia, alongside Malaya, North Borneo, and Sarawak. 
        Ideological differences led to Singapore being expelled from the federation two years later and it became an independent country.
        
        """
    )



    st.markdown(
        """
        This Part demonstrate the link to parts of the page. 
        """
    )

    st.header("Section B")
    st.markdown("Go to [Section E](#section-e)", unsafe_allow_html=True)
    st.markdown(
        """
        Some random content:
        “With COVID-19, we have become a lot more ‘kiasu’ because we are an essential service. Our engineers and technicians have to go out to clients’ sites and they also work in teams,” he told CNA.
    
        “We are very cautious so what we’ve done is: If you’re feeling unwell and even if you haven’t tested positive, please stay home and rest,” said Mr Koh.
    
        The issue of MCs has been under the spotlight in recent months, following an advisory and repeated reminders from authorities that workers who have COVID-19 do not require a doctor’s certification to be excused from work. This is to ensure that the local healthcare system does not become overloaded amid rising local infections.
    
        Employers who "wilfully" refuse to comply with the advisory will have their work pass privileges suspended, Manpower Minister Tan See Leng said this week.
    
        Noting that “it was remarkable” that authorities have had to “explicitly” tell this to employers, experts like Singapore Human Resources Institute’s executive director Alvin Goh said sick leave policies in workplaces here must “adapt to the new normal”.
    
        """
    )

    st.header("Section C")
    st.markdown(
        """
        Some random content:
        Premiums for larger and more powerful cars in Category B rose from S$93,590 to S$94,889.
        
        For the Open category, which can be used for any vehicle type but end up being used mainly for large cars, prices went up from S$93,102 to S$98,890. This is the highest since January 2013, when premiums closed at S$97,889.
        
        Motorcycle premiums closed at a record S$11,400, having risen from S$10,589 in the previous bidding exercise.
        
        COEs for commercial vehicles, which include goods vehicles and buses, rose to S$48,889 from S$46,501.
        
        A total of 2,941 bids were received, with a quota of 1,753 COEs available.
        """
    )

    st.header("Section D")
    st.markdown(
        """
        Some random content:
        Premiums for larger and more powerful cars in Category B rose from S$93,590 to S$94,889.
        
        For the Open category, which can be used for any vehicle type but end up being used mainly for large cars, prices went up from S$93,102 to S$98,890. This is the highest since January 2013, when premiums closed at S$97,889.
        
        Motorcycle premiums closed at a record S$11,400, having risen from S$10,589 in the previous bidding exercise.
        
        COEs for commercial vehicles, which include goods vehicles and buses, rose to S$48,889 from S$46,501.
        
        A total of 2,941 bids were received, with a quota of 1,753 COEs available.
        """
    )

    st.header("Section E")
    st.markdown(
        """
        Some random content:
        Premiums for larger and more powerful cars in Category B rose from S$93,590 to S$94,889.
        
        For the Open category, which can be used for any vehicle type but end up being used mainly for large cars, prices went up from S$93,102 to S$98,890. This is the highest since January 2013, when premiums closed at S$97,889.
        
        Motorcycle premiums closed at a record S$11,400, having risen from S$10,589 in the previous bidding exercise.
        
        COEs for commercial vehicles, which include goods vehicles and buses, rose to S$48,889 from S$46,501.
        
        A total of 2,941 bids were received, with a quota of 1,753 COEs available.
        
        Some random content:
        Premiums for larger and more powerful cars in Category B rose from S$93,590 to S$94,889.
        
        For the Open category, which can be used for any vehicle type but end up being used mainly for large cars, prices went up from S$93,102 to S$98,890. This is the highest since January 2013, when premiums closed at S$97,889.
        
        Motorcycle premiums closed at a record S$11,400, having risen from S$10,589 in the previous bidding exercise.
        
        COEs for commercial vehicles, which include goods vehicles and buses, rose to S$48,889 from S$46,501.
        
        A total of 2,941 bids were received, with a quota of 1,753 COEs available.
        """
    )


    st.markdown("Click [Section B](#section-b)", unsafe_allow_html=True)
