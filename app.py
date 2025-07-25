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
        color: white;
    }}
    .block-container {{
        padding: 3rem 2rem 2rem;
    }}
    </style>
    """
    st.markdown(css_code, unsafe_allow_html=True)

add_bg_from_local("back.jpg")

# --- Header ---
st.title("👋 Hi, I'm Yuvraj Kumar")
st.markdown("Final-year **CSE (AI/ML)** student • Building intelligent systems and cool projects")

# --- Resume Download Button ---
with open("Yuvraj_Kumar_AL150.pdf", "rb") as file:
    resume_data = file.read()
st.download_button(
    label="📄 Download Resume (PDF)",
    data=resume_data,
    file_name="Yuvraj_Kumar_Resume.pdf",
    mime="application/pdf"
)

# --- About Me Section ---
st.markdown("## 🧠 About Me")
st.write(
    "I'm a passionate machine learning and computer vision enthusiast. "
    "I enjoy solving real-world problems, experimenting with intelligent systems, and turning ideas into working prototypes."
)

# --- Projects Section ---
st.markdown("## 💼 Projects")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📹 Cinevo‑AI Object Detection")
    st.image("obj.jpg", use_container_width=True)
    st.write("YOLOv5-based Streamlit app for detecting objects in images, videos, and webcam.")

with col2:
    st.subheader("🎬 Movie Recommendation System")
    st.image("frontend.png", use_container_width=True)
    st.write("Python ML project combining collaborative and content-based filtering to recommend movies.")

st.markdown("🔗 [View All Projects on GitHub](https://github.com/yuvraj-3/Projects)")

# --- Contact Me Section ---
st.markdown("## 📬 Contact Me")

st.markdown(
    """
    <style>
    .contact-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 2rem;
    }
    .contact-box a {
        color: #00CED1;
        text-decoration: none;
        font-weight: bold;
    }
    .contact-box a:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='contact-box'>
        <p>Feel free to reach out to me:</p>
        <ul>
            <li>📧 <a href='mailto:yuvrajkumarsingh303@gmail.com'>yuvrajkumarsingh303@gmail.com</a></li>
            <li>🔗 <a href='https://www.linkedin.com/in/yuvraj5400/' target='_blank'>LinkedIn</a></li>
            <li>💻 <a href='https://github.com/yuvraj-3' target='_blank'>GitHub</a></li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Footer ---
st.markdown("---")
st.write("Made with ❤️ using [Streamlit](https://streamlit.io)")
