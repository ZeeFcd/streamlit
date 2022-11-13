import streamlit as st

if 'cam' not in st.session_state:
    st.session_state.cam = False

if 'picture1' not in st.session_state:
    st.session_state.picture1 = st.camera_input("Take a picture")
    st.session_state.cam = True

if st.session_state.cam in st.session_state:
    st.image(st.session_state.picture1)

