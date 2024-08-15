from pathlib import Path
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
CSS_FILE = current_dir / ".." / "styles" / "main.css"
RESUME_FILE = current_dir / ".." / "assets" / "cv.pdf"
PROFILE_PIC = current_dir / ".." / "assets" / "images" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Jordi Ricard Onrubia Palacios"
PAGE_ICON = ":desktop_computer:"
NAME = """<h1 style='text-align: center'>Jordi Ricard Onrubia Palacios</h1>"""
DESCRIPTION = """<p style='text-align: center'>Software & Data Engineer 💻 | Associated Professor 🏫 | 
                Ex-LleidaHacker ❤️</p>"""

SOCIAL_MEDIA = [
    {"icon": "fa-solid fa-3xl fa-envelope", "link": "jordirop.professional@gmail.com",
     "text": "jordirop.professional@gmail.com"},
    {"icon": "fa-brands fa-3xl fa-linkedin", "link": "https://www.linkedin.com/in/jordirop/", "text": "JordiROP"},
    {"icon": "fa-brands fa-3xl fa-github", "link": "https://github.com/JordiROP", "text": "JordiROP"},
    {"icon": "fa-brands fa-3xl fa-twitter", "link": "https://twitter.com/JordiRicardOnru", "text": "JordiRicardOnru"}
]