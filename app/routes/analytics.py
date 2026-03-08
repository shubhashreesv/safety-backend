from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models.product_view_event import ProductViewEvent
from app.models.enquiry_click_event import EnquiryClickEvent

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.post("/product-view/{product_id}")
def log_product_view(product_id: int, db: Session = Depends(get_db)):
    event = ProductViewEvent(product_id=product_id)
    db.add(event)
    db.commit()
    return {"status": "view_logged"}

@router.post("/enquiry-click/{product_id}")
def log_enquiry_click(
    product_id: int,
    quantity: int | None = None,
    option_selected: str | None = None,
    db: Session = Depends(get_db)
):
    event = EnquiryClickEvent(
        product_id=product_id,
        quantity=quantity,
        option_selected=option_selected
    )
    db.add(event)
    db.commit()
    return {"status": "enquiry_logged"}

@router.get("/summary")
def analytics_summary(db: Session = Depends(get_db)):
    total_views = db.query(func.count(ProductViewEvent.id)).scalar()
    total_enquiries = db.query(func.count(EnquiryClickEvent.id)).scalar()

    conversion_rate = 0
    if total_views:
        conversion_rate = round((total_enquiries / total_views) * 100, 2)

    return {
        "total_views": total_views,
        "enquiry_clicks": total_enquiries,
        "conversion_rate": conversion_rate,
    }
