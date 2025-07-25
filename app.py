import streamlit as st
import base64

# --- Page Config ---
st.set_page_config(
    page_title="Yuvraj Kumar | Resume",
    page_icon="🧠",
    layout="wide"
)

# --- Background Image ---
def add_bg_from_local(img_path):
    with open(img_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    css_code = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_string}");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }}
    </style>
    """
    st.markdown(css_code, unsafe_allow_html=True)

add_bg_from_local("back.jpg")

# --- Header ---
st.title("👋 Hi, I'm Yuvraj Kumar")
st.markdown("Final-year **CSE (AI/ML)** student • Building intelligent systems and cool projects")

# --- About Me Section ---
st.markdown("## 📖 About Me")
with st.expander("Click to read more about me"):
    st.markdown(
        """
        Hi, I'm Yuvraj Kumar Singh — a final-year B.Tech student in Computer Science with a specialization in Artificial Intelligence and Machine Learning, currently studying at **LNCTE, Bhopal (Madhya Pradesh)**.

        I was born and brought up in **Patna, Bihar**, and have always been curious about how machines think. My journey into programming began with C++, and over time I’ve grown passionate about solving real-world problems with AI, ML, and computer vision.

        I'm always building something new and love working on intelligent systems that actually make a difference.
        """
    )
    st.download_button(
        label="📄 Download Resume (PDF)",
        data=open("Yuvraj_Kumar_AL150.pdf", "rb").read(),
        file_name="Yuvraj_Kumar_Resume.pdf",
        mime="application/pdf"
    )

# --- Projects Section ---
st.markdown("## 💼 Projects")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📹 Cinevo‑AI Object Detection")
    st.write("YOLOv5-based Streamlit app for detecting objects in images, videos, and webcam.")
    st.markdown("[🔗 View Project](https://github.com/yuvraj-3/Projects)", unsafe_allow_html=True)
    st.image("obj.png", use_container_width=True, caption="Object Detection System")

with col2:
    st.subheader("🎬 Movie Recommendation System")
    st.write("Python ML project combining collaborative and content-based filtering to recommend movies.")
    st.markdown("[🔗 View Project](https://github.com/yuvraj-3/Projects)", unsafe_allow_html=True)
    st.image("frontend.png", use_container_width=True, caption="Movie Recommendation")

st.markdown("🔗 [View All Projects on GitHub](https://github.com/yuvraj-3/Projects)")

# --- Contact Me ---
st.markdown("---")
st.markdown("## 📫 Contact Me")

st.markdown(
    """
    <div style='font-size:16px; line-height:2'>
        📧 <a href="mailto:yuvrajkumarsingh303@gmail.com">yuvrajkumarsingh303@gmail.com</a><br>
        🔗 <a href="https://github.com/yuvraj-3" target="_blank">GitHub</a><br>
        🔗 <a href="https://www.linkedin.com/in/yuvraj5400/" target="_blank">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Footer ---
st.markdown("---")
st.write("Made with ❤️ using [Streamlit](https://streamlit.io)")
