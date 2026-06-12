import streamlit as st
from predicat import predict_salary

st.title("Salary Prediction App")

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=25
)

experience = st.number_input(
    "Experience",
    min_value=0,
    max_value=50,
    value=1
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

education = st.selectbox(
    "Education",
    ["Bachelor", "High School", "Master", "PhD"]
)

location = st.selectbox(
    "Location",
    ["Rural", "Suburban", "Urban"]
)

job_title = st.selectbox(
    "Job Title",
    ["Engineer", "Manager", "Director"]
)

if st.button("Predict Salary"):

    salary = predict_salary(
        age,
        experience,
        gender,
        education,
        location,
        job_title
    )

    st.success(f"Predicted Salary: ₹{salary:,.2f}")