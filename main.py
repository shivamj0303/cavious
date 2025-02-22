from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import logging
from database import SessionLocal, engine
from models import Interaction, Base
from utils import get_intent_response

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Create database tables
Base.metadata.create_all(bind=engine)

# FastAPI app setup
app = FastAPI()

class TextInput(BaseModel):
    text: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/chat")
def chat(input_data: TextInput, db: Session = Depends(get_db)):
    user_text = input_data.text.lower()
    response = get_intent_response(user_text)
    
    # Save interaction to database
    db_interaction = Interaction(user_input=user_text, response=response)
    db.add(db_interaction)
    db.commit()
    
    # Logging request and response
    logger.info(f"User input: {user_text}")
    logger.info(f"Response: {response}")
    
    return {"response": response}