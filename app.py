# app.py

import streamlit as st

st.set_page_config(page_title="Yuvraj's Resume", page_icon="🧠", layout="wide")

st.title("📝 Yuvraj's Interactive Resume")

st.subheader("👨‍🎓 About Me")
st.write("Final-year B.Tech student (CSE - AI/ML), passionate about machine learning, computer vision, and building cool stuff.")

st.subheader("💼 Projects")
st.markdown("- **Cinevo-AI Object Detection**: YOLOv5-based object detector with image, video, and webcam support.")
st.markdown("- **Movie Recommendation System**: ML model using collaborative and content-based filtering.")

st.subheader("🎓 Education")
st.write("DAV Public School | B.Tech in Computer Science (AI/ML)")

st.subheader("📜 Certifications")
st.markdown("- **CCNA: Introduction to Networks** – Cisco")
st.markdown("- **Data Science BootCamp** – GeeksforGeeks")

st.subheader("📫 Contact")
st.markdown("📧 yuvrajkumarsingh303@gmail.com")
st.markdown("🔗 [GitHub](https://github.com/yuvraj-3) | [LinkedIn](https://www.linkedin.com/in/yuvraj5400/)")

