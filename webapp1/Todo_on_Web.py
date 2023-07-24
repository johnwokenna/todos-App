import streamlit as St
import functions


todos = functions.get_todos()


def add_todo():
    todo_local = St.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)


St.title("My Todo on Web")
St.subheader("My first app on web")
St.write("This app is to increase my productivity")

for index, todo in enumerate(todos):
    checkbox = St.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del St.session_state[todo]
        St.experimental_rerun()

St.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')



