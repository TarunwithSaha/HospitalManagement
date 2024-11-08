import streamlit as st

#---PAGE SETUP ---
eda_page = st.Page(
    page = "views/hospitalEDA.py",
    title="Hospital EDA",
    # icon ="",for icon we can use the materials library of Google
    default= True,# this makes this page as the default one i.e. when we load our web app this is the page that we will see
)

pne_page = st.Page(
    page = "views/pneumonia.py",
    title="Pneumonia Prediction",

)

dia_page = st.Page(
    page = "views/diabetes.py",
    title = "Diabetes Prediction",


)


#--- Now we can make the Navigation Menu ---

pg = st.navigation(pages=[eda_page,pne_page,dia_page])
#the above command is to create the navigation menu using the navigation feature


#---Run Navigation ---
pg.run()