#Importing the libraries
import streamlit as st
import pickle
from keras import preprocessing
from keras import applications
import numpy as np

#Declaring the title 
st.title('Predicting Pneumonia from the uploaded Image')

#Loading the model
with open(r'C:\Users\HP\OneDrive\Desktop\Streamlit\HospitalManagement\views\model_pickle','rb') as f:
    model=pickle.load(f)



#the below code is to upload the image
with st.sidebar.header('Upload your Image in JPEG format'):
    up_f=st.sidebar.file_uploader("Upload the image")



#Now processing the image for prediction
if up_f is not None:
    img = preprocessing.image.load_img(up_f,target_size=(224,224))
    x= preprocessing.image.img_to_array(img)
    x=np.expand_dims(x,axis=0)
    image_data = applications.vgg16.preprocess_input(x)
    classes = model.predict(image_data)
    if(classes[0][0]>classes[0][1]):
        st.write("Normal")
    else:
        st.write("Pneumonia Detected")
st.write("Pneumonia Page")