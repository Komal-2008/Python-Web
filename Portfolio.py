import streamlit as st

#personal details
st.title("Student Portfolio")

st.header("Personal Information")

name=st.text_input("Enter Your Name")

dob=st.text_input("Enter Date of Birth")

city=st.text_input("Enetr City")

email=st.text_input("Enter Email")

hobbies=st.text_input("Enetr Hobbies")

#Academic Details
st.header("Academic Information")

college=st.text_input("Enter College Name")

course=st.selectbox(
    "Course",
    ["Diploma","B.Tech","BCA"]
)

Branch=st.selectbox(
    "Branch",
    ["Computer","Mechanical","Civil","Electrical","Electronics",]
)

sem=st.selectbox(
    "Semester",
    [1,2,3,4,5,6,7,8]
)

cgpa=st.text_input("CGPA")

Skill=st.text_input("Skill")

futur=st.text_area("Write about your futur Plans")

goal=st.text_area("Explain what you want to become in the future and why")

submit=st.button("Submit")

if submit:
    st.header("Submitted Information")

    st.header("Personal Information")
    st.write("Name :", name)
    st.write("Date Of Birth :", dob)
    st.write("City :", city)
    st.write("Email :", email)
    st.write("Hobbies :", hobbies)

    st.header("Academic Information")
    st.write("College Name :", college)
    st.write("Cource :", course)
    st.write("Branch :", Branch)
    st.write("Semester :", sem)
    st.write("CGPA :",cgpa)
    st.write("Skill :", Skill)
    st.write("Futur Plans :", futur)
    st.write("Goals :", goal)