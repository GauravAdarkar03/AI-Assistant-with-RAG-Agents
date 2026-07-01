from fastapi import APIRouter

router = APIRouter()

@router.get("/question")
def generate_question():
    return {
        "response": "What is Kubernetes?",
        "tokens": {
            "prompt_tokens": 10,
            "completion_tokens": 15,
            "total_tokens": 25
        }
    }