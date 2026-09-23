import streamlit as st

from services.resume_parser import extract_text_from_pdf
from services.gemini_service import generate_interview_questions
from utils.prompts import create_interview_prompt
from utils.style import apply_global_style


st.set_page_config(
    page_title="Interview Setup",
    page_icon="⚙️",
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
# PAGE HEADER
# ============================================================

st.markdown("### ✦ STEP 01")

st.title("Interview Setup")

st.caption(
    "Upload your resume and configure the interview "
    "questions you want Gemini to generate."
)

st.divider()


# ============================================================
# RESUME UPLOAD
# ============================================================

st.markdown("## 📄 Upload your resume")

uploaded_file = st.file_uploader(
    "Choose your resume PDF",
    type=["pdf"]
)


if uploaded_file is not None:

    try:

        resume_text = extract_text_from_pdf(
            uploaded_file
        )

        if not resume_text:

            st.warning(
                "No text could be extracted from this PDF. "
                "Please upload a text-based PDF resume."
            )

            st.stop()


        st.success(
            f"Resume processed successfully — "
            f"{uploaded_file.name}"
        )


        # ====================================================
        # EXTRACTED TEXT
        # ====================================================

        with st.expander(
            "👁️ View extracted resume text"
        ):

            st.text_area(
                "Resume Content",
                resume_text,
                height=300,
                label_visibility="collapsed"
            )


        st.divider()


        # ====================================================
        # INTERVIEW CONFIGURATION
        # ====================================================

        st.markdown("## ⚙️ Interview Configuration")


        col1, col2, col3 = st.columns(3)


        with col1:

            job_role = st.selectbox(
                "Target Job Role",
                [
                    "Software Developer",
                    "Frontend Developer",
                    "Backend Developer",
                    "Full Stack Developer",
                    "Data Analyst",
                    "Data Scientist",
                    "Machine Learning Engineer"
                ]
            )


        with col2:

            seniority = st.selectbox(
                "Experience Level",
                [
                    "Fresher",
                    "Intern",
                    "Junior",
                    "Mid-Level"
                ]
            )


        with col3:

            difficulty = st.selectbox(
                "Difficulty",
                [
                    "Easy",
                    "Medium",
                    "Hard"
                ],
                index=1
            )


        # ====================================================
        # QUESTION DISTRIBUTION
        # ====================================================

        st.markdown(
            "## 📊 Question Category Distribution"
        )

        st.caption(
            "Choose how many questions you want from "
            "each interview category."
        )


        col1, col2, col3, col4 = st.columns(4)


        with col1:

            technical_questions = st.number_input(
                "Technical",
                min_value=0,
                max_value=50,
                value=10,
                step=1
            )


        with col2:

            project_questions = st.number_input(
                "Project-Based",
                min_value=0,
                max_value=50,
                value=5,
                step=1
            )


        with col3:

            behavioral_questions = st.number_input(
                "Behavioral",
                min_value=0,
                max_value=50,
                value=3,
                step=1
            )


        with col4:

            hr_questions = st.number_input(
                "HR",
                min_value=0,
                max_value=50,
                value=2,
                step=1
            )


        # ====================================================
        # TOTAL
        # ====================================================

        total_questions = (
            technical_questions
            + project_questions
            + behavioral_questions
            + hr_questions
        )


        st.divider()


        col1, col2 = st.columns(2)


        with col1:

            st.metric(
                "Total Questions",
                total_questions
            )


        with col2:

            if total_questions > 50:

                st.error(
                    "Maximum allowed questions is 50."
                )

            elif total_questions == 0:

                st.warning(
                    "Please select at least one question."
                )

            else:

                st.success(
                    "Distribution is ready."
                )


        # ====================================================
        # GENERATE
        # ====================================================

        st.divider()

        st.markdown("## ✨ Generate Interview")


        if total_questions > 50:

            st.error(
                "Please reduce the category distribution "
                "to 50 questions or fewer."
            )


        elif total_questions == 0:

            st.warning(
                "Please select at least one question."
            )


        else:

            if st.button(
                "✨ Generate Interview Questions",
                use_container_width=True
            ):

                prompt = create_interview_prompt(
                    resume_text=resume_text,
                    job_role=job_role,
                    seniority=seniority,
                    difficulty=difficulty,
                    technical_questions=technical_questions,
                    project_questions=project_questions,
                    behavioral_questions=behavioral_questions,
                    hr_questions=hr_questions
                )


                with st.spinner(
                    "🤖 Gemini is analyzing your resume..."
                ):

                    try:

                        result = (
                            generate_interview_questions(
                                prompt
                            )
                        )


                        # ====================================
                        # SAVE RESULT
                        # ====================================

                        st.session_state[
                            "interview_result"
                        ] = result


                        st.session_state[
                            "resume_text"
                        ] = resume_text


                        st.session_state[
                            "job_role"
                        ] = job_role


                        st.session_state[
                            "seniority"
                        ] = seniority


                        st.session_state[
                            "difficulty"
                        ] = difficulty


                        st.session_state[
                            "technical_questions"
                        ] = technical_questions


                        st.session_state[
                            "project_questions"
                        ] = project_questions


                        st.session_state[
                            "behavioral_questions"
                        ] = behavioral_questions


                        st.session_state[
                            "hr_questions"
                        ] = hr_questions


                        st.success(
                            "Interview questions generated successfully!"
                        )


                        st.info(
                            "Your AI analysis is now available "
                            "on the **AI Analysis** page."
                        )


                    except Exception as e:

                        st.error(
                            f"Gemini error: {str(e)}"
                        )


    except Exception as e:

        st.error(
            f"Could not process the resume: {str(e)}"
        )
