#(FastAPI Backend)
from fastapi import FastAPI
from api.chat import router as chat_router

app = FastAPI(
    title="AI Interview Agent",
    version="1.0.0"
)

app.include_router(chat_router)

@app.get("/")
def home():
    return {"message": "Welcome"}

@app.get("/health")
def health():
    return {"status": "Healthy"}
#RUN : uvicorn api:app --reload

# Open in your browser:
# http://127.0.0.1:8000
# http://127.0.0.1:8000/health
# http://127.0.0.1:8000/docs (Swagger UI)