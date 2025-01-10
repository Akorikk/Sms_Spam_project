import streamlit as st
import pickle 
import re

import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

port_stem = PorterStemmer()



def stemming(text):
    stammed_contant = re.sub('[^a-zA-Z]', ' ', text)
    stammed_contant = stammed_contant.lower()
    stammed_contant = stammed_contant.split()
    stammed_contant = [port_stem.stem(word) for word in stammed_contant if word not in stopwords.words('english')]
    stammed_contant = ' '.join(stammed_contant) 

    return stammed_contant


cv = pickle.load(open("vectorizer.pkl","rb"))
model = pickle.load(open("model.pkl", "rb"))


st.title("SMS Spam Classifier")

input_sms = st.text_input("Enter Message")

if st.button('Predict'):

    # 1. preprocess
    transformed_sms = stemming(input_sms)
    # 2. vectorize
    vector_input = cv.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")


