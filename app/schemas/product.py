from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    sku: str
    category: str
    description: Optional[str] = None

class ProductUpdate(BaseModel):
    name: Optional[str]
    category: Optional[str]
    description: Optional[str]
    is_active: Optional[bool]

class ProductResponse(BaseModel):
    id: int
    name: str
    sku: str
    category: str
    description: Optional[str]
    image_url: Optional[str]
    is_active: bool

    class Config:
        from_attributes = True
