import streamlit as st
import functions


todos = functions.get_todos()
st.checkbox("First checkbox")
st.checkbox("Second check box")
st.write("This app will be structured and modified")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")

