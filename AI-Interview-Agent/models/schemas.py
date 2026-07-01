from pydantic import BaseModel

class InterviewQuestion(BaseModel):
    question: str
    difficulty: str

class Evaluation(BaseModel):
    score: int
    strengths: list[str]
    weaknesses: list[str]
    missing_points: list[str]
    ideal_answer: str