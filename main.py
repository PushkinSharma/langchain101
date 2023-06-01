import streamlit as st
from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain.llms import OpenAI
import openai
import os

load_dotenv()
api_key = os.environ.get('OPENAI_API_KEY')



template = """ HI

 business = {biz}

 problem = {prob}




 """

prompt = PromptTemplate(input_variables=["biz","prob"],template = template)

def load_llm():

    llm = OpenAI(temperature=0.5)
    return llm

llm = load_llm()



st.title("Business Solution Provider")

with st.sidebar:
     st.header("Langchain Overview: :parrot::link: ")
     st.markdown("LangChain is a software development framework designed to simplify the creation of applications using large language models.")
     st.header("Made By: :red[Pushkin Sharma]")
     st.write("This is my first Langchain project. I'm attempting to solve a very basic problem here.")



col1, col2 = st.columns(2)

with col1:
        st.markdown("Can't find the solution to the problem holding your business back? Don't worry I got you! Just enter some basic information and we will provide you with a detailed solution.")

with col2:
        st.image(image="vecteezy_illustration-vector-graphic-cartoon-character-of-business_5482438.jpg",width=300)

st.markdown("###  Enter some information:")


def get_business():

    business = st.text_input(label=":red[Business Category:]",placeholder="Finance")
    return business

def get_problem():

    problem = st.text_input(label=":red[Problem:]",placeholder="Insufficient leads")
    return problem


col1,col2 = st.columns(2)

with col1:

    business_input = get_business()

with col2:
    problem_input = get_problem()


st.markdown("### Solution:")

if business_input and problem_input:


    answer = llm(prompt.format(biz=business_input,prob=problem_input))
    #st.text_area(label="",value=answer)
    st.write(answer)
    #st.write(prompt.format(biz=business_input,prob=problem_input))

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

st.markdown("##### Happy with the result?")

col4,col5,col6,col7,col8,col9=st.columns(6)

with col4:
    st.button("Yes :smile:")

with col5:
    st.button("No :japanese_goblin:")
