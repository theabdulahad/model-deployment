import streamlit as st
import joblib

st.title("Model Deployment")

male = st.radio("Are You Male?",["Yes","No"],horizontal=True)

if male == "Yes":
    gender=1
else:
    gender = 0

age = st.slider("Select Your Age : ")

cigsPerDay = st.number_input("Enter No.of Ciggarettes You Smoke Per Day ")

bmi = st.number_input("Enter Your BMI")

if st.button("Predict!"):
    model = joblib.load("model.h5")
    prediction=model.predict([[gender,age,cigsPerDay,bmi]])
    if prediction == ["Not At Risk"]:
        st.success("You are not at risk of getting heart disease in next 10 years")
    else:
        st.success("At Risk")
