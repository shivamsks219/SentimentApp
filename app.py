import nltk
import streamlit as st
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentiments = SentimentIntensityAnalyzer()

def check(comment):
    sentiment_dict = sentiments.polarity_scores(comment)
    print(sentiment_dict['compound'])
    if sentiment_dict['compound'] >= 0.05 :
        return ("Positive")
    elif sentiment_dict['compound'] <= - 0.05 :
        return ("Negative")
    else :
        return ("Neutral")

def emoji(str):
    if(str=="Positive"):
        return ":smile:"
    elif(str=="Negative"):
        return ":angry:"
    else:
        return ":confused:"


st.markdown("# Sentiment Analyser")
with st.form("feedback_form"):
   st.write("Fill the Feedback Form")
   name=st.text_input("Enter Name")
   slider_val = st.slider("Rating", 0, 5)
   comment = st.text_area("Enter your Comments")
   checkbox_val = st.checkbox("Confirm")
   submitted = st.form_submit_button("Submit")
   if submitted and checkbox_val:
    st.markdown("### Sentiment : "+ check(comment)+" "+emoji(check(comment)))
    

st.write(" Programmed by Shivam Kumar :smile:")
st.markdown("Contact : shivamsks219@gmail.com")
st.markdown("LinkedIn : https://www.linkedin.com/in/shivam-kumar-sks/ ")
st.markdown("GitHub : https://github.com/shivamsks219/ ")
