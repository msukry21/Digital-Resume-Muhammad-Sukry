# Import Library
from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "doc" / "CV-Muhammad_Sukry.pdf"
profile_pic = current_dir / "doc" / "Muhammad_Sukry.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Muhammad Sukry"
PAGE_ICON = ":wave:"
NAME = "Muhammad Sukry"
DESCRIPTION = """
Perkenalkan nama saya Muhammad Sukry, 
saya adalah seorang mahasiswa Teknik Elektro Universitas Andalas dengan minat di Artificial Intelligence, Machine Learning, Programmable Logic Control,Automation Engineer, Instrumentation Engineer,Data Science, Programming,Internet Of Things,. 
Saya memiliki pengalaman basic electronic,control system, dan mengerjakan project di bidang IoT dan Artificial Intelligence
Saya juga seorang Mahasiswa yang sudah banyak mengikuti pelatihan terkait SCADA,PLC,Control System

"""
EMAIL = "msukry21@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/@muhammadsukry225",
    "LinkedIn": "https://www.linkedin.com/in/muhammad-sukry-71a743172/",
    "GitHub": "https://github.com/msukry21",
    "Instagram": "https://www.instagram.com/sukry_21_/",
}
PROJECTS = {
    "🏆 Monitoring And Controlling Agricultural Land ": "Ekowisata Sungkai Green Park Smart Farming",
    "🏆 Modeling For Chatbot Web app":"Python Flask",
    "🏆 Membuat Recommender System": " Jupyter Notebook",
    "🏆 Designing an Automated System in F&B Industry for Beverage Processing" : "EcoStructure Machine Expert Basic",

}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- Bagian pengaturan foto profile ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=270)
    st.write("Automation Engineer | Artificial Intelligence | Final Year Electrical Engineering at Andalas University")

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Curicullum Vitae",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Merancang Sistem Otomatis pada Industri F&B untuk Pengolahan Minuman: "EcoStructure Machine Expert Basic"
- ✔️ Pemrograman Intermediate PLC Modicon 221 : "EcoStructure Machine Expert Basic"
- ✔️ Merancang Sistem Kontrol Boiler: "WinCC Explorer"
- ✔️ 3 tahun berpengalaman dalam bidang Elektro.
- ✔️ Menguasai basic elektronika.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, Arduino, Matlab, C++
- 📊 Data Visulization: Tableu
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: MySQL
"""
)

# --- HISTORY ---
st.write('\n')
st.subheader("Experience")
st.write("---")

# --- JOB 1
st.write("🚧", "**Student Artificial Intelligence | PT Orbit Future Academy**")
st.write("2023 - Sekarang")

# --- JOB 2
st.write('\n')
st.write("🚧", "**Coordinator Practicum | Digital Control Laboratory**")
st.write("2022 - 2023")
st.write(
    """
- ► Mengatur dan mengawasi Praktikum.
- ► Time Management dan Team Management
- ► Berkomunikasi dan Mengajarkan materi praktikum.
"""
)

# --- Projects & Pencapaian ---
st.write('\n')
st.subheader("Projects & Pencapaian")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
