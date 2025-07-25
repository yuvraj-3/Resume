import streamlit as st

# --- Page config ---
st.set_page_config(
    page_title="Yuvraj Kumar | Resume",
    page_icon="🧠",
    layout="wide"
)

# --- Sidebar ---
with st.sidebar:
    st.image("https://avatars.githubusercontent.com/u/101135865?v=4", width=150)
    st.title("Yuvraj Kumar")
    st.markdown("Final-year CSE (AI/ML) Student")
    st.write("📍 Patna, Bihar")
    st.write("📧 yuvrajkumarsingh303@gmail.com")
    st.markdown("[🔗 GitHub](https://github.com/yuvraj-3)")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/yuvraj5400/)")
    st.download_button(
        label="📄 Download Resume (PDF)",
        data=open("Yuvraj_Kumar_AL150.pdf", "rb").read(),
        file_name="Yuvraj_Kumar_Resume.pdf",
        mime="application/pdf"
    )

# --- Main Section ---
st.title("👋 Hi, I'm Yuvraj Kumar Singh")
st.markdown("Final-year **CSE (AI/ML)** student • Building intelligent systems and cool projects")

st.markdown("## 📖 About Me")
st.write(
    "I'm a passionate machine learning and computer vision enthusiast, currently pursuing B.Tech in Computer Science "
    "with specialization in AI & ML. I love solving real-world problems with code and always strive to learn new tech."
)

st.markdown("## 💼 Projects")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📹 Cinevo‑AI Object Detection")
    st.write("YOLOv5-based Streamlit app for detecting objects in images, videos, and webcam. Supports local CPU inference.")

with col2:
    st.subheader("🎬 Movie Recommendation System")
    st.write("Python ML project combining collaborative and content-based filtering to recommend personalized movies.")

st.markdown("🔗 [View All Projects on GitHub](https://github.com/yuvraj-3/Projects)")

st.markdown("## 🎓 Education")
st.write("**DAV Public School**")
st.write("B.Tech in Computer Science – Artificial Intelligence & Machine Learning")

st.markdown("## 📜 Certifications")
st.markdown("- **CCNA: Introduction to Networks** – Cisco")
st.markdown("- **Data Science BootCamp** – GeeksforGeeks")

st.markdown("---")
st.write("Made with ❤️ using [Streamlit](https://streamlit.io)")
