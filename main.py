from fastapi import FastAPI
from intents import recognize_intent
app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "Server is running"}

@app.post("/process")
def process_text(user_input: str):
    intent = recognize_intent(user_input)
    return {"user_input": user_input, "intent": intent}