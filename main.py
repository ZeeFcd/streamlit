import streamlit as st


def take_picture():
    st.session_state.picture1 = st.camera_input("Take a picture of your hand")


def show_picture():
    st.image(st.session_state.picture1)


if 'picture1' not in st.session_state:
    st.session_state.picture1 = None


st.button('Take picture', on_click=take_picture)
st.button('Show picture', on_click=show_picture)
