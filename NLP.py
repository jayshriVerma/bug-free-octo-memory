import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import streamlit as st
from spacy.tokens import Token

nlp = spacy.load("en_core_web_sm")
spacy_text = SpacyTextBlob()
nlp.add_pipe(spacy_text)
text = "I am very happy today"

st.title("Sentiment analyser")
user_input = st.text_input("Text", text)
doc = nlp(user_input)

st.write("Polarity:", round(doc._.sentiment.polarity, 2))
st.write("Subjectivity:", round(doc._.sentiment.subjectivity, 2))
