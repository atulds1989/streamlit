import streamlit as st

st.sidebar.title("this is side bar")
st.sidebar.button("click")
st.sidebar.radio('Gender', ['male', 'female'])


container = st.container()

container.write("inside the container")

st.write("outside the container")
