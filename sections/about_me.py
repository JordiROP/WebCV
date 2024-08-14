from constants import about_me
from utils.layout import boxed_element


def set_about_me():
    boxed_element(
        subheader=about_me.SUBHEADER_KNOW_ME,
        text=about_me.TEXT_KNOW_ME,
        key="about_me")
