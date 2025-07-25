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

# --- Sidebar ---
# --- Sidebar ---
with st.sidebar:
    st.markdown(
        """
        <style>
        .sidebar-content {
            text-align: center;
            padding-top: 20px;
        }
        .sidebar-content img {
            border-radius: 50%;
            margin-bottom: 15px;
        }
        .sidebar-links a {
            display: block;
            margin: 5px 0;
            font-weight: 500;
            color: #4a4a4a;
            text-decoration: none;
        }
        .sidebar-links a:hover {
            color: #1f77b4;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.image("https://avatars.githubusercontent.com/u/101135865?v=4", width=120)
    st.markdown("### Yuvraj Kumar")
    st.markdown("Final-year CSE (AI/ML) Student")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="sidebar-links">', unsafe_allow_html=True)
    st.markdown("[💻 GitHub](https://github.com/yuvraj-3)", unsafe_allow_html=True)
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/yuvraj5400/)", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### 📄 Resume")
    st.download_button(
        label="Download Resume",
        data=open("Yuvraj_Kumar_AL150.pdf", "rb").read(),
        file_name="Yuvraj_Kumar_Resume.pdf",
        mime="application/pdf"
    )

# --- Main Content ---
st.title("👋 Hi, I'm Yuvraj Kumar ")
st.markdown("Final-year **CSE (AI/ML)** student • Building intelligent systems and cool projects")

st.markdown("## 📖 About Me")
st.write(
    "I'm a passionate machine learning and computer vision enthusiast. "
    "I enjoy solving real-world problems, experimenting with intelligent systems, and turning ideas into working prototypes."
)

st.markdown("## 💼 Projects")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📹 Cinevo‑AI Object Detection")
    st.write("YOLOv5-based Streamlit app for detecting objects in images, videos, and webcam.")

with col2:
    st.subheader("🎬 Movie Recommendation System")
    st.write("Python ML project combining collaborative and content-based filtering to recommend movies.")

st.markdown("🔗 [View All Projects on GitHub](https://github.com/yuvraj-3/Projects)")

st.markdown("---")
st.write("Made with ❤️ using [Streamlit](https://streamlit.io)")
