from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class TextInput(BaseModel):
    text: str

app = FastAPI(title="FastAPI Service",
             description="A sample FastAPI service ready for Render deployment",
             version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Service!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/text")
async def receive_text(input_data: TextInput):
    return {
        "received_text": input_data.text,
        "length": len(input_data.text),
        "status": "success"
    }
