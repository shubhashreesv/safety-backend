from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class EnquiryClickEvent(Base):
    __tablename__ = "enquiry_click_events"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=True)
    option_selected = Column(String(100), nullable=True)
    channel = Column(String(50), default="whatsapp")
    clicked_at = Column(DateTime(timezone=True), server_default=func.now())
