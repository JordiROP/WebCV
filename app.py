import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from PIL import Image
from sections import timeline, about_me, footer
from constants import home
from utils import image_processing


st.set_page_config(page_title=home.PAGE_TITLE, page_icon=home.PAGE_ICON, layout="centered")
st.write('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css"/>',
         unsafe_allow_html=True)


with open(home.CSS_FILE) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(home.RESUME_FILE, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(home.PROFILE_PIC)

# --- HERO SECTION ---
with stylable_container(
        key="hero_container",
        css_styles="""
                {
                    border: 1px solid rgba(49, 51, 63, 0.2);
                    border-radius: 10px;
                    box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.06), 0 2px 5px 0 rgba(0, 0, 0, 0.2);
                }"""):
    col1, col2 = st.columns([1, 3], gap="small")
    with col1:
        st.markdown(f"""<img title="profile-image" class="profile-image" 
                        src="data:image/png;base64,{image_processing.image_to_bytes(home.PROFILE_PIC)}">""",
                    unsafe_allow_html=True)
    with col2:
        with st.container():
            with stylable_container(key="name-desc", css_styles="""{text-align: center; margin-top: 1rem}"""):
                st.markdown(home.NAME, unsafe_allow_html=True)
                st.markdown(home.DESCRIPTION, unsafe_allow_html=True)
            with stylable_container(key="resume", css_styles="""{text-align: center; margin-top: 1rem}"""):
                st.download_button(
                    label=" 📄 Download Resume",
                    data=PDFbyte,
                    file_name=home.RESUME_FILE.name,
                    mime="application/octet-stream",
                )
            with stylable_container(key="socials", css_styles="""{text-align: center; margin-top: 1rem}"""):
                st.markdown(
                    f"""
                    <a href='mailto:{home.SOCIAL_MEDIA[0]['link']}'>\t<i class='{home.SOCIAL_MEDIA[0]['icon']}'></i></a>
                    <a href='{home.SOCIAL_MEDIA[1]['link']}'>\t<i class='{home.SOCIAL_MEDIA[1]['icon']}'></i></a>
                    <a href='{home.SOCIAL_MEDIA[2]['link']}'>\t<i class='{home.SOCIAL_MEDIA[2]['icon']}'></i></a>
                    <a href='{home.SOCIAL_MEDIA[3]['link']}'>\t<i class='{home.SOCIAL_MEDIA[3]['icon']}'></i></a>""",
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
