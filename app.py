#import groq
import streamlit as st
#phase 2 import
import os
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langchain.memory import ChatMessageHistory
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())
groq_api_key= os.getenv("GROQ_API_KEY")
#client= groq.Groq()
st.title("_US Visa Consultant_ by :green[ARKESHA]:flag-us:")
# use session set for track status to hold values of chat_message user
# Initialize memory
if "memory" not in st.session_state:
    st.session_state.memory = ChatMessageHistory()
if "messages" not in st.session_state:
    st.session_state["messages"]=[]
#display old history
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).markdown(msg["content"])

prompt= st.chat_input("Ask me anything")
if prompt:
    st.chat_message("user").markdown(f"{prompt}")
    st.session_state["messages"].append({"role":"user","content":prompt})
    st.session_state.memory.add_user_message(prompt)  # Add to LangChain memory
    groq_sys_prompt=ChatPromptTemplate.from_messages([("system","""you are work as professional USA immegrant visa counsltant.
                                                             you are expert in providing latest information related to US visa & immegrant policy of 2025.  
                                                            provide the accurate and precise answers. 
                                                            and also guide the user for visa related 
                                                            process through key highlights in brief.provide the answer
                                                        in well defined structured format.if you don't have the information in your knowledge base & you are not that much confident to provide the answer as of 2025 information,reply
                                                        i don't have the information.or 
                                                       for more information you can visit "https://travel.state.gov/content/travel/en/us-visas/visa-information-resources/all-visa-categories.html" """),
                                                           MessagesPlaceholder(variable_name="history"),
    ("human", "{user_input}")
    ])
    model="llama-3.3-70b-versatile"
    groq_chat=ChatGroq(
        api_key=groq_api_key,
        model_name=model
    )
    
    chain= groq_sys_prompt | groq_chat | StrOutputParser()
    #response= chain.invoke({"user_input":prompt})
    response = chain.invoke({
        "user_input": prompt,
        "history": st.session_state.memory.messages  # Pass conversation history
    })
    #response="Hi, I'm your Asssistant"
    st.chat_message("assistant").markdown(f"{response}")
    st.session_state["messages"].append({"role":"assistant","content":response})
    st.session_state.memory.add_ai_message(response) 
