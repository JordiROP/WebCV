import streamlit as st
from constants import tech_xp, academic_xp, education, others

from PIL import Image
from pathlib import Path

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
images_dir = current_dir / ".." / "assets" / "images"


def set_prof_experience():
    for field in tech_xp.FIELDS:
        st.subheader(field.get("subheader"), divider="gray")
        st.write(field.get("date"))
        if type(field.get("text")) == str:
            st.write(field.get("text"))
        else:
            for txt in field.get("text"):
                st.write(txt)


def set_academic_experience():
    st.header(academic_xp.HEADER_ACADEMIC_XP, divider="gray")

    for field in academic_xp.FIELDS:
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
    st.header(education.HEADER_UNI, divider="gray")
    for data in education.UNI_DATA:
        st.subheader(data.get("subheader"))
        st.write(data.get("date"))
        st.write(data.get("text"))

    st.header(education.HEADER_CFGS, divider="gray")
    st.subheader(education.SUBHEADER_DAM)
    st.write(education.DATE_DAM)
    st.write(education.TEXT_DAM)

    st.header(education.HEADER_OTHER, divider="gray")
    for course in education.COURSES:
        st.subheader(course.get("title"))
        st.write(course.get("description"))
        st.markdown("<a href='{}'>\t{}</a>".format(
            course.get("credential"), "Certificate"),
            unsafe_allow_html=True)


def set_additional_activities():
    for field in others.FIELDS:
        st.header(field.get("header"), divider="gray")
        if field.get("subheader"):
            st.subheader(field.get("subheader"))
        for text in field.get("text"):
            (st.markdown(text))
