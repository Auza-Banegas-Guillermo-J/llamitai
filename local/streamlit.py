import streamlit as st
import time

import my_LLM as lm

def response_generator(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.1)

def get_key(route="./.key.txt"):
    with open(".key.txt") as key_file:
        key = key_file.read()
        #print("Using key : " + str(key))
    return key

st.title("LLamita :red[Bot] 🦙🤖", anchor=False)

if "messages" not in st.session_state:
    st.session_state.messages = []
    vectorstore, model, template = lm.init_module()
    st.session_state.vectorstore = vectorstore
    st.session_state.model = model
    st.session_state.template = template
    with st.chat_message(name = "guille_bot", avatar = "🦙"):
        st.write_stream(response_generator("Hola bola! Que tranza el dia de hoy?"))

for message in st.session_state.messages:
    with st.chat_message(name=message["role"],avatar=message["icon"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Soltar la sopa 👀"):
    st.chat_message(name = "llama_user", avatar = "🎩").markdown(prompt)
    st.session_state.messages.append({
        "role": "llama_user", 
        "content": prompt, 
        "icon": "🎩"
        })

    response = lm.get_answer(
        question = prompt, 
        template = st.session_state.template, 
        vectorstore = st.session_state.vectorstore, 
        model = st.session_state.model
        )
    with st.chat_message(name="guille_bot",avatar="🦙"):
        st.write_stream(response_generator(response))
    st.session_state.messages.append({
        "role": "guille_bot", 
        "content": response, 
        "icon": "🦙"
        })
