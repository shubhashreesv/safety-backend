from .keyword_search import keyword_search
from .semantic_search import semantic_intent
from .responses import RESPONSES


def get_chatbot_response(message: str, db):

    product_matches = keyword_search(message, db)

    if product_matches:
        return {
            "intent": "product_search",
            "response": "✅ Yes, we have the following safety products available:",
            "products": product_matches
        }

    intent = semantic_intent(message)

    response_data = RESPONSES.get(intent)

    if response_data:
        return {
            "intent": intent,
            "response": response_data["response"],
            "products": []
        }

    return {
        "intent": "unknown",
        "response": "Sorry, I couldn't understand your request. Please ask about safety equipment.",
        "products": []
    }