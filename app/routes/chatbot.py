from fastapi import APIRouter
from app.models.chatbot import ChatRequest, ChatResponse
from app.chatbot.chatbot_engine import get_chatbot_response

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = get_chatbot_response(request.message)

    return ChatResponse(
        response=result["message"],
        products=result["products"]
    )