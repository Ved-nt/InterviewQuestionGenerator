def create_interview_prompt(
    resume_text,
    job_role,
    seniority,
    difficulty,
    technical_questions,
    project_questions,
    behavioral_questions,
    hr_questions
):
    total_questions = (
        technical_questions
        + project_questions
        + behavioral_questions
        + hr_questions
    )

    prompt = f"""
You are an expert technical interviewer and career coach.

Your task is to analyze a candidate's resume and generate
personalized interview questions.

TARGET JOB ROLE:
{job_role}

EXPERIENCE LEVEL:
{seniority}

INTERVIEW DIFFICULTY:
{difficulty}

TOTAL NUMBER OF QUESTIONS:
{total_questions}

REQUIRED QUESTION DISTRIBUTION:
- Technical: {technical_questions}
- Project-Based: {project_questions}
- Behavioral: {behavioral_questions}
- HR: {hr_questions}

CANDIDATE RESUME:
-------------------------
{resume_text}
-------------------------

IMPORTANT INSTRUCTIONS:

1. Analyze the candidate's resume carefully.

2. Generate exactly {total_questions} questions.

3. Follow the requested category distribution EXACTLY:
   - Technical: exactly {technical_questions}
   - Project-Based: exactly {project_questions}
   - Behavioral: exactly {behavioral_questions}
   - HR: exactly {hr_questions}

4. Questions should be relevant to the target job role.

5. Questions should be based primarily on information actually
   present in the resume.

6. NEVER invent:
   - projects
   - internships
   - companies
   - technologies
   - certifications
   - work experience

7. Technical questions should test relevant technical knowledge.

8. Project-Based questions should focus only on projects
   actually mentioned in the resume.

9. Behavioral questions should be realistic interview questions
   related to teamwork, problem solving, challenges,
   communication, learning, and similar situations.

10. HR questions should be realistic placement/interview
    questions such as introduction, career goals, strengths,
    weaknesses, motivation, and role-related questions.

11. Match the requested difficulty level.

12. Avoid duplicate or nearly identical questions.

13. For every question, explain briefly why an interviewer
    might ask it.

14. Extract the candidate's most important skills.

15. Provide a short candidate summary.

16. If a technology appears in the resume, questions may test
    the candidate's understanding of that technology.

17. Do not judge or criticize the candidate.

18. Keep questions concise and interview-ready.

19. Return ONLY the requested structured JSON response.
"""

    return prompt
