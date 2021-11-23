import streamlit as st
from textblob import TextBlob
from annotated_text import annotated_text

#name of app
st.set_page_config(page_title='Sentiment Analyzer',page_icon='👽')

st.balloons()

#remove main menu and footer note
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
	content:'Made with ❤️ by om pramod'; 
	visibility: visible ;
}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#aligning title to center
st.markdown("<h1 style='text-align: center; color: voilet;font-family: Courier'>Real Time Sentiment Analyzer </h1>", unsafe_allow_html=True)

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

input = st.text_input("Enter a sentence...")
if st.button("Analyze text") :
    st.write(" ")
    st.write(" ")
    st.write(" ")
    edu = TextBlob(input)
    score = edu.sentiment.polarity
    if score==0:st.info("This message is Neutral 😐")
    elif score<0:st.info("This message is Negative 😫")
    elif score>0:st.info("This message is Positive 😀")