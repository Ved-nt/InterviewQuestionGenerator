from typing import List

from pydantic import BaseModel, Field


class InterviewQuestion(BaseModel):
    question: str = Field(
        description="The interview question"
    )

    category: str = Field(
        description="Technical, Project-Based, Behavioral, or HR"
    )

    difficulty: str = Field(
        description="Easy, Medium, or Hard"
    )

    why_asked: str = Field(
        description="Why an interviewer may ask this question"
    )


class InterviewResponse(BaseModel):
    candidate_summary: str = Field(
        description="A short summary of the candidate based only on the resume"
    )

    key_skills: List[str] = Field(
        description="Important technical and professional skills found in the resume"
    )

    questions: List[InterviewQuestion] = Field(
        description="Personalized interview questions"
    )
