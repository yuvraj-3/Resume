import streamlit as st

# Page config
st.set_page_config(
    page_title="Yuvraj's Resume",
    page_icon="🧠",
    layout="wide",
)

# Sidebar
with st.sidebar:
    st.image("https://avatars.githubusercontent.com/u/101135865?v=4", width=150)  # Your GitHub profile pic
    st.title("Yuvraj Kumar")
    st.markdown("**Final-year CSE (AI/ML)**")
    st.write("📍 Patna, Bihar")
    st.markdown("📧 yuvrajkumarsingh303@gmail.com")
    st.markdown("🔗 [GitHub](https://github.com/yuvraj-3)")
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/yuvraj5400/)")
    st.download_button("📄 Download Resume (PDF)", "Resume.pdf", file_name="c:\Users\yuvra\OneDrive\Desktop\gitdemo\Resume\Yuvraj_Kumar_AL150.pdf")

# Main title
st.title("📝 Yuvraj's Interactive Resume")
st.markdown("Welcome! This is a minimal interactive version of my resume built using **Streamlit**.")

# About Me
st.header("👨‍🎓 About Me")
st.info("Final-year B.Tech student in Computer Science (AI/ML) at DAV Public School. Passionate about machine learning, computer vision, and building cool stuff that works.")

# Projects
st.header("💼 Projects")

st.subheader("📹 Cinevo-AI Object Detection")
st.write("YOLOv5-based Streamlit app for detecting objects in images, videos, and webcam streams. Supports local inference without GPU.")

st.subheader("🎬 Movie Recommendation System")
st.write("Machine learning-based recommendation engine using collaborative and content-based filtering with Scikit-learn and Pandas.")

# Education
st.header("🎓 Education")
st.write("**DAV Public School**")
st.write("B.Tech in Computer Science – Artificial Intelligence & Machine Learning")

# Certifications
st.header("📜 Certifications")
st.markdown("- **CCNA: Introduction to Networks** – Cisco")
st.markdown("- **Data Science BootCamp** – GeeksforGeeks")

# Footer/End
st.markdown("---")
st.write("Built with ❤️ using [Streamlit](https://streamlit.io)")
