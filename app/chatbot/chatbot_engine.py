from app.chatbot.intents import intents
from app.chatbot.responses import responses

def get_chatbot_response(user_message: str):

    message = user_message.lower()

    for intent, keywords in intents.items():
        for word in keywords:
            if word in message:
                return responses[intent]

    return {
        "message": "I can help you find safety equipment like helmets, gloves, masks, and shoes.",
        "products": []
    }