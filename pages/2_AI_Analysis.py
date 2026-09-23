import streamlit as st

from utils.style import apply_global_style


st.set_page_config(
    page_title="AI Analysis",
    page_icon="🎯",
    layout="wide"
)


# ============================================================
# APPLY GLOBAL STYLE
# ============================================================

apply_global_style()


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
# CHECK RESULT
# ============================================================

if "interview_result" not in st.session_state:

    st.warning(
        "No interview analysis is available yet."
    )

    st.info(
        "Go to **Interview Setup** and generate "
        "your interview questions first."
    )

    st.stop()


result = st.session_state["interview_result"]


# ============================================================
# HEADER
# ============================================================

st.markdown("### ✦ STEP 02")

st.title("AI Interview Analysis")

st.caption(
    "Gemini's analysis of your resume and "
    "interview requirements."
)

st.divider()


# ============================================================
# INTERVIEW CONFIGURATION
# ============================================================

st.markdown("## 🎯 Interview Configuration")


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Target Role",
        st.session_state.get(
            "job_role",
            "Not specified"
        )
    )


with col2:

    st.metric(
        "Experience",
        st.session_state.get(
            "seniority",
            "Not specified"
        )
    )


with col3:

    st.metric(
        "Difficulty",
        st.session_state.get(
            "difficulty",
            "Not specified"
        )
    )


st.divider()


# ============================================================
# CANDIDATE SUMMARY
# ============================================================

st.markdown("## 👤 Candidate Summary")

st.info(
    result.candidate_summary
)


# ============================================================
# KEY SKILLS
# ============================================================

st.markdown("## 🛠️ Key Skills")


if result.key_skills:

    skills_text = " · ".join(
        result.key_skills
    )

    st.success(
        skills_text
    )

else:

    st.caption(
        "No key skills were extracted."
    )


st.divider()


# ============================================================
# QUESTION DISTRIBUTION
# ============================================================

st.markdown("## 📊 Question Distribution")


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Technical",
        st.session_state.get(
            "technical_questions",
            0
        )
    )


with col2:

    st.metric(
        "Project-Based",
        st.session_state.get(
            "project_questions",
            0
        )
    )


with col3:

    st.metric(
        "Behavioral",
        st.session_state.get(
            "behavioral_questions",
            0
        )
    )


with col4:

    st.metric(
        "HR",
        st.session_state.get(
            "hr_questions",
            0
        )
    )


st.divider()


# ============================================================
# TOTAL
# ============================================================

st.markdown("## 📌 Preparation Overview")


total_questions = len(result.questions)


col1, col2 = st.columns(2)


with col1:

    st.metric(
        "Questions Generated",
        total_questions
    )


with col2:

    st.metric(
        "Skills Identified",
        len(result.key_skills)
    )


st.divider()


# ============================================================
# NEXT STEP
# ============================================================

st.markdown("## 💬 Ready to Practice?")


st.write(
    "Your personalized interview questions are ready. "
    "Open **Interview Questions** from the sidebar "
    "to start reviewing them."
)
