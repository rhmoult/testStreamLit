import streamlit as st
st.title("Hello World")
x = st.slider("Select a value", 0, 10)
st.write(f"Value: {x}")
