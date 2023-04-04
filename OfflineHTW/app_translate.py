from google_trans_new import google_translator  
import streamlit as st
import easyocr
import pyttsx3
from PIL import Image
import cv2
import numpy as np
import os, io
from google.cloud import vision
from google.cloud.vision_v1 import types
import pandas as pd




def display_text(bounds):
    text = []
    for x in bounds:
        t = x[1]
        text.append(t)
    text = ' '.join(text)
    return text






st.sidebar.title('Language Selection Menu')
st.sidebar.subheader('Select...')
src = st.sidebar.selectbox("From Language", ['English','Chinese WIP'])


helper = {'English':'en', 'Assamesse':'as', 'Bihari':'bh', 'Bhojpuri':'bho', 'Bengali':'bn', 'Hindi':'hi',
          'Maithili':'mai', 'Marathi':'mr','Nagpuri':'sck', 'Tamil':'ta', 'Telugu':'te', 'Urdu':'ur'}
# dst = helper[destination]
source = helper[src]


st.set_option('deprecation.showfileUploaderEncoding', False)
st.title(' Handwriting Recognition System')
st.subheader('Handwriting Recognition using Machine Learning')
st.text('Select Language from the Sidebar.')

#html_string = "<input type="file" id="img" name="img" accept="image/*">"
#st.markdown(html_string, unsafe_allow_html=True)

image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg', 'JPG'])



if st.button("Convert",key=1):

    if image_file is not None:

        
        img = Image.open(image_file)
        img = np.array(img)

        st.subheader('Image you Uploaded...')
        st.image(image_file, width=450)

        if src == 'English':
            image_name = image_file.name
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'/Users/oussamatamraoui/Documents/HandwritingProjects/ServiceAccountToken.json'
            client = vision.ImageAnnotatorClient()
            FILE_PATH = os.path.join("/Users/oussamatamraoui/Documents/HandwritingProjects/Images", image_name)

            with io.open(FILE_PATH, 'rb') as image_file:
                content = image_file.read()

            image = vision.Image(content=content)
            response = client.document_text_detection(image=image)

            
            
            with st.spinner('Extracting Text from given Image'):
                docText = response.full_text_annotation.text
                st.subheader('Google Deployment')
                st.text(docText)
                translator = google_translator()  
                translate_text = translator.translate(docText,lang_tgt='zh-CN') 
                st.subheader('Translation of text to Chinese')
                st.text(translate_text)
                eng_reader = easyocr.Reader(['en'])
                detected_text = eng_reader.readtext(img)
                st.subheader('Nvidia CUDA Deployment')
                text = display_text(detected_text)
                st.write(docText)

                


    
    else:
        st.subheader('Image not found! Please Upload an Image.')


