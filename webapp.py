import streamlit as st
import functions


todos=functions.get_games()
st.set_page_config(layout='wide')

def add_todo():
    new_todo=st.session_state['new_todo'] + '\n'
    todos.append(new_todo)
    functions.write_games(todos)


st.title('My todos list')
st.subheader('This is to improve productivity')
st.write('This is to improve <b>productivity</b>',unsafe_allow_html=True)
abutton= st.button('Complete')



for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox and abutton:
        print(checkbox)
        todos.pop(index)
        functions.write_games(todos)
        del st.session_state[todo]
        st.experimental_rerun()



st.text_input(label='',placeholder='Add new todo',on_change=add_todo,key='new_todo')
