from pathlib import Path

from constants import tech_xp, academic_xp, education, others
from utils.layout import boxed_element, boxed_element_group, multiboxed_element_group

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
images_dir = current_dir / ".." / "assets" / "images"


def set_prof_experience():
    count = 0
    for field in tech_xp.FIELDS:
        count += 1
        boxed_element(
            subheader=field.get("subheader"),
            date=field.get("date"),
            text=field.get("text"),
            key=f"prof_xp_{count}"
        )


def set_academic_experience():
    multiboxed_element_group(
        header=academic_xp.HEADER_ACADEMIC_XP,
        elements=academic_xp.FIELDS,
        key="academic_experience",
        extra_fields=["technologies"],
        images_dir=images_dir
    )


def set_education():
    boxed_element_group(
        elements=education.UNI_DATA,
        header=education.HEADER_UNI,
        key="education_uni"
    )

    boxed_element_group(
        elements=[{"subheader": education.SUBHEADER_DAM, "text": education.TEXT_DAM, "date": education.DATE_DAM}],
        header=education.HEADER_CFGS,
        key="education_cfgs"
    )

    boxed_element_group(
        elements=education.COURSES,
        header=education.HEADER_OTHER,
        key="education_others"
    )


def set_additional_activities():
    for field in others.FIELDS:
        boxed_element(
            key=field.get("header").lower().replace(" ", "_"),
            header=field.get("header"),
            subheader=field.get("subheader", None),
            text=field.get("text"),
            subheader_divider=None
        )
