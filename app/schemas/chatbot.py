from pydantic import BaseModel
from typing import List, Optional


class ChatRequest(BaseModel):
    message: str


class ChatProduct(BaseModel):
    id: int
    name: str
    image: Optional[str]
    link: str


class ChatResponse(BaseModel):
    intent: str
    response: str
    products: List[ChatProduct]