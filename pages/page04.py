import streamlit as st


def app():
    """
        What is this page for?
        """
st.title('Page 4') #set the title

st.header("Section A")

st.write('# This is a Page for Project Secret!')
st.write('## This is Page 04')
st.markdown(
    """
    This page demostrate the link to parts of the page. 
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
    """
)


st.markdown("Click [Section B](#section-b)", unsafe_allow_html=True)
