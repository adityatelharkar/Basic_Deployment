import streamlit as st
import time as t


#Title
st.title("Welcome to My First Interface")
#image
st.image("pngbharatlogo.png")
#Header
st.header("Bharat Software Solutions")

#SubHeader
st.subheader("Email-info@bharatsoftwaresol.in")
#info
st.info("We are in Trainings as well as Development")

#warning Massage
st.warning("our Updated location is at baner pl note")

#write
st.write("Employee Name")

#Error Massege
st.error("Invalid")

#Sucess Massege
st.success("Everything look Good..!!")

#Markdown
st.markdown("Hello All")
st.markdown(":moon:")
st.markdown(":Sun:")

##Text,Caption

#to Display Mathamatical Equation

st.latex(r'''a+b x^2+c''')
st.latex(r'''y=mx+c''')

#checkBox
st.checkbox("Login")

#Button
st.button("Click")

#radio
st.radio("Gender",["Male","Female"])

#Selectbox
st.selectbox("Select Your Course",["Analytics","Machine Learning","Python"])

#MultiSelectBox
st.multiselect("Choose Multiple",["a","B","C"])

#select Slider&Slider
st.select_slider("Slider",["Good","Better","Best"])

st.slider("Rating",0,100)

#Number Input

st.number_input("select Number",0,100)

#text Input
st.text_input("Enter Email")

#date input
st.date_input("select Date")

#text Area
st.text_area("Describe yourself")

#File Upload
st.file_uploader("Upload Your File")
#choose Color
st.color_picker("Color")

#progress Tracker
st.progress(90)

with st.spinner("Wait........................"):
    t.sleep(1)

st.balloons()

#sidebar

st.sidebar.title("WELCOME")
st.sidebar.text_input("Enter E-mail")
st.sidebar.text_input("Password")
st.sidebar.button("Submit")
st.sidebar.selectbox("Gender",["Male","Female"])


import pandas as pd
import numpy as np
st.title("Bar Chart")
data=pd.DataFrame(np.random.randn(50,2),columns=["X","Y"])
st.bar_chart(data)

st.title("Scatter Plot")
st.scatter_chart(data)

st.line_chart(data)
st.area_chart(data)