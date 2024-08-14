import streamlit as st
from streamlit_extras.stylable_container import stylable_container

from constants import about_me


def set_about_me():
    with stylable_container(
            key="about",
            css_styles="""
                            {  
                                border-radius: 10px;
                                box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.06), 0 2px 5px 0 rgba(0, 0, 0, 0.2);
                            }"""):
        with st.container(border=True):
            st.subheader(about_me.SUBHEADER_KNOW_ME, divider="gray")
            st.write(about_me.TEXT_KNOW_ME)
