import streamlit as st

var = st.camera_input("Take a picture")
if 'picture1' not in st.session_state:
    st.session_state.picture1 = var

if 'picture1' in st.session_state:
    st.image(st.session_state.picture1)
    st.session_state.picture1 = var
