import streamlit as st
from streamlit_extras.stylable_container import stylable_container

from constants import tech_xp, academic_xp, education, others

from PIL import Image
from pathlib import Path

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
images_dir = current_dir / ".." / "assets" / "images"


def set_prof_experience():
    count = 0
    for field in tech_xp.FIELDS:
        count += 1
        with stylable_container(
                key=f"prof_xp_{count}",
                css_styles="""
                                {  
                                    border-radius: 10px;
                                    box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.06), 0 2px 5px 0 rgba(0, 0, 0, 0.2);
                                }"""):
            with st.container(border=True):
                st.subheader(field.get("subheader"), divider="gray")
                st.write(field.get("date"))
                if type(field.get("text")) == str:
                    st.write(field.get("text"))
                else:
                    for txt in field.get("text"):
                        st.write(txt)


def set_academic_experience():
    with stylable_container(
            key=f"acad_xp",
            css_styles="""
                            {  
                                border-radius: 10px;
                                box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.06), 0 2px 5px 0 rgba(0, 0, 0, 0.2);
                            }"""):
        with st.container(border=True):
            st.header(academic_xp.HEADER_ACADEMIC_XP, divider="gray")
            count = 0
            count += 1
            for field in academic_xp.FIELDS:
                with stylable_container(
                        key=f"acad_xp_{count}",
                        css_styles="""
                                        {  
                                            border-radius: 10px;
                                            box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.06), 0 2px 5px 0 rgba(0, 0, 0, 0.2);
                                        }"""):
                    with st.container(border=True):
                        st.subheader(field.get("subheader"))
                        if type(field.get("text")) == str:
                            st.write(field.get("text"))
                        else:
                            for txt in field.get("text"):
                                st.write(txt)

                        st.write("Technologies:")
                        tech_cols = zip(field.get("tech"), st.columns(10, vertical_alignment="center"))
                        for element in tech_cols:
                            with element[1]:
                                st.image(Image.open(images_dir / element[0]))


def set_education():
    with stylable_container(
            key="uni",
            css_styles="""
                            {  
                                border-radius: 10px;
                                box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.06), 0 2px 5px 0 rgba(0, 0, 0, 0.2);
                            }"""):
        with st.container(border=True):
            st.header(education.HEADER_UNI, divider="gray")
            for data in education.UNI_DATA:
                st.subheader(data.get("subheader"))
                st.write(data.get("date"))
                st.write(data.get("text"))

    with stylable_container(
            key="cfgs",
            css_styles="""
                            {  
                                border-radius: 10px;
                                box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.06), 0 2px 5px 0 rgba(0, 0, 0, 0.2);
                            }"""):
        with st.container(border=True):
            st.header(education.HEADER_CFGS, divider="gray")
            st.subheader(education.SUBHEADER_DAM)
            st.write(education.DATE_DAM)
            st.write(education.TEXT_DAM)

    with stylable_container(
            key="cert",
            css_styles="""
                            {  
                                border-radius: 10px;
                                box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.06), 0 2px 5px 0 rgba(0, 0, 0, 0.2);
                            }"""):
        with st.container(border=True):
            st.header(education.HEADER_OTHER, divider="gray")
            for course in education.COURSES:
                st.subheader(course.get("title"))
                st.write(course.get("description"))
                st.markdown("<a href='{}'>\t{}</a>".format(
                    course.get("credential"), "Certificate"),
                    unsafe_allow_html=True)


def set_additional_activities():
    for field in others.FIELDS:
        with stylable_container(
                key="cert",
                css_styles="""
                                {  
                                    border-radius: 10px;
                                    box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.06), 0 2px 5px 0 rgba(0, 0, 0, 0.2);
                                }"""):
            with st.container(border=True):
                st.header(field.get("header"), divider="gray")
                if field.get("subheader"):
                    st.subheader(field.get("subheader"))
                for text in field.get("text"):
                    (st.markdown(text))
