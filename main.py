from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from database import get_db, Message

class TextInput(BaseModel):
    text: str

class MessageResponse(BaseModel):
    id: int
    text: str
    timestamp: datetime

    class Config:
        from_attributes = True

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

@app.post("/text", response_model=MessageResponse)
async def receive_text(input_data: TextInput, db: Session = Depends(get_db)):
    # Create new message
    db_message = Message(text=input_data.text)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

@app.get("/texts", response_model=List[MessageResponse])
async def get_texts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    messages = db.query(Message).order_by(Message.timestamp.desc()).offset(skip).limit(limit).all()
    return messages
