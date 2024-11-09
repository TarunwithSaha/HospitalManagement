import pandas as pd 
import pandas.api.types as ptypes
#the above is to get to know the type of column
import numpy as np
import streamlit as st 
# from pandas_profiling import ProfileReport
#some issue with the above code for now 
from streamlit_pandas_profiling import st_profile_report
#  #this will allow us to use pandas profiling in the streamlit application
import matplotlib.pyplot as plt # this will import the pyplot from the matplotlib.pyplot
import pdfkit # this will import the pdfkit
import tempfile # this will import the tempfile
from datetime import datetime# this will import the datetime module for the streamlit webapp
#also installed wkhtmltopdf

st.markdown(
    """
    # **EDA on Hospital Data**
"""
)
# for above the '#' tells that it is heading one and the two astriks makes it bold 








#the below code is to upload the csv file
with st.sidebar.header('1.Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV")
    # st.sidebar.markdown('''
    # [Example CSV]()
    #                     ''')


#Pandas Profiling Report
if uploaded_file is not None:
    @st.cache_data
    
# In Streamlit, the @st.cache decorator is used to cache the output of a function, so that when the function is called with the same inputs, the results are reused rather than recalculated. This is especially useful when working with operations that are computationally expensive or time-consuming, such as loading large datasets or running complex computations.

# In your code, the @st.cache decorator is applied to the load_csv function:

# python
# Copy code
# @st.cache
# def load_csv():
#     csv = pd.read_csv(uploaded_file)
#     return csv
# Purpose of @st.cache in Your Code:
# Efficiency: If the file uploaded_file remains the same, load_csv() won’t need to reload the CSV from disk repeatedly; it will use the cached DataFrame instead.
# Performance: This caching improves performance in Streamlit apps, where reruns occur whenever a user interacts with widgets. Without caching, the file would be reloaded each time the app reruns, potentially slowing it down.
# Reducing Redundant Computation: If users toggle between views or perform other actions, Streamlit re-runs the code. Cached functions ensure that redundant computations are avoided.
















    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    # pr = ProfileReport(df,explorative =True)
    st.header('**Input Dataframe**')
    st.write(df)
    st.write('---')
    cl = df.columns.tolist()
    st.write("Please select any of the columns to get insights of the data in it ")
    st.write(cl)
    name = st.text_input("Please enter the required column:-")
    if name is not None:
        
        if name in cl:
            if ptypes.is_numeric_dtype(df[name]):
                #this will get passed if the type of data in the name column is of numeric type
                st.write(f"The columns name is {name}") #this will wrtie the name of the column
                mn = df[name].mean() # this will calculate the mean 
                med = df[name].median() # this will calculate the median
                md = df[name].mode()[0] if not df[name].mode().empty else 'No Mode' 
                # this will tell the mode of the column
                st.write(f"**Median** is :- {mn} ")
                #this will write the mean 
                st.write(f"The **Median** is :- {md}")
                #this will write the median
                st.write(f"The **Mode** is :- {md} ")
                #this will write the mode
                sum= df[name].describe()# this will describe the data
                st.write(f"The summary is {sum}") #this will write the summary


                #Grouped the numeric data into bins example intervals of 20
                bin_labels = ['0-20','20-40','40-60','60-80','80-100']
                df[name+" "]= pd.cut(df[name],bins=[0,20,40,60,80,100],labels=bin_labels)

                #counting the occurrences in each bin
                c_counts = df[name+" "].value_counts()



                

                st.title(f"Pie chart for the data in column {name}")
                #this will set the title for the pie chart 


                # now plotting the pie chart
                fig,ax = plt.subplots()
                ax.pie(c_counts,labels = c_counts.index,autopct = '%1.1f%%',startangle = 90)
                ax.axis('equal') # Equal aspect ratio ensures the pie chart is circular 

                st.pyplot(fig) #displaying the pie chart in streamlit 
                









                #Generating the report as HTML
                report_html  = f"""
                <h1> Analysis Report for {name}</h1>
                <p> <strong>Mean: </strong>{mn}</p>
                <p><strong>Median:</strong>{med}</p>
                <p><strong>Mode: </strong>{md} </p>

                """
                #Converting the pie chart to HTML image 
                with tempfile.NamedTemporaryFile(delete=False,suffix=".png") as tmpfile:
                    fig.savefig(tmpfile.name)
                    pie_chart_html = f'<img src ="file://{tmpfile.name}" width = "400"'
                report_html +=f"<h2>Pie Chart for {name}</h2>{pie_chart_html}"
                #PDF generation button
                if st.button("Download Analysis as PDF "):
                    #Save HTML to PDF 
                    config = pdfkit.configuration(wkhtmltopdf=r'"C:\Users\Tarun\Downloads\wkhtmltox-0.12.6-1.msvc2015-win64.exe"')
                    pdf_file =pdfkit.from_string(report_html,False,configuration=config)
                    c_time = datetime.now.strftime("%y-%m-%d %H:%M:%S")#this get the current time and will be used to distinguish between files
                    st.download_button(label="Download  PDF ", data=pdf_file, file_name=f"{name}_analysis_{c_time}.pdf",mime = "application/pdf")




            else:
                st.write(f"The columns name is {name}") # this will write the name of the column
            
        if name not in cl:
            st.write("The entered column is not in the list!!!")
    else:
        pass
else:
    st.info('Awaiting for CSV file to be uploaded')
    if st.button('Press to use the already uploaded dataset'):
        # @st.cache
        #this is for reading the csv file 
        df1 = pd.read_csv(r'C:\Users\HP\OneDrive\Desktop\Streamlit\HospitalManagement\archive\healthcare_dataset.csv')#here r is placed before for raw string 
        #here we droped the hospital column from the dataframe
        df= df1.drop('Hospital', axis = 1)
        st.write(df)  










#this feature is for uploading the data in csv format 
# with st.sidebar.header('Upload Your CSV data'):
#     uploaded_file = st.sidebar.file_uploader("Upload your csv file")
#     st.sidebar.markdown('''
#     [Example CSV input file](df)
#                         ''')

# if(uploaded_file==''):
#     st.write("Hello ")
# else:
#     st.write("Hi")
