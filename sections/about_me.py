import streamlit as st
from constants import about_me


def set_about_me():
    st.subheader(about_me.SUBHEADER_KNOW_ME, divider="gray")
    st.write(about_me.TEXT_KNOW_ME)
