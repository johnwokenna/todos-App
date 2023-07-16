import streamlit as st
import functions

st.title("My todo web app")
st.subheader("This is my first web app")
st.text("This is it")

todos = functions.get_todos()
st.checkbox("First checkbox")
st.checkbox("Second check box")
st.write("This app will be structured and modified")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")

