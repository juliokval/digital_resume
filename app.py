from pathlib import Path

import streamlit as st
from PIL import Image

# ==== PATH SETTINGS ----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" /"main.css"
resume_file = current_dir / "assets" / "my resume.pdf"
profile_pic = current_dir / "assets" / "photo.jpeg"



# --- GENERAL SETTINGS ---
PAGE_TITLE = "👋🏾MY_DIGITAL CV   | Kabagamba Jules Valentin"
PAGE_ICON = "random"
NAME = "Kabagamba Jules Valentin"
DESCRIPTION = """
Automation and Robotics Student, I'm an IT analyst excelling in softwares Troubleshooting, HR analyst, Interested in Tech development and a passionate Volleyball player.
"""
EMAIL = "julesvalentin04@gmail.com"
SOCIAL_MEDIA = {
	"👑LINKEDIN": "https://www.linkedin.com/in/jules-valentin-kabagamba-7366621b5/?originalSubdomain=pl",
	"👑GITHUB": "https://github.com/juliokval",
	"👑INSTAGRAM": "https://www.instagram.com/jules_valentin.023/",

}
PROJECT = {
	"⚫🃏BLACK_JACK GAME - similar to casino black_jack but in python codes--a walkthrough of the game": "https://github.com/juliokval/mypython/blob/main/Blackjackgame.ipynb"
}





st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
	st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
	PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2,gap="small")
with col1:
	st.image(profile_pic, width=230)


with col2:
	st.title(NAME)
	st.write(DESCRIPTION)
	st.download_button(
		label="  📄 Download my Resume",
		data=PDFbyte,
		file_name=resume_file.name,
		mime="application/octet-stream",
		)
	st.write("🪪",EMAIL)
st.write("---")

# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (plateform,link) in enumerate(SOCIAL_MEDIA.items()):
	cols[index].write(f"[{plateform}]({link})")

st.write("---")



# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
	"""

-  ✅ 2years experience in Troubleshooting softwares and few coding skills from data and apps.
-  ✅ Strong hands on experience and knowledge in Microsoft package, information Tech and Control systems.
-  ✅ Excellent team-player and displaying strong sense of initiative on tasks.
"""

)

st.write("---")



# --- SKILLS ---
st.write("#")
st.subheader("Hard skills")
st.write(
	"""
- 💻 Programming: Python 
- 📊 Data Visulization: MS Excel
"""
)
st.write("---")



# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")

# --- JOB 1
st.write("👨🏾‍💻", "**IT analyst & HR analyst | HCL TECHNOLOGIES**")
st.write("04/2022 - Present")
st.write(
	"""
- ⏩ Use of  Extensive ticketing system, knowledge with Powershell and terminal in mac-os and command prompt for windows
- ⏩ use and tracking of KPIs needed to be used for the proper functionning of different softwares in different situations of debugging and functions.
- ⏩ Design of methods for resolving issues by 12% of impreoved predictions instead of escalating issues
"""
)

st.write("---")

# --- Projects ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECT.items():
	st.write(f"[{project}]({link})")









