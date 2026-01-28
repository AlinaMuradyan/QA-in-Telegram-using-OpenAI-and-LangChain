#!/usr/bin/env python
# coding: utf-8

from langchain_classic.chat_models import ChatOpenAI
from langchain_classic.chains import LLMChain
from langchain_classic.prompts import PromptTemplate
from langchain_classic.memory import ConversationBufferMemory

from config import OPENAI_API_KEY

user_memory = {}

llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model='gpt-4.1-nano',
    temperature=0
)

prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="""
You are a helpful assistant.

Conversation so far:
{chat_history}

User question:
{question}

Answer concisely.
"""
)

def get_chain(chat_id):
    if chat_id not in user_memory:
        user_memory[chat_id] = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

    memory = user_memory[chat_id]

    return LLMChain(
        llm=llm,
        prompt=prompt,
        memory=memory
    )

def ask_question(question, chat_id):
    chain = get_chain(chat_id)
    return chain.run(question)