import streamlit as st

from pathlib import Path
from PIL import Image

from sections import timeline, about_me

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv.pdf"
profile_pic = current_dir / "assets" / "images" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Jordi Ricard Onrubia Palacios"
PAGE_ICON = ":desktop_computer:"
NAME = "Jordi Ricard Onrubia Palacios"
DESCRIPTION = """Software and Data Engineer"""

SOCIAL_MEDIA = [
    {"icon": "fa-solid fa-envelope", "link": "jordirop.professional@gmail.com", "text": "jordirop.professional@gmail.com"},
    {"icon": "fa-brands fa-linkedin", "link": "https://www.linkedin.com/in/jordirop/", "text": "JordiROP"},
    {"icon": "fa-brands fa-github", "link": "https://github.com/JordiROP", "text": "JordiROP"},
    {"icon": "fa-brands fa-twitter", "link": "https://twitter.com/JordiRicardOnru", "text": "JordiRicardOnru"}
]

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="centered")
st.write('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css"/>',
         unsafe_allow_html=True)
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns([1, 3], gap="small")
with col1:
    st.image(profile_pic, use_column_width="auto")
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    for social in SOCIAL_MEDIA:
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


footer = '</style> <div class="footer"> <p>Made with :heart: by Jordi Onrubia Palacios</p> </div>'
st.markdown(footer, unsafe_allow_html=True)