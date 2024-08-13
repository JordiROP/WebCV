import streamlit as st
from constants import about_me


def set_about_me():
    st.subheader(about_me.SUBHEADER_ABOUT, divider="gray")
    st.write(about_me.TEXT_ABOUT)