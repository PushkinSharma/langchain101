import streamlit as st

# Add a heading to the page
st.title("Business Solution Provider")
# Initialize the UI with 2 columns

col1, col2 = st.columns(2)

with col1:
        st.markdown("Can't find the solution to the problem holding your business back? Don't worry we got you! Just enter some basic information and we will provide you with a detailed solution.")

with col2:
        st.image(image="graphic.jpeg",width=300)

st.markdown("###  Enter some information:")

col1,col2 = st.columns(2)

with col1:
    business = st.text_input(label="",placeholder="Business Category")

with col2:
    problem = st.text_input(label="",placeholder="Problem")

st.markdown("### Solution:")







#sidebar

# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )
#
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )
