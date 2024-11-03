import streamlit as st
import functions
from streamlit import checkbox, session_state

todos=functions.readfile()
def add_todo():
    todo = st.session_state["new todo"]+"\n"
    todos.append(todo)
    functions.write_todo(todos)

st.title("My Todo Project")
st.subheader("Explore python")
st.write("hii there")
for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="add new",
              on_change=add_todo,key="new todo")

