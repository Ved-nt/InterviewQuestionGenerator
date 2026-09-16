import streamlit as st

from utils.style import apply_global_style


st.set_page_config(
    page_title="Interview Questions",
    page_icon="💬",
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

    st.caption(
        "Powered by Gemini"
    )


# ============================================================
# CHECK RESULT
# ============================================================

if "interview_result" not in st.session_state:

    st.warning(
        "No interview questions are available yet."
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

st.markdown("### ✦ STEP 03")

st.title("Interview Questions")

st.caption(
    "Personalized questions generated from your resume."
)

st.divider()


# ============================================================
# QUESTION SUMMARY
# ============================================================

total_questions = len(result.questions)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Total",
        total_questions
    )


with col2:

    st.metric(
        "Technical",
        st.session_state.get(
            "technical_questions",
            0
        )
    )


with col3:

    st.metric(
        "Project-Based",
        st.session_state.get(
            "project_questions",
            0
        )
    )


with col4:

    st.metric(
        "Behavioral + HR",
        (
            st.session_state.get(
                "behavioral_questions",
                0
            )
            +
            st.session_state.get(
                "hr_questions",
                0
            )
        )
    )


st.divider()


# ============================================================
# GROUP QUESTIONS
# ============================================================

categories = [
    "Technical",
    "Project-Based",
    "Behavioral",
    "HR"
]


for category in categories:

    category_questions = [
        question
        for question in result.questions
        if question.category.lower()
        == category.lower()
    ]


    if not category_questions:

        continue


    # ========================================================
    # CATEGORY HEADER
    # ========================================================

    st.markdown(
        f"## {category}"
    )

    st.caption(
        f"{len(category_questions)} question(s)"
    )


    # ========================================================
    # QUESTIONS
    # ========================================================

    for question_number, question in enumerate(
        category_questions,
        start=1
    ):

        with st.expander(
            f"{question_number}. {question.question}",
            expanded=False
        ):

            col1, col2 = st.columns(2)


            with col1:

                st.markdown(
                    f"**Category:** "
                    f"{question.category}"
                )


            with col2:

                st.markdown(
                    f"**Difficulty:** "
                    f"{question.difficulty}"
                )


            st.divider()


            st.markdown(
                "**Why might an interviewer ask this?**"
            )


            st.write(
                question.why_asked
            )


    st.divider()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<p class="footer-text">'
    'AI Interview Coach · Generated with Gemini'
    '</p>',
    unsafe_allow_html=True
)
