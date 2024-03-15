from itertools import zip_longest
import streamlit as st
from streamlit_chat import message
from langchain.chat_models import ChatOpenAI
from langchain.schema import (SystemMessage,HumanMessage,AIMessage)
chabhi_key = st.secrets["chabhi_api_key"]
st.set_page_config("welcome to AI world")
st.title("AI helper")
if 'generated'not in st.session_state:
    st.session_state['generated']=[]
if'past'not in st.session_state:
    st.session_state['past']=[]
if'entered_prompt'not in st.session_state:
    st.session_state['entered_prompt']=""
chat=ChatOpenAI(temperaturte=0.1,model_name="gpt-3.5-turbo",openai_api_key=chabhi_key)
def buid_message_list():
    """ek list jisame system,human,ai message rakhe hai"""
    zipped_messages=[SystemMessage(content="you have double phd degree in computer science and Artificial intelligence.And working on recent research on recent AI published paper globely")]
    for human_msg,ai_msg in zip_longest(st.session_state['past'],st.session_state['generated']):
        if human_msg is not None:
            zipped_messages.append(HumanMessage(content=human_msg))
        if ai_msg is not None:
            zipped_messages.append(AIMessage(content=ai_msg))
            return zipped_messages
def generated_response():
    """chatGPT se response generate karwate hai"""
    zipped_messages=buid_message_list()
    ai_response=chat(zipped_messages)
    return ai_response.content
def submit():
    st.session_state.entered_prompt=st.session_state.prompt_input
    st.session_state.prompt_input=""
    st.text_input('you:',key='prompt_input',on_change=submit)
    if st.session_state.entered_prompt !="":
        user_input=st.session_state.entered_prompt
        st.session_state.past.append(user_input)
        if st.session_state['generated']:
            for i in range(len(st.session_state['generated']-1,-1,-1)):
                message(st.session_state['generated'][i],key=str(1))
                message(st.session_state['past'][i],is_user=True,key=str[i]+'_user')