#(FastAPI Backend)
from fastapi import FastAPI

app = FastAPI(
    title="AI Interview Agent",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "AI Interview Agent API is running."
    }

@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }