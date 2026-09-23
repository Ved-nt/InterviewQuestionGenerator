import streamlit as st


def apply_global_style():
    st.markdown(
        """
        <style>

        /* =====================================================
           MAIN APPLICATION BACKGROUND
           ===================================================== */

        .stApp {
            background:
                radial-gradient(
                    circle at 10% 10%,
                    rgba(99, 102, 241, 0.15),
                    transparent 30%
                ),
                radial-gradient(
                    circle at 90% 20%,
                    rgba(6, 182, 212, 0.12),
                    transparent 30%
                ),
                radial-gradient(
                    circle at 50% 90%,
                    rgba(139, 92, 246, 0.10),
                    transparent 35%
                ),
                #070b14;
        }


        /* =====================================================
           SIDEBAR
           ===================================================== */

        section[data-testid="stSidebar"] {
            background:
                radial-gradient(
                    circle at 20% 10%,
                    rgba(99, 102, 241, 0.18),
                    transparent 35%
                ),
                radial-gradient(
                    circle at 80% 70%,
                    rgba(6, 182, 212, 0.12),
                    transparent 35%
                ),
                linear-gradient(
                    180deg,
                    #0d1324 0%,
                    #090d18 100%
                );

            border-right: 1px solid rgba(255, 255, 255, 0.08);
        }


        /* Sidebar text */

        section[data-testid="stSidebar"] * {
            color: rgba(255, 255, 255, 0.88);
        }


        /* Sidebar headings */

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            color: white;
        }


        /* Sidebar divider */

        section[data-testid="stSidebar"] hr {
            border-color: rgba(255, 255, 255, 0.08);
        }


        /* =====================================================
           MAIN HEADINGS
           ===================================================== */

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

            animation:
                gradientMove 6s linear infinite;
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


        /* =====================================================
           BUTTONS
           ===================================================== */

        .stButton > button {

            border-radius: 12px;

            border:
                1px solid
                rgba(139, 92, 246, 0.40);

            background:
                linear-gradient(
                    90deg,
                    rgba(99, 102, 241, 0.85),
                    rgba(139, 92, 246, 0.85),
                    rgba(6, 182, 212, 0.85)
                );

            color: white;

            font-weight: 700;

            transition:
                all 0.25s ease;
        }


        .stButton > button:hover {

            transform:
                translateY(-2px);

            box-shadow:
                0 8px 30px
                rgba(99, 102, 241, 0.35);
        }


        /* =====================================================
           METRICS
           ===================================================== */

        div[data-testid="stMetric"] {

            background:
                rgba(255, 255, 255, 0.035);

            border:
                1px solid
                rgba(255, 255, 255, 0.08);

            padding:
                15px;

            border-radius:
                14px;
        }


        /* =====================================================
           FILE UPLOADER
           ===================================================== */

        section[data-testid="stFileUploaderDropzone"] {

            background:
                rgba(255, 255, 255, 0.025);

            border:
                1px dashed
                rgba(139, 92, 246, 0.45);

            border-radius:
                14px;
        }


        /* =====================================================
           EXPANDERS
           ===================================================== */

        div[data-testid="stExpander"] {

            background:
                rgba(255, 255, 255, 0.025);

            border:
                1px solid
                rgba(255, 255, 255, 0.08);

            border-radius:
                12px;
        }


        /* =====================================================
           TEXT AREA
           ===================================================== */

        textarea {

            background:
                rgba(255, 255, 255, 0.035) !important;

            border:
                1px solid
                rgba(255, 255, 255, 0.08) !important;

            border-radius:
                10px !important;
        }


        /* =====================================================
           SELECTBOX / INPUTS
           ===================================================== */

        div[data-baseweb="select"] > div {

            background:
                rgba(255, 255, 255, 0.035);

            border:
                1px solid
                rgba(255, 255, 255, 0.08);

            border-radius:
                10px;
        }


        /* =====================================================
           ALERTS
           ===================================================== */

        div[data-testid="stAlert"] {

            border-radius:
                12px;
        }


        /* =====================================================
           FOOTER
           ===================================================== */

        .footer-text {

            text-align:
                center;

            color:
                rgba(255, 255, 255, 0.45);

            margin-top:
                60px;

            padding-bottom:
                20px;
        }


        /* =====================================================
           DIVIDERS
           ===================================================== */

        hr {

            border-color:
                rgba(255, 255, 255, 0.08);
        }


        </style>
        """,
        unsafe_allow_html=True
    )
