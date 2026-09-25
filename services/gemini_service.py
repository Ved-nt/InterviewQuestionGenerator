import os

import streamlit as st
from dotenv import load_dotenv
from google import genai

from models.interview_models import InterviewResponse


# Load variables from .env when running locally
load_dotenv()


# Get Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# If .env is not available, try Streamlit Secrets
if not GEMINI_API_KEY:
    try:
        GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    except Exception:
        GEMINI_API_KEY = None


GEMINI_MODEL = "gemini-3.6-flash"


def get_gemini_client():
    if not GEMINI_API_KEY:
        raise ValueError(
            "GEMINI_API_KEY is not configured. "
            "Please configure it in .env or Streamlit Secrets."
        )

    return genai.Client(api_key=GEMINI_API_KEY)


def generate_interview_questions(prompt):
    client = get_gemini_client()

    response_format = {
        "type": "text",
        "mime_type": "application/json",
        "schema": InterviewResponse.model_json_schema()
    }

    interaction = client.interactions.create(
        model=GEMINI_MODEL,
        input=prompt,
        response_format=response_format
    )

    if not interaction.output_text:
        raise ValueError("Gemini returned an empty response.")

    try:
        result = InterviewResponse.model_validate_json(
            interaction.output_text
        )

        return result

    except Exception as e:
        raise ValueError(
            f"Could not parse Gemini response: {str(e)}"
        )
