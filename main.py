import streamlit as st

# Add a heading to the page
st.title("Business Solution Provider")
# Initialize the UI with 2 columns

col1, col2 = st.columns(2)

with col1:
        st.markdown("Can't find the solution to your problem holding your business back? Don't worry we got you!")

with col2:

        st.image(image="graphic.jpeg",width=300)

st.markdown("###  Enter some details:")

col3,col4 = st.columns(2)

with col3:
    business = st.text_input(label="",placeholder="Business Category")

with col4:
    problem = st.text_input(label="",placeholder="Problem")









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
