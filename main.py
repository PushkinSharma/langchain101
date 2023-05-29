import streamlit as st
st.header("Welcome to my first app!")

col1,col2 = st.columns(2)

with col1:
    st.write("lhs")


with col2:
    st.markdown("## Hi")
    st.write("rhs")


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
