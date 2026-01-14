from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class ProductViewEvent(Base):
    __tablename__ = "product_view_events"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    viewed_at = Column(DateTime(timezone=True), server_default=func.now())
