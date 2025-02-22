INTENT_RESPONSES = {
    "hello": "Hello! How can I assist you?",
    "time": "I can't tell time yet, but I can help with other things!",
    "weather": "I don't have live weather updates, but you can check a weather app!",
    "bye": "Goodbye! Have a great day!"
}

def get_intent_response(user_text: str) -> str:
    """Returns a response based on keyword matching."""
    for keyword, reply in INTENT_RESPONSES.items():
        if keyword in user_text:
            return reply
    return "I'm not sure how to respond to that."
