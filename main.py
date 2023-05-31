import streamlit as st

st.title("Business Solution Provider")

with st.sidebar:
     st.header("Langchain Overview: :parrot::link: ")
     st.markdown("LangChain is a software development framework designed to simplify the creation of applications using large language models.")
     st.header("Made By: :red[Pushkin Sharma]")
     st.write("This is my first Langchain project. I'm attempting to solve a very basic problem here.")



col1, col2 = st.columns(2)

with col1:
        st.markdown("Can't find the solution to the problem holding your business back? Don't worry we got you! Just enter some basic information and we will provide you with a detailed solution.")

with col2:
        st.image(image="vecteezy_illustration-vector-graphic-cartoon-character-of-business_5482438.jpg",width=300)

st.markdown("###  Enter some information:")

col1,col2 = st.columns(2)

with col1:
    business = st.text_input(label="",placeholder="Business Category")

with col2:
    problem = st.text_input(label="",placeholder="Problem")


st.markdown("### Solution:")



st.markdown("##### Happy with the result?")

col4,col5,col6,col7,col8,col9=st.columns(6)

with col4:
    st.button("Yes :smile:")

with col5:
    st.button("No :japanese_goblin:")
