#(FastAPI Backend)
from fastapi import FastAPI

from api.chat import router as chat_router
from api.upload import router as upload_router

#creates the FastAPI application.
app = FastAPI()

#"Load all APIs from chat.py"
app.include_router(chat_router)

#"Load all APIs from upload.py"
app.include_router(upload_router)

@app.get("/")
def home():
    return {
        "message": "AI Interview Agent"
    }

#RUN : uvicorn api:app --reload

# Open in your browser:
# http://127.0.0.1:8000
# http://127.0.0.1:8000/health
# http://127.0.0.1:8000/docs (Swagger UI)

#This is the heart of your backend.

