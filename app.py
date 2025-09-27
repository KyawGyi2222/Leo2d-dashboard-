import streamlit as st

st.title("Leo2d Dashboard")
st.write("Welcome to Leo2d percent viewer!")

percent = st.slider("Select percent:", 0, 100, 50)
st.write(f"Your percent is: {percent}%")
