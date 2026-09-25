import streamlit as st
from utils.style import apply_global_style

st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_global_style()

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(99, 102, 241, 0.18),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(6, 182, 212, 0.14),
                transparent 30%
            ),
            radial-gradient(
                circle at 50% 90%,
                rgba(139, 92, 246, 0.12),
                transparent 35%
            ),
            #070b14;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #0d1324 0%,
                #090d18 100%
            );
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    /* Main title */
    h1 {
        background:
            linear-gradient(
                90deg,
                #ffffff,
                #8b5cf6,
                #22d3ee,
                #ffffff
            );
        background-size: 300% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientMove 6s linear infinite;
    }

    @keyframes gradientMove {
        0% {
            background-position: 0% center;
        }

        50% {
            background-position: 100% center;
        }

        100% {
            background-position: 0% center;
        }
    }

    /* Buttons */
    .stButton > button {
        border-radius: 12px;
        border: 1px solid rgba(139,92,246,0.4);
        background:
            linear-gradient(
                90deg,
                rgba(99,102,241,0.85),
                rgba(139,92,246,0.85),
                rgba(6,182,212,0.85)
            );
        color: white;
        font-weight: 700;
        transition: all 0.25s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow:
            0 8px 30px rgba(99,102,241,0.35);
    }

    /* Metrics */
    div[data-testid="stMetric"] {
        background: rgba(255,255,255,0.035);
        border: 1px solid rgba(255,255,255,0.08);
        padding: 15px;
        border-radius: 14px;
    }

    /* Footer */
    .footer-text {
        text-align: center;
        color: rgba(255,255,255,0.45);
        margin-top: 60px;
        padding-bottom: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🤖 AI Interview Coach")

    st.caption(
        "Resume-based GenAI interview preparation"
    )

    st.divider()

    st.markdown("### Navigation")

    st.info(
        "Use the pages in the sidebar to move between "
        "Interview Setup, AI Analysis and Questions."
    )

    st.divider()

    st.markdown("### Project")

    st.caption(
        "GenAI-Powered Interview Question Generator"
    )
# ============================================================
# HERO
# ============================================================

st.markdown("###  GENAI • INTERVIEW PREPARATION")

st.title("AI Interview Coach")

st.markdown(
    """
    Turn your resume into personalized interview preparation.

    Upload your resume, configure your interview requirements,
    and generate questions tailored to your skills, projects,
    experience and target role.
    """
)


st.markdown("## How it works")


col1, col2, col3 = st.columns(3)

with col1:
    st.metric("01", "Setup")
    st.caption(
        "Upload your resume and configure the interview."
    )

with col2:
    st.metric("02", "Analyze")
    st.caption(
        "Gemini analyzes your resume and generates personalized questions."
    )

with col3:
    st.metric("03", "Practice")
    st.caption(
        "Review questions and prepare for your interview."
    )


st.divider()


st.markdown("## 🚀 Get Started")

st.write(
    "Use the **Interview Setup** page from the sidebar "
    "to upload your resume and start generating questions."
)


st.markdown(
    '<p class="footer-text">'
    'AI Interview Coach · GenAI College Project'
    '</p>',
    unsafe_allow_html=True
)
