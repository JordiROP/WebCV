import streamlit as st
from PIL import Image
from sections import timeline, about_me, footer
from constants import home

st.set_page_config(page_title=home.PAGE_TITLE, page_icon=home.PAGE_ICON, layout="centered")
st.write('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css"/>',
         unsafe_allow_html=True)

with open(home.CSS_FILE) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(home.RESUME_FILE, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(home.PROFILE_PIC)

# --- HERO SECTION ---
col1, col2 = st.columns([1, 3], gap="small")
with col1:
    st.image(profile_pic, use_column_width="auto")
with col2:
    st.title(home.NAME)
    st.write(home.DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=home.RESUME_FILE.name,
        mime="application/octet-stream",
    )
    for social in home.SOCIAL_MEDIA:
        st.markdown("<i class='{}'></i><a href='mailto: {}'>\t{}</a>".format(
            social['icon'], social['link'], social['text']),
            unsafe_allow_html=True)

about, tech_xp, acad_xp, edu, add_act = st.tabs(["About Me",
                                                 "Professional Experience",
                                                 "Academic Experience",
                                                 "Education",
                                                 "Additional Activities"])

with about:
    about_me.set_about_me()
with tech_xp:
    timeline.set_prof_experience()
with acad_xp:
    timeline.set_academic_experience()
with edu:
    timeline.set_education()
with add_act:
    timeline.set_additional_activities()

footer.set_footer()
