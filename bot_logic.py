# In bot_logic.py
import json
import random
import datetime

# A simple "memory" to store the user's name
user_data = {"name": None}

def load_knowledge_base(file_path):
    """Loads the knowledge base from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def handle_math_query(user_input):
    """Parses and calculates a simple math expression."""
    try:
        # Remove any leading "what is" or similar phrases
        expression = user_input.replace("what is", "").replace("calculate", "").strip()
        # Evaluate the expression safely
        # Note: 'eval' is powerful but can be risky with untrusted input.
        # For a simple chatbot, it's generally fine, but for production,
        # a safer parser is recommended.
        result = eval(expression)
        return f"The answer is {result}."
    except Exception:
        return "I can't calculate that. Please provide a simple math problem (e.g., 5 + 3)."

def get_bot_response(user_input, knowledge_base):
    """Finds a matching response from the knowledge base."""
    normalized_input = user_input.lower()
    
    # Check for math intent first
    if any(word in normalized_input for word in ["calculate", "what is", "+", "-", "*", "/"]):
        return handle_math_query(normalized_input)

    # Check for time intent
    if any(p in normalized_input for p in knowledge_base["time_query"]["patterns"]):
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."
    
    # Check for name input
    if "my name is" in normalized_input or "i'm called" in normalized_input:
        name = normalized_input.split("is")[-1].strip().capitalize()
        user_data["name"] = name
        return f"Nice to meet you, {name}!"

    # Iterate through general knowledge base items
    for intent, data in knowledge_base.items():
        if data["responses"] and any(pattern in normalized_input for pattern in data["patterns"]):
            return random.choice(data["responses"])
    
    # Return a default response if no pattern is found
    return "I'm sorry, I don't understand that. Can you try rephrasing?"