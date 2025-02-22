from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import get_db, engine
from models import Base, Interaction
from intents import recognize_intent

app = FastAPI()


# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/ping")
def ping():
    return {"message": "Server is running"}

@app.post("/process")
def process_text(user_input: str, db: Session = Depends(get_db)):
    intent = recognize_intent(user_input)

    # Store interaction in DB
    interaction = Interaction(user_input=user_input, intent=intent)
    db.add(interaction)
    db.commit()

    return {"user_input": user_input, "intent": intent}