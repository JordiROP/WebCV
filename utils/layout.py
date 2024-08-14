import streamlit as st
from PIL import Image
from streamlit_extras.stylable_container import stylable_container


def boxed_element(subheader: str, text: str, date: str = None, header: str = None, key: str = None, **kwargs):
    with stylable_container(
            key=key,
            css_styles="""
                            {  
                                border-radius: 10px;
                                box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.06), 0 2px 5px 0 rgba(0, 0, 0, 0.2);
                            }"""):
        with st.container(border=True):
            if header:
                st.header(header, divider=kwargs.get("header_divider", "gray"))
            if subheader:
                st.subheader(subheader, divider=kwargs.get("subheader_divider", "gray"))
            if date:
                st.write(date)
            if type(text) is str:
                st.write(text)
            else:
                for txt in text:
                    st.markdown(txt)


def boxed_element_group(elements: list, header: str = None, key: str = None, **kwargs):
    with stylable_container(
            key=key,
            css_styles="""
                            {  
                                border-radius: 10px;
                                box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.06), 0 2px 5px 0 rgba(0, 0, 0, 0.2);
                            }"""):
        with st.container(border=True):
            if header:
                st.header(header, divider=kwargs.get("header_divider", "gray"))
            for element in elements:
                if element.get("subheader", None):
                    st.subheader(element.get("subheader"))
                if element.get("date", None):
                    st.write(element.get("date"))
                if element.get("text", None):
                    st.write(element.get("text"))
                if element.get("credential", None):
                    st.markdown("<a href='{}'>\t{}</a>".format(element.get("credential"), "Certificate"),
                                unsafe_allow_html=True)


def multiboxed_element_group(header: str, elements: list, key: str, **kwargs):
    with stylable_container(
            key=key,
            css_styles="""
                        {  
                            border-radius: 10px;
                            box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.06), 0 2px 5px 0 rgba(0, 0, 0, 0.2);
                        }"""):
        with st.container(border=True):
            st.header(header, divider=kwargs.get("header_divider", "gray"))
            for field in elements:
                with stylable_container(
                        key=f"{key}_{field.get("subheader").lower().replace(" ", "_")}",
                        css_styles="""
                                        {  
                                            border-radius: 10px;
                                            box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.06), 0 2px 5px 0 rgba(0, 0, 0, 0.2);
                                        }"""):
                    with st.container(border=True):
                        st.subheader(field.get("subheader"), kwargs.get("header_divider", None))
                        if type(field.get("text")) == str:
                            st.write(field.get("text"))
                        else:
                            for txt in field.get("text"):
                                st.write(txt)

                        for extra in kwargs.get("extra_fields", []):
                            st.write(str(extra).capitalize())
                            tech_cols = zip(field.get(extra), st.columns(10, vertical_alignment="center"))
                            for element in tech_cols:
                                with element[1]:
                                    st.image(Image.open(kwargs.get("images_dir", None) / element[0]))
