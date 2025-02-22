def recognize_intent(text: str):
    text = text.lower()
    
    # Basic keyword-based intent recognition
    if "hello" in text or "hi" in text:
        return "greeting"
    elif "weather" in text:
        return "weather_query"
    elif "time" in text:
        return "time_query"
    else:
        return "unknown"
