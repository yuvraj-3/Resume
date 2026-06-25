
import streamlit as st
import base64

st.set_page_config(page_title="Yuvraj Kumar | Portfolio", page_icon="🧠", layout="wide")

def load_css():
    with open("style.css","r",encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def add_bg(img_path):
    with open(img_path,"rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(f"""
    <style>
    .stApp {{
        background-image:url("data:image/jpg;base64,{encoded}");
        background-size:cover;
        background-position:center;
        background-attachment:fixed;
    }}
    </style>
    """, unsafe_allow_html=True)

load_css()
add_bg("back.jpg")

st.markdown("""
<div class="hero">

<h4>👋 Hello, I'm</h4>

<h1>Yuvraj <span>Kumar</span></h1>

<h3>B.Tech CSE (AI & ML) Graduate • Python Developer • Machine Learning Enthusiast</h3>

</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

stats = [
    ("B.Tech", "Graduate"),
    ("Python", "Primary Language"),
    ("AI/ML", "Specialization"),
]

for col, (title, subtitle) in zip((c1, c2, c3), stats):
    with col:
        st.markdown(
            f"""
            <div class="stat">
                <h2>{title}</h2>
                <p>{subtitle}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
st.markdown("## 👨‍💻 About Me")
st.markdown("""
<div class="card">
I'm <b>Yuvraj Kumar </b>, 
            a Computer Science graduate specializing in Artificial Intelligence and Machine Learning.
            I enjoy building practical AI applications using Python, FastAPI, Machine Learning, and Computer Vision, 
            and I'm currently looking for opportunities where I can continue learning while contributing to real-world projects.
</div>
""",unsafe_allow_html=True)

st.download_button(
    "📄 Download Resume",
    open("Yuvraj_Kumar.pdf","rb").read(),
    "Yuvraj_Kumar.pdf",
    mime="application/pdf"
)

st.markdown("## 🚀 Skills")

st.markdown("""
<div style="display:flex;flex-wrap:wrap;gap:12px;">

<span class="skill">🐍 Python</span>
<span class="skill">⚡ FastAPI</span>
<span class="skill">🤖 Machine Learning</span>
<span class="skill">👁️ Computer Vision</span>
<span class="skill">📊 Pandas</span>
<span class="skill">🔢 NumPy</span>
<span class="skill">🧠 TensorFlow</span>
<span class="skill">📷 OpenCV</span>
<span class="skill">🐙 Git</span>
<span class="skill">💻 Streamlit</span>

</div>
""", unsafe_allow_html=True)
# =========================
# Featured Projects
# =========================

st.markdown("## 💼 Featured Projects")

col1, col2 = st.columns(2, gap="large")

# -------------------------
# Cinevo AI
# -------------------------
with col1:
    st.image("obj.png", use_container_width=True)

    st.markdown("### 🚗 Cinevo AI")

    st.write(
        "Real-time object detection application built using "
        "YOLOv5, OpenCV and Streamlit. Supports image, video "
        "and webcam detection."
    )

    st.markdown("""
    **Tech Stack**

    `Python` `YOLOv5` `OpenCV` `Streamlit`
    """)

    st.link_button(
        "💻 View Project",
        "https://github.com/yuvraj-3/Projects/tree/main/cinevo-AI",
        use_container_width=True
    )

# -------------------------
# Movie Recommendation
# -------------------------
with col2:
    st.image("frontend.png", use_container_width=True)

    st.markdown("### 🎬 Movie Recommendation System")

    st.write(
        "Machine Learning based movie recommendation system "
        "using content-based and collaborative filtering "
        "to recommend similar movies."
    )

    st.markdown("""
    **Tech Stack**

    `Python` `Pandas` `Scikit-learn` `Streamlit`
    """)

    st.link_button(
        "💻 View Project",
        "https://github.com/yuvraj-3/Projects/tree/main/Movie%20Recommendation%20System",
        use_container_width=True
    )

st.markdown("---")

st.markdown("## 📫 Contact")

a,b,c=st.columns(3)
with a:
    st.markdown('<div class="card">📧<br><b>Email</b><br>yuvrajkumarsingh303@gmail.com</div>',unsafe_allow_html=True)
with b:
    st.link_button("💻 GitHub","https://github.com/yuvraj-3")
with c:
    st.link_button("🔗 LinkedIn","https://www.linkedin.com/in/yuvraj5400/")

st.markdown("---")
st.markdown("<center>Made with ❤️ using Streamlit</center>",unsafe_allow_html=True)
